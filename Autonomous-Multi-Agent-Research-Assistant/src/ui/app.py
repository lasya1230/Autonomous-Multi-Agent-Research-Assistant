import sys
import os
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.orchestrator.controller import ResearchOrchestrator
from src.utils.pdf_exporter import export_report_to_pdf

st.set_page_config(
    page_title="Autonomous Multi-Agent Research Assistant",
    page_icon="✨",
    layout="wide",
)

st.markdown(
    """
    <style>
        .main {
            padding-top: 1rem;
            background: linear-gradient(180deg, #f8fbff 0%, #eef6ff 100%);
        }

        .block-container {
            padding-top: 1.2rem;
            padding-bottom: 2rem;
        }

        .hero-card {
            padding: 1.8rem;
            border-radius: 24px;
            background: linear-gradient(135deg, #60a5fa, #818cf8, #c084fc);
            color: white;
            box-shadow: 0 14px 35px rgba(99, 102, 241, 0.25);
            margin-bottom: 1rem;
        }

        .hero-title {
            font-size: 2.1rem;
            font-weight: 800;
            margin-bottom: 0.4rem;
        }

        .hero-subtitle {
            font-size: 1rem;
            opacity: 0.96;
            margin-bottom: 0.9rem;
        }

        .pill-wrap {
            display: flex;
            gap: 0.55rem;
            flex-wrap: wrap;
            margin-top: 0.8rem;
        }

        .pill {
            background: rgba(255,255,255,0.22);
            padding: 0.38rem 0.85rem;
            border-radius: 999px;
            font-size: 0.85rem;
            border: 1px solid rgba(255,255,255,0.16);
            font-weight: 600;
        }

        .section-card {
            background: rgba(255,255,255,0.82);
            border: 1px solid #dbeafe;
            padding: 1rem;
            border-radius: 18px;
            margin-bottom: 1rem;
            box-shadow: 0 8px 24px rgba(96, 165, 250, 0.08);
        }

        .metric-card {
            background: linear-gradient(180deg, #ffffff, #f8fbff);
            border: 1px solid #dbeafe;
            padding: 1rem;
            border-radius: 18px;
            text-align: center;
            box-shadow: 0 8px 20px rgba(59, 130, 246, 0.08);
        }

        .metric-title {
            font-size: 0.9rem;
            color: #475569;
            margin-bottom: 0.35rem;
            font-weight: 600;
        }

        .metric-value {
            font-size: 1.65rem;
            font-weight: 800;
            color: #1d4ed8;
        }

        .subtask-badge {
            display: inline-block;
            padding: 0.28rem 0.75rem;
            border-radius: 999px;
            background: linear-gradient(90deg, #dbeafe, #ede9fe);
            color: #3730a3;
            font-size: 0.8rem;
            font-weight: 700;
            margin-bottom: 0.65rem;
        }

        .small-muted {
            color: #64748b;
            font-size: 0.92rem;
        }

        div[data-testid="stTextInput"] input {
            border-radius: 14px !important;
            border: 2px solid #bfdbfe !important;
            background-color: white !important;
        }

        div[data-testid="stTextInput"] input:focus {
            border: 2px solid #60a5fa !important;
            box-shadow: 0 0 0 1px #60a5fa !important;
        }

        div.stButton > button,
        div[data-testid="stFormSubmitButton"] > button {
            border-radius: 14px !important;
            background: linear-gradient(90deg, #3b82f6, #8b5cf6) !important;
            color: white !important;
            font-weight: 700 !important;
            border: none !important;
            height: 3rem !important;
            box-shadow: 0 8px 18px rgba(99, 102, 241, 0.2);
        }

        div.stButton > button:hover,
        div[data-testid="stFormSubmitButton"] > button:hover {
            filter: brightness(1.05);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-card">
        <div class="hero-title">Autonomous Multi-Agent Research Assistant</div>
        <div class="hero-subtitle">
            Bright, intelligent research powered by planning, retrieval, analysis, verification, writing, web search, and PDF export.
        </div>
        <div class="pill-wrap">
            <div class="pill">Planner Agent</div>
            <div class="pill">Retriever Agent</div>
            <div class="pill">Analyst Agent</div>
            <div class="pill">Verifier Agent</div>
            <div class="pill">Writer Agent</div>
            <div class="pill">Web Search</div>
            <div class="pill">PDF Export</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.title("⚙️ Controls")
    st.markdown("Customize the research view.")
    show_evidence = st.checkbox("Show retrieved evidence", value=True)
    show_web = st.checkbox("Show web results", value=True)
    show_report = st.checkbox("Show final report", value=True)

    st.markdown("---")
    st.markdown("### 💡 Sample Topics")
    st.caption("Try these:")
    st.code("AI in healthcare", language=None)
    st.code("Impact of generative AI on education", language=None)
    st.code("Benefits and risks of electric vehicles", language=None)

st.markdown("## Start Research")

with st.form("research_form", clear_on_submit=False):
    col1, col2 = st.columns([5, 1])

    with col1:
        research_query = st.text_input(
            "Enter your research question",
            placeholder="Type your topic and press Enter...",
        )

    with col2:
        st.write("")
        st.write("")
        run_clicked = st.form_submit_button("Run Research", use_container_width=True)

if run_clicked:
    if not research_query.strip():
        st.warning("Please enter a research question first.")
    else:
        with st.spinner("Running multi-agent research pipeline..."):
            orchestrator = ResearchOrchestrator()
            result = orchestrator.run(research_query)

        st.success("Research completed successfully.")

        total_subtasks = len(result.get("subtasks", []))
        total_sections = len(result.get("sections", []))

        evidence_count = 0
        verified_count = 0

        for section in result.get("sections", []):
            evidence_count += len(section.get("retrieved_chunks", []))
            if section.get("verification_result", {}).get("verified"):
                verified_count += 1

        m1, m2, m3, m4 = st.columns(4)

        with m1:
            st.markdown(
                """
                <div class="metric-card">
                    <div class="metric-title">Query</div>
                    <div class="metric-value">1</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with m2:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-title">Subtasks</div>
                    <div class="metric-value">{total_subtasks}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with m3:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-title">Evidence Chunks</div>
                    <div class="metric-value">{evidence_count}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with m4:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-title">Verified Sections</div>
                    <div class="metric-value">{verified_count}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("## Research Query")
        st.markdown(
            f"""
            <div class="section-card">
                <div class="small-muted">Submitted topic</div>
                <h4 style="margin-top:0.4rem; color:#1e3a8a;">{result["query"]}</h4>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("## Planned Subtasks")
        for i, subtask in enumerate(result["subtasks"], start=1):
            with st.expander(f"Subtask {i}", expanded=(i == 1)):
                st.markdown(
                    f"""
                    <div class="subtask-badge">Task {i}</div>
                    <div style="font-size:1rem; font-weight:700; color:#312e81;">{subtask}</div>
                    """,
                    unsafe_allow_html=True,
                )

        st.markdown("## Detailed Research Sections")
        for i, section in enumerate(result["sections"], start=1):
            with st.expander(f"Section {i}: {section['subtask']}", expanded=(i == 1)):
                st.markdown("### Summary")
                st.markdown(
                    f"""
                    <div class="section-card">
                        {section["analysis_result"]["summary"]}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                st.markdown("### Key Points")
                key_points = section["analysis_result"].get("key_points", [])
                if key_points:
                    for idx, point in enumerate(key_points, start=1):
                        st.markdown(f"**{idx}.** {point}")
                else:
                    st.write("No key points available.")

                st.markdown("### Verification")
                verification = section["verification_result"]
                c1, c2, c3 = st.columns(3)
                c1.metric("Verified", str(verification.get("verified", False)))
                c2.metric("Confidence", verification.get("confidence", "Low"))
                c3.metric("Evidence Count", verification.get("evidence_count", 0))
                st.info(verification.get("message", "No verification message."))

                if show_evidence:
                    st.markdown("### Retrieved Evidence")
                    retrieved_chunks = section.get("retrieved_chunks", [])
                    if retrieved_chunks:
                        for j, chunk in enumerate(retrieved_chunks, start=1):
                            st.markdown(f"**Chunk {j}** · similarity score: `{round(chunk['score'], 4)}`")
                            st.code(chunk["text"], language=None)
                    else:
                        st.write("No local evidence found.")

                if show_web:
                    st.markdown("### Web Search Results")
                    web_results = section.get("web_results", [])
                    if web_results:
                        for item in web_results:
                            title = item.get("title", "No title")
                            url = item.get("url", "")
                            content = item.get("content", "")

                            st.markdown(
                                f"""
                                <div class="section-card">
                                    <div style="font-weight:800; font-size:1rem; color:#1e3a8a;">{title}</div>
                                    <div class="small-muted" style="margin:0.35rem 0;">{url}</div>
                                    <div>{content}</div>
                                </div>
                                """,
                                unsafe_allow_html=True,
                            )
                    else:
                        st.write("No web results available.")

        if show_report:
            st.markdown("## Final Report")
            st.text_area(
                "Generated Research Report",
                result["final_report"],
                height=420,
            )

            pdf_path = export_report_to_pdf(result["final_report"])
            with open(pdf_path, "rb") as pdf_file:
                st.download_button(
                    label="Download PDF Report",
                    data=pdf_file,
                    file_name="research_report.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                )
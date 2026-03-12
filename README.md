# 🧠 Autonomous Multi-Agent Research Assistant

An **AI-powered research system** that simulates a team of intelligent agents collaborating to perform structured research tasks.

The system automatically **plans research steps, retrieves knowledge, analyzes information, verifies findings, and generates structured reports** through a modern interactive interface.

Built using **Python, Streamlit, vector embeddings, and agent orchestration**, the assistant demonstrates how **agentic AI systems can automate complex research workflows**.

---

# 🚀 Project Overview

The **Autonomous Multi-Agent Research Assistant** is designed to replicate the workflow of a research team by coordinating multiple specialized AI agents.

Each agent performs a specific role in the research pipeline:

- Planning research tasks
- Retrieving relevant information
- Analyzing evidence
- Verifying insights
- Writing structured reports
- Enhancing results using web search

The system provides a **clean and interactive Streamlit interface** that allows users to input a research question and receive a **fully structured research report** with supporting evidence.

---

# ⚙️ System Architecture

The research workflow follows a **multi-agent orchestration pipeline**:

```
User Query
     │
     ▼
Planner Agent
     │
     ▼
Retriever Agent (Vector Search / RAG)
     │
     ▼
Analyst Agent
     │
     ▼
Verifier Agent
     │
     ▼
Writer Agent
     │
     ▼
Final Structured Research Report
```

Additional capabilities include:

- Web search integration for real-time information
- Evidence validation
- PDF report export
- Interactive visualization in the UI

---

# ✨ Key Features

### Multi-Agent Architecture
Implements an agentic workflow where specialized agents collaborate to complete research tasks.

### Research Task Planning
Automatically decomposes complex queries into smaller research subtasks.

### Retrieval-Augmented Generation (RAG)
Uses semantic embeddings to retrieve relevant knowledge from stored documents.

### Evidence-Based Analysis
The system analyzes retrieved information and extracts meaningful insights.

### Verification Layer
Each section is validated against retrieved evidence to ensure reliability.

### Web Search Integration
Enhances results using external web search for additional context.

### Interactive UI
A modern **Streamlit-based interface** allows users to run research queries easily.

### PDF Report Export
Generated research reports can be exported as professional PDF documents.

---

# 🖥️ User Interface

The application includes an interactive UI with:

- Bright and modern design
- Query input with **Enter-to-search support**
- Research subtasks visualization
- Evidence display
- Web search results
- Downloadable research reports

---

# 📁 Project Structure

```
Autonomous-Multi-Agent-Research-Assistant
│
├── data
│   └── outputs
│
├── docs
│
├── src
│   ├── agents
│   │   ├── planner_agent.py
│   │   ├── retriever_agent.py
│   │   ├── analyst_agent.py
│   │   ├── verifier_agent.py
│   │   ├── writer_agent.py
│   │   └── web_search_agent.py
│   │
│   ├── orchestrator
│   │   └── controller.py
│   │
│   ├── rag
│   │   ├── document_loader.py
│   │   ├── text_chunker.py
│   │   ├── embedding_generator.py
│   │   └── retriever.py
│   │
│   ├── ui
│   │   └── app.py
│   │
│   └── utils
│       └── pdf_exporter.py
│
├── tests
│
├── requirements.txt
└── README.md
```

---

# ⚡ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/autonomous-multi-agent-research-assistant.git
```

Navigate to the project directory:

```bash
cd autonomous-multi-agent-research-assistant
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory:

```
TAVILY_API_KEY=your_api_key_here
```

This enables real-time web search integration.

---

# ▶️ Running the Application

Start the Streamlit app:

```bash
streamlit run src/ui/app.py
```

The application will open automatically in your browser.

---

# 🔍 Example Query

```
AI in Healthcare
```

The system will automatically:

1. Break the query into research subtasks  
2. Retrieve supporting information  
3. Analyze insights  
4. Verify findings  
5. Generate a structured research report  

---

# 🛠️ Technologies Used

- Python
- Streamlit
- Sentence Transformers
- Vector Embeddings
- Retrieval-Augmented Generation (RAG)
- Tavily Web Search API
- ReportLab
- Multi-Agent Architecture

---

# 🎯 Use Cases

This project can be used for:

- AI research automation
- Knowledge discovery
- Technical research assistance
- Academic research support
- Agentic AI experimentation

---

# 🚧 Future Improvements

Planned enhancements include:

- LLM-powered summarization
- Knowledge graph integration
- Persistent vector database (Pinecone / FAISS)
- Research citation generation
- Multi-document ingestion
- Improved agent reasoning

---

# 👩‍💻 Author

**Lasya Hanu**

---

# 📄 License

This project is licensed under the MIT License.

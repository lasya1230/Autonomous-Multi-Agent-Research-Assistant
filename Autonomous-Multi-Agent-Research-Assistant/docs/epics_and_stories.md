# Epics and Stories

## Epic 1 — Project Setup and User Interface

### Story 1.1 — Create project folder structure
Create the basic folders for docs, src, data, and tests.

### Story 1.2 — Set up Python virtual environment
Create and activate a virtual environment for the project.

### Story 1.3 — Install required packages
Install Streamlit, Pinecone, OpenAI, python-dotenv, and other required libraries.

### Story 1.4 — Create basic Streamlit app
Create the first Streamlit screen with title and empty layout.

### Story 1.5 — Add research query input box
Allow the user to type a research question.

### Story 1.6 — Add Run Research button
Add a button to start the research workflow.

---

## Epic 2 — RAG and Memory System

### Story 2.1 — Create document loader
Load text or PDF documents into the system.

### Story 2.2 — Create text chunker
Split large text into smaller chunks.

### Story 2.3 — Create embedding generator
Convert text chunks into embeddings.

### Story 2.4 — Connect Pinecone
Set up Pinecone vector database connection.

### Story 2.5 — Store embeddings in Pinecone
Save document embeddings into the vector database.

### Story 2.6 — Retrieve relevant chunks
Search Pinecone and return the most relevant chunks for a query.

---

## Epic 3 — Agent System

### Story 3.1 — Create Planner Agent
Break a research query into smaller subtasks.

### Story 3.2 — Create Retriever Agent
Retrieve relevant context for each subtask.

### Story 3.3 — Create Analyst Agent
Summarize and combine findings from retrieved context.

### Story 3.4 — Create Verifier Agent
Check whether findings are supported by evidence.

### Story 3.5 — Create Writer Agent
Generate the final structured research report.

---

## Epic 4 — Orchestration Flow

### Story 4.1 — Create orchestrator
Build the controller that manages the full agent workflow.

### Story 4.2 — Connect planner to retriever
Pass subtasks from planner agent to retriever agent.

### Story 4.3 — Connect retriever to analyst
Pass retrieved context to analyst agent.

### Story 4.4 — Connect analyst to verifier
Send findings to verifier agent.

### Story 4.5 — Connect verifier to writer
Send verified findings to writer agent.

---

## Epic 5 — Results and Explainability

### Story 5.1 — Show final report in Streamlit
Display the final research output.

### Story 5.2 — Show retrieved evidence
Display chunks used for retrieval.

### Story 5.3 — Show agent logs
Display what each agent did during execution.

### Story 5.4 — Add download/export option
Allow the user to save the research report.

---

## Epic 6 — Basic Testing and Cleanup

### Story 6.1 — Test input and output flow
Check whether query-to-report flow works.

### Story 6.2 — Test Pinecone retrieval
Verify retrieved chunks are relevant.

### Story 6.3 — Improve UI clarity
Make the app cleaner and easier to use.

### Story 6.4 — Clean code and comments
Improve readability for beginner understanding.
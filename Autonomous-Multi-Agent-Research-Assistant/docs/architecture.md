# System Architecture

## Overview

The Autonomous Multi-Agent Research Assistant is designed as a modular AI system where multiple agents collaborate to perform research tasks.

The system accepts a research query from a user, decomposes it into smaller subtasks, retrieves relevant information, analyzes findings, verifies evidence, and generates a structured research report.

---

## High-Level Architecture

The system consists of the following layers:

1. User Interface Layer
2. Orchestrator Layer
3. Agent Layer
4. Retrieval (RAG) Layer
5. Memory Layer

---

## 1. User Interface Layer

Technology: Streamlit

Responsibilities:

* Accept research query from the user
* Display research results
* Display retrieved evidence
* Show agent activity logs

---

## 2. Orchestrator Layer

The orchestrator controls the entire research process.

Responsibilities:

* Receive user query
* Send task to planner agent
* coordinate agent workflow
* collect results from agents
* produce final output

The orchestrator acts as the **central controller** of the system.

---

## 3. Agent Layer

The system contains several specialized agents.

### Planner Agent

Responsibilities:

* understand the research question
* break the query into smaller subtasks

Example:

Input:
Impact of AI in healthcare

Output:

* applications of AI in healthcare
* benefits of AI
* risks of AI
* real-world examples

---

### Retriever Agent

Responsibilities:

* retrieve relevant information from the vector database
* perform semantic search

---

### Analyst Agent

Responsibilities:

* analyze retrieved documents
* summarize important insights

---

### Verifier Agent

Responsibilities:

* verify whether claims are supported by retrieved evidence
* reduce hallucinations

---

### Writer Agent

Responsibilities:

* generate a structured research report
* combine results from other agents

---

## 4. Retrieval Layer (RAG)

RAG stands for Retrieval Augmented Generation.

Responsibilities:

* convert documents into embeddings
* store embeddings in Pinecone
* retrieve relevant chunks using semantic similarity

Components:

* document loader
* text chunker
* embedding generator
* vector search

---

## 5. Memory Layer

Technology: Pinecone Vector Database

Responsibilities:

* store document embeddings
* enable semantic search
* provide long-term knowledge memory

---

## Data Flow

User Query

↓

Planner Agent

↓

Retriever Agent

↓

Vector Database Search

↓

Analyst Agent

↓

Verifie

# Product Brief

## Project Name
Autonomous Multi-Agent Research Assistant

## Project Summary
This project is an AI-based research assistant that uses multiple agents to complete research tasks. It breaks a user query into smaller tasks, retrieves useful information, verifies findings, and generates a structured final report.

## Problem
Doing research manually takes time. Users need to search many sources, organize information, and verify if the results are correct. A simple chatbot may answer questions, but it may not properly verify information or organize it well.

## Proposed Solution
Build a multi-agent research assistant with:
- a Planner Agent to break the task into smaller parts
- a Retriever Agent to find relevant information
- an Analyst Agent to summarize findings
- a Verifier Agent to check whether claims are supported
- a Writer Agent to prepare the final report
- Pinecone vector memory for storing and retrieving context
- a Streamlit UI for user interaction

## Target Users
- Students
- Researchers
- Analysts
- Beginners who need structured research help

## Main Goal
To create a research assistant that gives structured, evidence-based, and AI-verified outputs using multiple collaborating agents.

## In Scope
- multi-agent workflow
- query breakdown
- retrieval using vector database
- verification of findings
- final report generation
- Streamlit UI

## Out of Scope
- login/authentication
- large production deployment
- team collaboration features
- advanced browser automation

## Success Criteria
- User can enter a research query
- System breaks the query into subtasks
- Relevant information is retrieved
- Final answer is structured and easy to read
- Major claims are checked against evidence
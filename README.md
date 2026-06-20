# AdsparkX AI Agent

## Project Overview

AdsparkX AI Agent is a Persona-Aware Customer Support Agent built using Python, Streamlit, LangChain, ChromaDB, and Retrieval-Augmented Generation (RAG).

The system detects user personas, retrieves relevant information from a knowledge base, generates context-aware responses, and escalates sensitive requests to a human agent when required.

## Project Structure

adsparkx-ai-agent/

* data/

  * api_troubleshooting.md
  * billing_policy.txt
  * password_reset_guide.pdf

* agents/

  * persona_detector.py
  * response_generator.py
  * escalation.py

* rag/

  * ingest.py
  * retriver.py

* app.py

* requirements.txt

* README.md

* .env

## Features

* Persona Detection
* Retrieval-Augmented Generation (RAG)
* ChromaDB Vector Database
* Human Escalation Workflow
* Streamlit User Interface
* PDF, TXT, and Markdown Knowledge Base Support

## Run the Application
python -m streamlit run app.py

## Author

SR Suresh

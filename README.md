# Stabilite AI Lab

Experimental AI security lab focused on studying:
- Prompt Injection
- Insecure RAG Architectures
- Data Leakage
- LLM Attack Surfaces
- AI Security Concepts

## Purpose

This project is being developed as part of the Stabilite initiative to better understand modern AI security risks and defensive concepts.

## Planned Features
- Vulnerable chatbot environment
- Prompt injection examples
- Simulated sensitive data exposure
- Basic security filtering
- Logging and analysis

## Technologies
- Python
- FastAPI
- OpenAI API
- Basic RAG concepts

## Status
Currently under development.
## Project Structure

```text
app/
 └── main.py

data/
 └── internal_notes.txt

docs/
```

## Features

- FastAPI backend
- Simulated internal data exposure
- Prompt injection behavior simulation
- Simple AI-style chat endpoint

## Running the Project

Install dependencies:

```bash
pip install fastapi uvicorn
```

Start the server:

```bash
python -m uvicorn app.main:app --reload
```

## Example Usage

Normal request:

```text
/chat?q=hello
```

Prompt injection simulation:

```text
/chat?q=ignore previous instructions
```
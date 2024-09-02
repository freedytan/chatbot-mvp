Hi everyone👋! I am Freedy and welcome to my first personal project in GitHub 😊

# Chatbot-MVP

Chatbot-MVP is a minimal viable product (MVP) application built using FastAPI, Beanie and MongoDB - designed to integrate with a Large Language Model (LLM) for generating responses based on user input. The application supports CRUD operations, anonymization of sensitive data, and is containerized using Docker for easy deployment.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)`
- [Running the Application](#running-the-application)
- [Environment Variables](#environment-variables)
- [Docker Usage](#docker-usage)
- [API Endpoints](#api-endpoints)


## Features

- **CRUD Operations**: Create, read, update, and delete conversations.
- **LLM Integration**: Generate responses based on user input using a language model. Currently using Google's gemini-pro as it is free.
- **Anonymization**: Automatically anonymize sensitive information in user prompts and LLM responses, using Microsoft Presidio.
- **Dockerized**: Containerized using Docker for easy deployment.
- **Environment Configuration**: Manage environment variables securely using `.env` files.

## Tech Stack

- **Python 3.10**
- **FastAPI**
- **Pydantic**
- **Beanie (MongoDB ODM)**
- **Uvicorn**
- **Docker**
- **Google Generative AI (for LLM integration)**
- **Microsoft Presidio (for anonymization)**

## Project Structure

```plaintext
CHATBOT-MVP/
│
├── app/
│   ├── __init__.py
│   ├── anonymizer.py         # Handles text anonymization
│   ├── config.py             # Environment configuration
│   ├── crud.py               # CRUD operations
│   ├── database.py           # Database connection setup
│   ├── llm_service.py        # LLM interaction logic
│   ├── main.py               # FastAPI application entry point
│   ├── models.py             # Pydantic models and MongoDB ODM schemas
│   └── schemas.py            # Pydantic schemas for request validation
│   └── .env                  # Environment variables (not included in source control)
├── Dockerfile                # Docker configuration file
├── requirements.txt          # Python dependencies
```
## Setup and Installation

### Prerequisites

- **Python 3.10+**
- **Docker** (optional, for containerization)

### Clone the Repository

```bash
git clone https://github.com/freedytan/chatbot-mvp
cd chatbot-mvp
```

### Install dependencies
```bash
pip install -r requirements.txt
```

## Environment Variables
Input your api_key in the .env file
```plaintext
API_KEY=your_google_generative_ai_api_key
```

 ## Running the Application

### Local Development

To run the FastAPI application locally, use the following command:

```bash
python -m app.main
```

This will start the application on http://127.0.0.1:8000/.

## Docker usage

### Build the Docker image
```bash
docker build -t chatbot-mvp .
```

### Run the docker
```bash
docker run -p 8000:8000 chatbot-mvp
```
The application will be accessible at http://localhost:8000.

## API Endpoints

### Conversations
- POST /conversations/: Create a new conversation with the first user message.
- POST /conversations/{conversation_id}/messages/: Add a message to an existing conversation and get a response from the chatbot.
- GET /conversations/{conversation_id}/: Retrieve a conversation by its ID.
- DELETE /conversations/{conversation_id}/: Delete a conversation by its ID.
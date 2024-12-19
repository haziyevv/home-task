# NLP Tasks API Documentation

## Overview

The NLP Tasks API is a service that provides natural language processing capabilities through three main endpoints:

### Core Features
- **Text Similarity Analysis**: Compare and detect text similarities with configurable thresholds
- **Instruction-Based Text Processing**: Process text according to specific templates and rules
- **Feedback Implementation**: Apply text modifications based on provided feedback instructions

## Technical Requirements

### System Requirements
- Python 3.12 or higher
- Docker Engine 24.0.0 or higher
- Docker Compose v2.0 or higher

### Dependencies
- FastAPI 0.68.0+
- OpenAI API 1.5.0+
- Uvicorn 0.15.0+
- Additional requirements listed in `requirements.txt`

### API Key Requirements
- OpenAI API key with appropriate permissions

## Installation Guide

### Docker Installation (Recommended)

1. **Clone Repository**
   ```bash
   git clone https://github.com/haziyevv/home-task
   cd home-task
   ```

2. **Configure Environment**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

3. **Build and Start Services**
   ```bash
   docker-compose up --build
   ```

### Manual Installation

1. **Set Up Python Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variable**
   ```bash
   export OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Start Server**
   ```bash
   uvicorn hometask.api:app --host 0.0.0.0 --port 8000
   ```

## API Reference

### Endpoint: Text Similarity Search
`POST /task1`

Analyzes text similarity between two sources and a query.

#### Request Body
```json
{
    "first_text": "string",
    "second_text": "string",
}
```

#### Response
```json
{
    "message": "string",
    "differences": [
        {
            "first_text": "string",
            "second_text": "string"
        }
    ]
}
```

### Endpoint: Instruction Processing
`POST /task2`

Processes text according to provided instructions and templates.

#### Request Body
```json
{
    "template": "string",
    "input_text": "string"
}
```

#### Response
```json
{
    "result": "string",
    "explanation": "string"
}
```

### Endpoint: Feedback Implementation
`POST /task3`

Modifies text based on feedback instructions.

#### Request Body
```json
{
    "text": "string",
    "target": "Which part of the text to modify",
    "instruction": "how to modify the text, edit, add or delete"
}
```

#### Response
```json
{
    "updated_text": "string",
}
```

# NLP Tasks API Documentation

**In order to test the endpoints use examples in tasks.md**

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
   
4. Api will be started at: `http://0.0.0.0:8000` and gradio ui will be started at: `http://localhost:7860` It would be easier to use gradio ui.

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

## Gradio Web Interface

The project includes a user-friendly web interface built with Gradio that provides easy access to all API endpoints.

### Accessing the Interface

When running with Docker:
- Local URL: `http://localhost:7860`
- A public sharing URL will be generated and displayed in the console

### Interface Features

The interface provides three tabs:

1. **Text Similarity**
   - Input fields for two texts
   - Shows similarity analysis results

2. **Instruction Processing**
   - Template input field
   - Text input field
   - Displays processed results with explanations

3. **Feedback Implementation**
   - Text input field
   - Target specification field
   - Instruction field for modifications
   - Shows the updated text after changes

### Running the Interface Separately

To use the Gradio interface:

1. **First, start the FastAPI server:**
   ```bash
   uvicorn hometask.api:app --host 0.0.0.0 --port 8000
   ```

2. **Then, in a separate terminal, run the Gradio interface:**
   ```bash
   python -m hometask.gradio_interface
   ```

Note: The Gradio interface requires the API server to be running and accessible at `http://localhost:8000`.

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

from fastapi import FastAPI, HTTPException
import json
from .task1 import search_query_in_texts  # task1
from .task2 import follow_instructions  # task2
from .task3 import implement_feedback  # task3
from .schemas import (
    TextSearchRequest,
    TextSearchResponse,
    FollowInstructionsRequest,
    FollowInstructionsResponse,
    FeedbackImplementationRequest,
    FeedbackImplementationResponse,
)


app = FastAPI(
    title="HomeTasks API",
    description="API serving various NLP and text processing tasks",
    version="1.0.0"
)

# Models for request/response

# Routes
@app.get("/")
async def root():
    return {"message": "Welcome to HomeTasks API"}

@app.post("/task1", response_model=TextSearchResponse)
async def task1(request: TextSearchRequest):
    """
    Search for a query text in two given texts with approximate matching.
    """
    try:
        result, score1, score2 = search_query_in_texts(
            request.text1,
            request.text2,
            request.query,
            request.similarity_threshold
        )
        return {
            "exists_in_both": result,
            "similarity_scores": {
                "text1": score1,
                "text2": score2
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/task2", response_model=FollowInstructionsResponse)
async def task2(request: FollowInstructionsRequest):
    """
    Endpoint for Task 2 functionality
    """
    try:
        result = follow_instructions(request.template, request.input_text)
        response = json.loads(result)
        return FollowInstructionsResponse(**response)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/task3", response_model=FeedbackImplementationResponse)
async def task3(request: FeedbackImplementationRequest):
    """
    Endpoint for Task 3 functionality
    """
    try:
        # Add your task3 implementation here
        result = implement_feedback(request.text, request.target, request.instruction)
        return FeedbackImplementationResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
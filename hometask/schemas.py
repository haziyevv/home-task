from pydantic import BaseModel
from typing import List, Optional


class TextSimilarityRequest(BaseModel):
    first_text: str
    second_text: str

class TextDiff(BaseModel):
    first_text: str
    second_text: str

class TextSimilarityResponse(BaseModel):
    message: str
    differences: List[TextDiff]

class FollowInstructionsRequest(BaseModel):
    template: str
    input_text: str

class FollowInstructionsResponse(BaseModel):
    result: bool
    explanation: str

class FeedbackImplementationRequest(BaseModel):
    text: str
    target: str
    instruction: str

class FeedbackImplementationResponse(BaseModel):
    updated_text: str

from pydantic import BaseModel
from typing import List, Optional


class TextSearchRequest(BaseModel):
    text1: str
    text2: str
    query: str
    similarity_threshold: Optional[float] = 0.9

class TextSearchResponse(BaseModel):
    exists_in_both: bool
    similarity_scores: dict

class FollowInstructionsRequest(BaseModel):
    template: str
    input_text: str

class FollowInstructionsResponse(BaseModel):
    result: str
    explanation: str

class FeedbackImplementationRequest(BaseModel):
    text: str
    target: str
    instruction: str

class FeedbackImplementationResponse(BaseModel):
    updated_text: str

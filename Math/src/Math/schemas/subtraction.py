from pydantic import BaseModel

class SubtractionRequest(BaseModel):
    num1: float
    num2: float

class SubtractionResponse(BaseModel):
    result: float
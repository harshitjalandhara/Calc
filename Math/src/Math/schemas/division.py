from pydantic import BaseModel

class DivisionRequest(BaseModel):
    num1: float
    num2: float

class DivisionResponse(BaseModel):
    result: float
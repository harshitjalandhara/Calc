from pydantic import BaseModel

class PowerRequest(BaseModel):
    base: float
    exponent: float

class PowerResponse(BaseModel):
    result: float

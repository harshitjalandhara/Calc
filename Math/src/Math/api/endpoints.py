from fastapi import APIRouter, HTTPException
from src.Math.operations.calculator import add as calculate_add, divide as calculate_divide, multiply as calculate_multiply, subtract as calculate_subtract, power as calculate_power
from src.Math.schemas.addition import AdditionRequest, AdditionResponse
from src.Math.schemas.division import DivisionRequest, DivisionResponse
from src.Math.schemas.multiplication import MultiplicationRequest, MultiplicationResponse
from src.Math.schemas.subtraction import SubtractionRequest, SubtractionResponse
from src.Math.schemas.power import PowerRequest, PowerResponse

router = APIRouter()

@router.post("/add", response_model=AdditionResponse, summary="Performs standard addition of two numbers")
async def add_numbers(request: AdditionRequest):
    """
    Accepts two numbers and returns their sum.

    - **num1**: The first number (can be positive, negative, or a float).
    - **num2**: The second number (can be positive, negative, or a float).
    """
    result = calculate_add(request.num1, request.num2)
    return AdditionResponse(result=result)

@router.post("/divide", response_model=DivisionResponse, summary="Performs basic division of two numbers")
async def divide_numbers(request: DivisionRequest):
    """
    Accepts two numbers and returns their quotient.

    - **num1**: The numerator (can be positive, negative, or a float).
    - **num2**: The denominator (can be positive, negative, or a float).
    """
    if request.num2 == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero.")
    
    result = calculate_divide(request.num1, request.num2)
    return DivisionResponse(result=result)

@router.post("/multiply", response_model=MultiplicationResponse, summary="Performs standard multiplication of two numbers")
async def multiply_numbers(request: MultiplicationRequest):
    """
    Accepts two numbers and returns their product.

    - **num1**: The first number (can be positive, negative, or a float).
    - **num2**: The second number (can be positive, negative, or a float).
    """
    result = calculate_multiply(request.num1, request.num2)
    return MultiplicationResponse(result=result)

@router.post("/subtract", response_model=SubtractionResponse, summary="Performs standard subtraction of two numbers")
async def subtract_numbers(request: SubtractionRequest):
    """
    Accepts two numbers and returns their difference.

    - **num1**: The first number (can be positive, negative, or a float).
    - **num2**: The second number (can be positive, negative, or a float).
    """
    result = calculate_subtract(request.num1, request.num2)
    return SubtractionResponse(result=result)

@router.post("/power", response_model=PowerResponse, summary="Calculates the power of a number (base raised to an exponent)")
async def power_number(request: PowerRequest):
    """
    Accepts a base and an exponent, and returns the base raised to the power of the exponent.

    - **base**: The base number (can be positive, negative, or a float).
    - **exponent**: The exponent (can be positive, negative, or a float).
    """
    result = calculate_power(request.base, request.exponent)
    return PowerResponse(result=result)

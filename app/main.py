from fastapi import FastAPI, HTTPException
from app.services.fibonacci import calculate_fibonacci
from app.services.factorial import calculate_factorial
from app.services.loan import calculate_monthly_payment
from app.models.schemas import LoanRequest



app = FastAPI()

@app.get("/")
def root():
    return {"message": "Ikano assignment API by Dimitra Siskou"}

@app.get("/fibonacci/{n}",
         summary="Calculate the Fibonacci number")
def fibonacci(n: int):

    try:
        result = calculate_fibonacci(n)
        return {"result": result}

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

@app.get("/factorial/{n}", 
         summary="Calculate the factorial of a number")
def factorial(n: int):

    try:
        result = calculate_factorial(n)
        return {"result": result}

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )
    
@app.post("/loan_repayment",
         summary="Calculate monthly loan repayment")
def loan(request: LoanRequest):

    try:
        result = calculate_monthly_payment(
            request.principal, 
            request.annual_rate, 
            request.months)
        return {"monthly_payment": result}

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )
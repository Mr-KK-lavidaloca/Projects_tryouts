"""
FAST api app- Web api basics
""" 
from fastapi import FastAPI ,HTTPException
from .calculator import calculate 
from .models import CalculationRequest,CalculationResponse,OperationType

app=FastAPI(
    title="Caculator API",
    description="A simple calculator with pytho and fast api",
    version="1.0.0"
)
@app.get("/")
async def root():
  """ Learn Basic endpoint"""
  return{ "message":"calculator API","status":"running "}

@app.get("/calculate/{operation}")
async def calculate_get(operation:OperationType,a:float,b:float):
  """
  path parmeters and query parameters
  eg/calculate/add?a=10&b=5
  """
  result=calculate(operation.value,a,b)
  return CalculationResponse(**result)

@app.post("/calculate")  
async def calculate_post(request: CalculationRequest):
    """
    POST requests with JSON body
    """
    result = calculate(request.operation.value, request.a, request.b)
    return CalculationResponse(**result)

@app.get("/operations")
async def list_operations():
    return {
        "operations": [op.value for op in OperationType],
        "count": len(OperationType)
    }
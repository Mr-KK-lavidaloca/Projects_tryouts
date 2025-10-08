"""
simple data models-Learn pydantic basics
"""
from pydantic import BaseModel
from enum import Enum 

class OperationType(str,Enum):
    # supported operation-Learn Enums
    ADD="add"
    SUBTRACT="subtract"
    MULTIPLY="multiply"
    DIVIDE="divide"

class CalculationRequest(BaseModel):
    """ Request Model-learns data validation """
    a:float
    b:float
    operation:OperationType 

class CalculationResponse(BaseModel):
    """ Response Model - Learn API contracts"""
    success:bool  # ← Type annotation
    result:float | None=None  # union type | from 3.10 onwards
    error:str | None=None
    operation:str
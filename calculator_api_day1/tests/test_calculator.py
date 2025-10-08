import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))
"""
tests for calculator functions
"""
import pytest
from src.calculator_api.calculator import calculate

def test_add():
    """ basic function test"""
    result=calculate("add",10,5)
    assert result["success"] == True
    assert result["result"] == 15

def test_subtract():
    result = calculate("subtract", 10, 5)
    assert result["success"] == True
    assert result["result"] == 5


def test_multiply():
    result = calculate("multiply", 10, 5)
    assert result["success"] == True
    assert result["result"] == 50


def test_divide():
    result = calculate("divide", 10, 5)
    assert result["success"] == True
    assert result["result"] == 2

def test_divide_by_zero():
  result=calculate("divide",10,0)
  assert result["success"]==False
  assert "cannot divide by zero" in result["error"]

@pytest.mark.parametrize("a,b,expected",[
    (2, 3, 5),
    (0, 5, 5),
    (-1, 1, 0),
    (2.5, 2.5, 5.0)
])

def test_addition_various_inputs(a,b, expected):
    result=calculate("add",a,b)
    assert result["result"]==expected
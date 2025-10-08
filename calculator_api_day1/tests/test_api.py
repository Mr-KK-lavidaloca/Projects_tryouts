from fastapi.testclient import TestClient
from src.calculator_api.app import app
from src.calculator_api.models import OperationType

client=TestClient(app)

def test_root():
    """ Tests the API root endpoint returns correct structure"""
    response=client.get("/")
    assert response.status_code == 200
    response_data=response.json()
    assert "message" in response_data
    assert "status" in response_data

def test_calculate_get():
    """ test post endpoint with json request body"""
       # ACT: Call GET endpoint with URL parameters
    response=client.get("/calculate/add?a=10&b=5")
        # ASSERT: Verify successful response with correct calculation
    assert response.status_code == 200
    data=response.json()
    assert data["success"]==True
    assert data["result"]==15
    assert data["operation"]=="add"

def test_calculate_post():
    """tests POST endpoints with json request body """
         # ACT: Call POST endpoint with JSON payload
    response=client.post("/calculate",json={
        "a":20,
        "b":4,
        "operation":"multiply"
    })

    #ASSERT:Verify successful response with correct calculation
    assert response.status_code == 200
    data=response.json()
    assert data["success"]==True
    assert data["result"]==80
    assert data["operation"]=="multiply"

def test_division_by_zero_api():
    response =client.get("/calculate/divide?a=10&b=0")
        # ASSERT: Verify error response structure (not HTTP error)
    assert response.status_code == 200 # Our custom error handling returns 200
    data=response.json()
    assert data["success"]==False
    assert "error" in data
    assert "cannot divide by zero" in data["error"]

def test_list_operation():
    response=client.get("/operations")
    assert response.status_code==200
    data=response.json()
    assert "operations" in data
    assert "count" in data
    assert len(data["operations"])==4
    expected_operations=[op.value for op in OperationType]
    assert data["operations"] == expected_operations
    assert data["count"] == len(OperationType)
# Calculator REST API 🧮

A production-ready REST API calculator built with FastAPI and Python. Features comprehensive error handling, testing, and professional code structure.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)

## 🚀 Features

- **RESTful API** with FastAPI
- **Mathematical Operations**: Add, Subtract, Multiply, Divide
- **Comprehensive Error Handling** with meaningful error messages
- **Full Test Coverage** with pytest
- **Auto-generated API Documentation** (Swagger & ReDoc)
- **Production-ready Code Structure**
- **Input Validation** with Pydantic models
- **Type Hints** throughout the codebase

## 🛠️ Tech Stack

- **Python 3.8+**
- **FastAPI** - Modern web framework
- **Pydantic** - Data validation
- **pytest** - Testing framework
- **Uvicorn** - ASGI server

## 📁 Project Structure
````
day1-calculator-api/
├── src/
│ └── calculator_api/
│ ├── init.py
│ ├── app.py # FastAPI application & routes
│ ├── calculator.py # Business logic & operations
│ └── models.py # Pydantic data models
├── tests/
│ ├── init.py
│ ├── test_api.py # API endpoint integration tests
│ └── test_calculator.py # Core logic unit tests
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .gitignore # Git ignore rules
└── run.bat # Windows startup script
````

## 🏃‍♂️ Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/day1-calculator-api.git
cd day1-calculator-api
```
Install dependencies

```bash
pip install -r requirements.txt
```
Run the application

Option A: Using the batch file (Windows)

```bash
run.bat
```
Option B: Manual command

```bash
cd src
uvicorn calculator_api.app:app --reload --host 0.0.0.0 --port 8000
```
Access the API

API will be running at: http://localhost:8000

Interactive documentation: http://localhost:8000/docs

Alternative documentation: http://localhost:8000/redoc

📚 API Documentation
Endpoints
GET /

Description: Root endpoint with API information

Response: API status and version

GET /calculate/{operation}
Description: Perform calculation via GET request

Parameters:

operation (path): add, subtract, multiply, divide

a (query): First number

b (query): Second number

Example: GET /calculate/add?a=10&b=5

POST /calculate
Description: Perform calculation via POST request with JSON body

Request Body:

```json
{
  "a": 10,
  "b": 5,
  "operation": "add"
}
```
GET /operations
Description: List all available operations

Response: Array of supported operations

Response Format
All endpoints return a consistent JSON response:

```json
{
  "success": true,
  "result": 15.0,
  "error": null,
  "operation": "add"
}
```
🧪 Testing
Run All Tests
```bash
pytest tests/
```
Run with Verbose Output
```bash
pytest tests/ -v
```
Run with Coverage Report
bash
```pytest tests/ --cov=calculator_api --cov-report=html
```
Test Examples
✅ Basic arithmetic operations

✅ Error handling (division by zero)

✅ Input validation

✅ API endpoint responses

🔧 Development
Project Setup for Development
Create virtual environment:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```
Install development dependencies:

```bash
pip install -r requirements.txt
```
Code Quality
Type hints throughout the codebase

Comprehensive error handling

Consistent code style

Modular architecture

🐛 Error Handling
The API provides clear error messages for:

Division by zero: {"success": false, "error": "cannot divide by zero"}

Invalid operations: {"success": false, "error": "Unknown operation"}

Invalid inputs: Proper validation with Pydantic models

🌐 API Usage Examples
Using curl
```bash
# Addition
curl "http://localhost:8000/calculate/add?a=10&b=5"

# Division with error
curl "http://localhost:8000/calculate/divide?a=10&b=0"

# POST request
curl -X POST "http://localhost:8000/calculate" \
  -H "Content-Type: application/json" \
  -d '{"a": 15, "b": 3, "operation": "multiply"}'
```
Using Python requests
```python
import requests

# GET request
response = requests.get("http://localhost:8000/calculate/add?a=10&b=5")
print(response.json())

# POST request
data = {"a": 20, "b": 4, "operation": "divide"}
response = requests.post("http://localhost:8000/calculate", json=data)
print(response.json())
```
📊 Learning Outcomes
This project demonstrates:

✅ REST API design with FastAPI

✅ Python functions and error handling

✅ Pydantic data validation

✅ Comprehensive testing strategy

✅ Project structure and organization

✅ Git version control

✅ API documentation

✅ Production code quality

🤝 Contributing
Fork the repository

Create a feature branch: git checkout -b feature/new-operation

Commit changes: git commit -m 'Add new operation'

Push to branch: git push origin feature/new-operation

Submit a pull request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Author
Your Name

GitHub: @Mr-KK-lavidaloca

Project Link: https://github.com/your-username/day1-calculator-api

⭐ Star this repository if you find it helpful!

```text

## **How to Use This:**

1. **Copy the entire text above**
2. **Create a new file** called `README.md` in your project folder
3. **Paste the content**
4. **Replace** `your-username` with your actual GitHub username
5. **Save the file**

## **What Makes This Professional:**
- ✅ **Badges** for visual appeal
- ✅ **Clear structure** with emojis
- ✅ **Comprehensive documentation**
- ✅ **Usage examples**
- ✅ **Development guide**
- ✅ **Professional formatting**

**This README will impress recruiters and help other developers understand your project!** 🚀
```

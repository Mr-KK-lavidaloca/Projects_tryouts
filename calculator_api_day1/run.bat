@echo off
cd src
uvicorn calculator_api.app:app --reload --host 0.0.0.0 --port 8000
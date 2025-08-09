# FastAPI Hello World Demo

A simple FastAPI application that returns a "Hello World" message.

## Installation

```bash
pip install -r requirements.txt
```

## Running the application

```bash
python main.py
```

Or you can use uvicorn directly:

```bash
uvicorn main:app --reload
```

## API Endpoints

- GET `/`: Returns a JSON response with a "Hello World" message
- GET `/docs`: Interactive API documentation (provided by Swagger UI)
- GET `/redoc`: Alternative API documentation (provided by ReDoc)


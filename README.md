# FastAPI Hello World Demo

A simple FastAPI application that returns a "Hello World" message with both API and frontend interfaces.

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

## Accessing the Application

- Frontend: Open http://localhost:8000 in your browser to see the HTML interface
- API: Access http://localhost:8000/api/hello for the JSON response

## API Endpoints

- GET `/`: Returns the HTML frontend
- GET `/api/hello`: Returns a JSON response with a "Hello World" message
- GET `/docs`: Interactive API documentation (provided by Swagger UI)
- GET `/redoc`: Alternative API documentation (provided by ReDoc)

## Project Structure

- `main.py`: FastAPI application
- `requirements.txt`: Project dependencies
- `templates/`: HTML templates
- `static/`: Static files (CSS, JavaScript)



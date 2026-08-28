# Task API

A simple CRUD API for managing a to-do list, built with Python and FastAPI.

## Features

- Create tasks
- Retrieve all tasks
- Retrieve a task by ID
- Update tasks
- Delete tasks
- Input validation
- Health check endpoint
- Interactive API documentation with Swagger UI

## Tech Stack

- Python 3.14+
- FastAPI
- Uvicorn
- Pydantic

## Project Structure

    CRUD_API/
    ├── main.py
    ├── requirements.txt
    ├── README.md
    └── .gitignore

## Setup

### 1. Clone the repository

    git clone <YOUR_GITHUB_REPOSITORY_URL>
    cd CRUD_API

### 2. Create a virtual environment

    python3 -m venv .venv

### 3. Activate the virtual environment

Linux/macOS:

    source .venv/bin/activate

Windows:

    .venv\Scripts\activate

### 4. Install dependencies

    pip install -r requirements.txt

## Run the API

Start the development server with:

    python -m uvicorn main:app --reload

The API will be available at:

    http://localhost:8000

## API Documentation

FastAPI automatically generates interactive Swagger UI documentation.

Open:

    http://localhost:8000/docs

You can use Swagger UI to test all API endpoints directly from your browser.

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Get API information |
| GET | `/health` | Health check |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{id}` | Get a task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{id}` | Update an existing task |
| DELETE | `/tasks/{id}` | Delete a task |

## Example Task

    {
      "id": 1,
      "title": "Learn FastAPI",
      "done": false
    }

## Data Storage

Tasks are currently stored in an in-memory Python list.

Data is reset whenever the API server restarts.

## Testing

The API can be tested interactively using Swagger UI:

    http://localhost:8000/docs

The following operations can be tested:

- Creating a task with `POST /tasks`
- Retrieving tasks with `GET /tasks` and `GET /tasks/{id}`
- Updating tasks with `PUT /tasks/{id}`
- Deleting a task with `DELETE /tasks/{id}`
- Testing validation and error responses
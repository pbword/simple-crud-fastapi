from fastapi import FastAPI

app = FastAPI(
    title="Task API",
    description="A simple CRUD API built using FastAPI.",
    version="1.0"
)


@app.get("/", summary="Get API information")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": [
            "/tasks"
        ]
    }


@app.get("/health", summary="Health check")
def health():
    return {
        "status": "ok"
    }
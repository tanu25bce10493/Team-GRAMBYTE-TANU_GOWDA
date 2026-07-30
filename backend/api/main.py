from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="SyncReserve AI API",
    description="Backend API for the SyncReserve AI project.",
    version="1.0.0",
)

# CORS Configuration
# During development we allow the local frontend servers.
origins = [
    "http://localhost:5500",  # VS Code Live Server
    "http://127.0.0.1:5500",
    "http://localhost:3000",  # Optional
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "Welcome to SyncReserve AI Backend"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "SyncReserve AI API",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }
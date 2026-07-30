from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.schemas import BookingRequest

app = FastAPI(
    title="SyncReserve AI API",
    description="Backend API for the SyncReserve AI project.",
    version="1.0.0",
)

origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://localhost:3000",
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


@app.post("/api/book")
def create_booking(booking: BookingRequest):
    """
    Temporary endpoint.
    The bridge integration will be added in a later commit.
    """
    return {
        "message": "Booking request received",
        "data": booking.model_dump()
    }
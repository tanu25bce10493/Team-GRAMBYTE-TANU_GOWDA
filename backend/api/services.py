from datetime import datetime

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from backend.api.schemas import BookingRequest, BookingResponse
from backend.api.services import book_resource
from backend.api.exceptions import (
    BookingException,
    booking_exception_handler,
    generic_exception_handler,
)

app = FastAPI(
    title="SyncReserve AI API",
    description="Backend API for the SyncReserve AI project.",
    version="1.0.0",
)

# Register exception handlers
app.add_exception_handler(
    BookingException,
    booking_exception_handler,
)

app.add_exception_handler(
    Exception,
    generic_exception_handler,
)

# CORS Configuration
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


@app.post(
    "/api/book",
    response_model=BookingResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
def create_booking(booking: BookingRequest):

    result = book_resource(booking)

    return BookingResponse(
        success=result["success"],
        status=result["status"],
        message=result["message"],
        booking=booking,
    )
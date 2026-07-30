from fastapi import Request
from fastapi.responses import JSONResponse


class BookingException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code


async def booking_exception_handler(
    request: Request,
    exc: BookingException,
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "status": exc.status_code,
            "message": exc.message,
        },
    )


async def generic_exception_handler(
    request: Request,
    exc: Exception,
):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "status": 500,
            "message": "Unable to process booking request.",
        },
    )
from pydantic import BaseModel, Field


class BookingRequest(BaseModel):
    student_id: str = Field(..., min_length=1)
    resource_id: str = Field(..., min_length=1)
    start_time: str
    end_time: str


class BookingResponse(BaseModel):
    success: bool
    status: int
    message: str
    booking: BookingRequest
from fastapi import status

# ...

@app.post(
    "/api/book",
    response_model=BookingResponse,
    status_code=status.HTTP_202_ACCEPTED
)
def create_booking(booking: BookingRequest):

    return BookingResponse(
        success=True,
        status=status.HTTP_202_ACCEPTED,
        message="Booking request accepted",
        booking=booking,
    )
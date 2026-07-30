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
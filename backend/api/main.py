@app.post(
    "/api/book",
    response_model=BookingResponse,
    status_code=status.HTTP_202_ACCEPTED
)
def create_booking(booking: BookingRequest):

    bridge_response = process_booking(booking)

    return BookingResponse(
        success=bridge_response["success"],
        status=bridge_response["status"],
        message=bridge_response["message"],
        booking=booking,
    )
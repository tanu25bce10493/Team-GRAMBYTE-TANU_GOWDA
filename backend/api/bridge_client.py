from backend.api.schemas import BookingRequest


def process_booking(booking: BookingRequest) -> dict:
    """
    Temporary bridge wrapper.

    This function will later call the real Python bridge
    that communicates with the C++ scheduling engine.
    """

    return {
        "success": True,
        "status": 200,
        "message": f"Booking confirmed for Resource {booking.resource_id}",
        "latency_ms": 0.14,
        "booking": {
            "student_id": booking.student_id,
            "resource_id": booking.resource_id,
            "start_time": booking.start_time,
            "end_time": booking.end_time,
        },
    }
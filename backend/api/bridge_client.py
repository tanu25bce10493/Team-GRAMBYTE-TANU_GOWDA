from backend.api.schemas import BookingRequest


def process_booking(booking: BookingRequest) -> dict:
    """
    Temporary bridge wrapper.

    Later this function will call the Python bridge
    that communicates with the C++ scheduling engine.

    For now, it simply returns a mock response using
    the incoming booking request.
    """

    return {
        "success": True,
        "status": 200,
        "message": f"Booking confirmed for Resource {booking.resource_id}",
        "latency_ms": 0.12,
        "resource_id": booking.resource_id,
        "booked_by": booking.booked_by,
        "start_time": booking.start_time,
        "end_time": booking.end_time,
    }
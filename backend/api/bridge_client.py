from backend.api.schemas import BookingRequest


def process_booking(booking: BookingRequest) -> dict:
    """
    Temporary bridge implementation.

    This function will later be replaced by the real
    Python-to-C++ bridge developed by Member 4.
    """

    return {
        "success": True,
        "status": 200,
        "message": "Slot is available",
        "latency_ms": 0.14
    }
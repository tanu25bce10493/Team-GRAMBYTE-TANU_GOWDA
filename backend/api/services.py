from backend.api.bridge_client import process_booking
from backend.api.schemas import BookingRequest


def book_resource(booking: BookingRequest) -> dict:
    """
    Handles the booking workflow.

    Currently forwards the request to the bridge layer.
    Future responsibilities:
    - AI recommendations
    - Waitlist handling
    - Audit logging
    - Business rule validation
    """

    bridge_response = process_booking(booking)

    return bridge_response
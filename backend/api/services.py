from datetime import datetime, timedelta

from backend.api.bridge_client import process_booking
from backend.api.exceptions import BookingException
from backend.api.schemas import BookingRequest


def book_resource(booking: BookingRequest) -> dict:
    """
    Handles booking workflow before forwarding
    the request to the bridge layer.
    """

    start = datetime.fromisoformat(booking.start_time)
    end = datetime.fromisoformat(booking.end_time)

    if start >= end:
        raise BookingException(
            "End time must be later than start time.",
            400,
        )

    if end - start > timedelta(hours=4):
        raise BookingException(
            "Maximum booking duration is 4 hours.",
            400,
        )

    return process_booking(booking)
from datetime import datetime, timedelta

from backend.api.bridge_client import process_booking
from backend.api.exceptions import BookingException
from backend.api.schemas import BookingRequest


def book_resource(booking: BookingRequest) -> dict:
    """
    Handles booking workflow before forwarding
    the request to the bridge layer.
    """

    # Validate datetime format
    try:
        start = datetime.fromisoformat(booking.start_time)
        end = datetime.fromisoformat(booking.end_time)

    except ValueError:
        raise BookingException(
            "Invalid date/time format. Please use ISO 8601 format (YYYY-MM-DDTHH:MM:SS).",
            400,
        )

    # Validate booking time
    if start >= end:
        raise BookingException(
            "End time must be later than start time.",
            400,
        )

    # Maximum booking duration
    if end - start > timedelta(hours=4):
        raise BookingException(
            "Maximum booking duration is 4 hours.",
            400,
        )

    # Forward request to bridge layer
    try:
        return process_booking(booking)

    except Exception as e:
        import traceback

        traceback.print_exc()

        raise BookingException(
            str(e),
            500,
        )
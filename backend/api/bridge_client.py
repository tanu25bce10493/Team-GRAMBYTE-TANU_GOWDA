import time

from backend.api.schemas import BookingRequest
from backend.bridge.bridge import run_cpp_engine


def process_booking(booking: BookingRequest) -> dict:
    """
    Sends the booking request to the Python bridge,
    which invokes the C++ scheduling engine.
    """

    start = time.perf_counter()

    response = run_cpp_engine(
        booking.resource_id,
        booking.start_time,
        booking.end_time
    )

    latency = round((time.perf_counter() - start) * 1000, 2)

    response["latency_ms"] = latency

    if response.get("success"):
        response["booking"] = {
            "student_id": booking.student_id,
            "resource_id": booking.resource_id,
            "start_time": booking.start_time,
            "end_time": booking.end_time,
        }

    return response
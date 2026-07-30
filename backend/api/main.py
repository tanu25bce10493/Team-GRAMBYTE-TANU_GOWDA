from backend.api.exceptions import (
    BookingException,
    booking_exception_handler,
    generic_exception_handler,
)

app.add_exception_handler(
    BookingException,
    booking_exception_handler,
)

app.add_exception_handler(
    Exception,
    generic_exception_handler,
)
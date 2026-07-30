#include <iostream>

#include "../include/GraphEngine.hpp"

int main()
{
    GraphEngine engine;

    // Create a sample resource
    Resource lab{
    1,
    "Computer Lab",
    40
    };

    engine.addResource(lab);

    // First booking
    Booking booking1{
    1,
    1,
    "Alice",
    "10:00",
    "11:00"
    };

    if (engine.createBooking(booking1))
    {
        std::cout << "Booking 1 Successful\n";
    }
    else
    {
        std::cout << "Booking 1 Failed\n";
    }

    // Second booking (Overlaps)
    Booking booking2;
    booking2.bookingId = 2;
    booking2.resourceId = 1;
    booking2.bookedBy = "Bob";
    booking2.startTime = "10:30";
    booking2.endTime = "11:30";

   std::cout
    << "Booking 2: "
    << (engine.createBooking(booking2)
        ? "Successful"
        : "Failed (Conflict Detected)")
    << '\n';

    return 0;
}
#include <iostream>

#include "../include/GraphEngine.hpp"

int main()
{
    GraphEngine engine;

    // Create a sample resource
    Resource lab;
    lab.id = 1;
    lab.name = "Computer Lab";
    lab.capacity = 40;

    engine.addResource(lab);

    // First booking
    Booking booking1;
    booking1.bookingId = 1;
    booking1.resourceId = 1;
    booking1.userId = "Alice";
    booking1.startTime = "10:00";
    booking1.endTime = "11:00";

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
    booking2.userId = "Bob";
    booking2.startTime = "10:30";
    booking2.endTime = "11:30";

    if (engine.createBooking(booking2))
    {
        std::cout << "Booking 2 Successful\n";
    }
    else
    {
        std::cout << "Booking 2 Failed (Conflict Detected)\n";
    }

    return 0;
}
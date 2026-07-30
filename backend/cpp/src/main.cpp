#include <iostream>
#include <string>

#include "../include/GraphEngine.hpp"

int main(int argc, char* argv[])
{
    // Expected:
    // SyncReserveAI.exe <resource_id> <start_time> <end_time>

    if (argc != 4)
    {
        std::cout << R"({
    "success": false,
    "status": 400,
    "message": "Invalid arguments"
})";

        return 1;
    }

    std::string resourceId = argv[1];
    std::string startTime = argv[2];
    std::string endTime = argv[3];

    GraphEngine engine;

    // Temporary resource for demo
    Resource lab{
        1,
        resourceId,
        40
    };

    engine.addResource(lab);

    Booking booking;

    booking.bookingId = 1;
    booking.resourceId = 1;
    booking.bookedBy = "API";
    booking.startTime = startTime;
    booking.endTime = endTime;

    bool success = engine.createBooking(booking);

    if (success)
    {
        std::cout << R"({
    "success": true,
    "status": 200,
    "message": "Booking confirmed"
})";
    }
    else
    {
        std::cout << R"({
    "success": false,
    "status": 409,
    "message": "Resource already booked"
})";
    }

    return 0;
}
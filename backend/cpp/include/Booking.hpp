#ifndef BOOKING_HPP
#define BOOKING_HPP

#include <string>

struct Booking
{
    int bookingId;
    int resourceId;
    std::string bookedBy;

    std::string startTime;
    std::string endTime;
};

#endif
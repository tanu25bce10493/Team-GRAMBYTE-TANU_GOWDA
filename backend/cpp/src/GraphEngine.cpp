#include "../include/GraphEngine.hpp"

void GraphEngine::addResource(const Resource& resource)
{
    resources.push_back(resource);
}

void GraphEngine::addBooking(const Booking& booking)
{
    bookings.push_back(booking);
}

bool GraphEngine::isResourceAvailable(
    int resourceId,
    const std::string& startTime,
    const std::string& endTime
) const
{
    for (const Booking& booking : bookings)
    {
        // Skip bookings for other resources
        if (booking.resourceId != resourceId)
        {
            continue;
        }

        // Check for time overlap
        bool overlap =
            (startTime < booking.endTime) &&
            (endTime > booking.startTime);

        if (overlap)
        {
            return false;
        }
    }

    return true;
}
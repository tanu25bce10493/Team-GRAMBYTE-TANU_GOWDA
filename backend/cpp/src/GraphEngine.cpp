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
        if (booking.resourceId != resourceId)
        {
            continue;
        }

        // Time intervals overlap if:
        // requestedStart < existingEnd
        // AND
        // requestedEnd > existingStart
        if (startTime < booking.endTime &&
            endTime > booking.startTime)
        {
            return false;
        }
    }

    return true;
}
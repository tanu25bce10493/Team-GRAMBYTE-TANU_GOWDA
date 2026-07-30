#include "../include/GraphEngine.hpp"

void GraphEngine::addResource(const Resource& resource)
{
    resources.push_back(resource);
}

bool GraphEngine::createBooking(const Booking& booking)
{
    if (!isResourceAvailable(
            booking.resourceId,
            booking.startTime,
            booking.endTime))
    {
        return false;
    }

    bookings.push_back(booking);
    return true;
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
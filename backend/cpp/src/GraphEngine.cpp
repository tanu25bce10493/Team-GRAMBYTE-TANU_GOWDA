#include "../include/GraphEngine.hpp"

void GraphEngine::addResource(const Resource& resource)
{
    resources.push_back(resource);
}

void GraphEngine::addBooking(const Booking& booking)
{
    bookings.push_back(booking);
} 
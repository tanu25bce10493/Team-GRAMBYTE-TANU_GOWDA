#ifndef GRAPH_ENGINE_HPP
#define GRAPH_ENGINE_HPP

#include <vector>

#include "Resource.hpp"
#include "Booking.hpp"

class GraphEngine
{
private:
    std::vector<Resource> resources;
    std::vector<Booking> bookings;

public:
    void addResource(const Resource& resource);
    void addBooking(const Booking& booking);
};

#endif
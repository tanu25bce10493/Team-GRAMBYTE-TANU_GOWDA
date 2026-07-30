#ifndef GRAPH_ENGINE_HPP
#define GRAPH_ENGINE_HPP

#include <vector>
#include <string>
#include "Resource.hpp"
#include "Booking.hpp"

class GraphEngine
{
private:
    std::vector<Resource> resources;
    std::vector<Booking> bookings;

public:
    void addResource(const Resource& resource);
    bool createBooking(const Booking& booking);

    bool isResourceAvailable(
        int resourceId,
        const std::string& startTime,
        const std::string& endTime
    ) const;
};

#endif
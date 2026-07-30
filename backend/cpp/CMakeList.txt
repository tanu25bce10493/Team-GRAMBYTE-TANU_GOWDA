cmake_minimum_required(VERSION 3.20)

project(SyncReserveAI)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories(include)

add_executable(
    SyncReserveAI

    src/main.cpp
    src/Resource.cpp
    src/Booking.cpp
    src/GraphEngine.cpp
)
cmake_minimum_required(VERSION 3.29)
project(cpp)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)
include_directories(hello-world)
include_directories(hello-world/test)

add_executable(cpp
    hello-world/test/catch.hpp
    hello-world/test/tests-main.cpp
    hello-world/hello_world.cpp
    hello-world/hello_world.h
    hello-world/hello_world_test.cpp
        lasagna/lasagna.cpp
        lasagna/lasagna_test.cpp)

cmake_minimum_required(VERSION 2.8.3)
project(dubins-test)

FIND_PACKAGE(Boost COMPONENTS program_options REQUIRED)

## Add support for C++11, supported in ROS Kinetic and newer
add_definitions(-std=c++11)

include("FindOMPL.cmake")

include_directories(${OMPL_INCLUDE_DIRS}
                    ${Boost_INCLUDE_DIRS})

add_executable(${PROJECT_NAME}   src/GeometricCarPlanning.cpp)

set(COMMON_LIBRARIES  ${OMPL_LIBRARIES}
                      ${Boost_LIBRARIES})
## Specify libraries to link a library or executable target against
target_link_libraries(${PROJECT_NAME} ${COMMON_LIBRARIES})


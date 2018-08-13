cmake_minimum_required(VERSION 2.8.3)
project(xytheta)

find_package(SBPL REQUIRED sbpl)


## Add support for C++11, supported in ROS Kinetic and newer
add_definitions(-std=c++11)


include_directories(${SBPL_INCLUDE_DIRS})

add_executable(${PROJECT_NAME}   src/xytheta.cpp)

set(COMMON_LIBRARIES  ${SBPL_LIBRARIES})
## Specify libraries to link a library or executable target against
target_link_libraries(${PROJECT_NAME} ${COMMON_LIBRARIES})


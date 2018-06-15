cmake_minimum_required(VERSION 2.8)
project( capture )

INCLUDE(FindPkgConfig)

# Find OpenCV
find_package( OpenCV 3.4.1 REQUIRED )

# Find V4L2 library
find_library( V4L2_lib v4l2 REQUIRED )

#Add the source files
file(GLOB SOURCES_CPP "*.cpp")

#Add Executable
add_executable(cap ${SOURCES_CPP})

target_link_libraries( cap ${OpenCV_LIBS} ${V4L2_lib} )

#EOF

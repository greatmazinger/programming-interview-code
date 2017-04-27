CMAKE_MINIMUM_REQUIRED(VERSION 3.3)
PROJECT(CircularBufferLib)

# ADD_EXECUTABLE(cbtest circbuffer_test.cpp)
# ADD_LIBRARY(circbuffer circbuffer_test.cpp)

FIND_PACKAGE( Boost 1.40 COMPONENTS program_options REQUIRED )
INCLUDE_DIRECTORIES( ${Boost_INCLUDE_DIR} )

SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -g -Werror")
ADD_EXECUTABLE( cbtest-boost circbuffer_boost.cpp )
TARGET_LINK_LIBRARIES( cbtest-boost ${Boost_LIBRARIES} )

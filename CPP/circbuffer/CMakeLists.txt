cmake_minimum_required (VERSION 2.8)
project (CircularBufferLib)
add_executable(cbtest circbuffer_test.cpp)
add_library(circbuffer circbuffer_test.cpp)

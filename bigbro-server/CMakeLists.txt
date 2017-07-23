cmake_minimum_required(VERSION 3.8)
project(bigbro_server)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        client.cc
        client.h
        common.h
        logger.cc
        logger.h
        main.cc
        main.h
        server.cc
        server.h)

find_package (Threads)

add_executable(bigbro_server ${SOURCE_FILES})
target_link_libraries( bigbro_server ${CMAKE_THREAD_LIBS_INIT} )
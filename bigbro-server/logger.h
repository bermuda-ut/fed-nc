/*=============================================================================
#     FileName: logger.h
#         Desc:  
#       Author: Max Lee
#        Email: hoso1312@gmail.com
#     HomePage: mallocsizeof.me
#      Version: 0.0.1
#   LastChange: 2017-07-16 18:21:15
=============================================================================*/
#pragma once

#include <iostream>
#include <string>

#define GLOBAL_LOG_LEVEL 0

enum LogLevel {
    debug = 0,
    info = 1,
    error = 2
};

class LoggableClass {
private:
    std::string name;

protected:
    explicit LoggableClass(std::string);

    void log(LogLevel, std::string);

private:
    std::string logLevelToString(LogLevel);
};

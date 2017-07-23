/*=============================================================================
#     FileName: logger.cc
#         Desc: simple global logger
#       Author: Max Lee
#        Email: hoso1312@gmail.com
#     HomePage: mallocsizeof.me
#      Version: 0.0.1
#   LastChange: 2017-07-16 16:06:54
=============================================================================*/
#include "common.h"
#include "logger.h"

#include <iomanip>

using std::ostream;
using std::cerr;
using std::cout;
using std::endl;
using std::time;
using std::string;
using std::time_t;
using std::put_time;

LoggableClass::LoggableClass(string name) {
    this->name = name;
}

void LoggableClass::log(LogLevel level, string str) {
    time_t t = time(NULL);
    std::tm tm = *std::localtime(&t);;

    if (level >= GLOBAL_LOG_LEVEL)
        ((level == error) ? cerr : cout) <<
                                         "[" << put_time(&tm, "%c") << "] " <<
                                         " " << logLevelToString(level) << "  " <<
                                         name << ": " << str << "\n";
}

string LoggableClass::logLevelToString(LogLevel level) {
    if (level == 0) return "DEBUG";
    if (level == 1) return "INFO ";
    if (level == 2) return "ERROR";
    return "LOGGER";
}

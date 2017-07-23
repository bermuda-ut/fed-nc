/*=============================================================================
#     FileName: client.cc
#         Desc:  
#       Author: Max Lee
#        Email: hoso1312@gmail.com
#     HomePage: mallocsizeof.me
#      Version: 0.0.1
#   LastChange: 2017-07-09 18:44:02
#      History:
=============================================================================*/
#include "client.h"

Client::Client(int sockfd) : LoggableClass("Client" + std::to_string(sockfd)) {
    log(info, "connected");
}

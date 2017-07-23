/*=============================================================================
#     FileName: server.h
#         Desc: server definitions
#       Author: Max Lee
#        Email: hoso1312@gmail.com
#     HomePage: mallocsizeof.me
#      Version: 0.0.1
#   LastChange: 2017-07-09 19:18:45
#      History:
=============================================================================*/
#pragma once

#include "client.h"
#include <vector>

// server stuff
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

using std::vector;

class Server {
    vector<Client> clients;

    public:
    int some_shit;
};


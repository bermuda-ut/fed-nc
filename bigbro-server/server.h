/*=============================================================================
#     FileName: server.h
#         Desc: server definitions
#       Author: Max Lee
#        Email: hoso1312@gmail.com
#     HomePage: mallocsizeof.me
#      Version: 0.0.1
#   LastChange: 2017-07-16 18:18:20
=============================================================================*/
#pragma once

#include "client.h"
#include "logger.h"
#include <vector>
#include <thread>

// server stuff
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <map>

#define REQUEST_QUEUE_LEN 10

typedef struct sockaddr_in SockAddr;

using std::vector;

class Server : public LoggableClass {
private:
    std::map<int, Client*> clientsMap;

    int sockfd, portNumber;

    SockAddr serverAddr;
    std::thread connector;

    void acceptConnections();

public:
    explicit Server(int portNumber);

    ~Server();
};


/*=============================================================================
#     FileName: server.cc
#         Desc:  
#       Author: Max Lee
#        Email: hoso1312@gmail.com
#     HomePage: mallocsizeof.me
#      Version: 0.0.1
#   LastChange: 2017-07-16 18:18:19
=============================================================================*/
#include "common.h"
#include "server.h"
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

Server::Server(int portNumber) : LoggableClass("Server") {
    log(debug, "Creating a socket");
    this->sockfd = socket(AF_INET, SOCK_STREAM, 0);

    if (sockfd < 0) {
        log(error, "Failed to create a socket");
        throw std::runtime_error("Failed to initialize socket");
    }

    // make the socket
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(portNumber);
    serverAddr.sin_addr.s_addr = INADDR_ANY;

    log(debug, "Binding the socket");
    // bind the socket
    int yes = 1;
    while (setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof(yes)) == -1) {
        log(error, "Failed to set socket option, retrying in 1 second..");
        sleep(1);
    } 

    while (bind(sockfd, (struct sockaddr*) &serverAddr, sizeof(serverAddr)) < 0) {
        log(error, "Error on binding, retrying in 1 second..");
        sleep(1);
    }

    log(info, "Successfully Instantiated");
}


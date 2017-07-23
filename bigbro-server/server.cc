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
#include <memory>

using std::shared_ptr;
using std::make_shared;
using std::thread;

Server::Server(int portNumber) : LoggableClass("Server") {
    log(debug, "Creating a socket");

    this->portNumber = portNumber;
    this->sockfd = socket(AF_INET, SOCK_STREAM, 0);
    while (sockfd < 0) {
        log(error, "Failed to create a socket");
        throw std::runtime_error("Failed to initialize socket");
    }

    // make the socket
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(portNumber);
    serverAddr.sin_addr.s_addr = INADDR_ANY;

    log(debug, "Set socket options");
    int yes = 1;
    while (setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof(yes)) == -1) {
        log(error, "Failed to set socket option, retrying in 1 second..");
        sleep(1);
    }

    log(debug, "Binding the socket");
    while (bind(sockfd, (struct sockaddr *) &serverAddr, sizeof(serverAddr)) < 0) {
        log(error, "Error on binding, retrying in 1 second..");
        sleep(1);
    }

    // listen
    log(debug, "Listening on socket");
    while (listen(sockfd, REQUEST_QUEUE_LEN) < 0) {
        log(error, "Error on listen, retrying in 1 second..");
        sleep(1);
    }

    connector = thread([=] { acceptConnections(); });
    log(info, "Successfully Instantiated with queue size " + std::to_string(REQUEST_QUEUE_LEN) + " port " +
              std::to_string(this->portNumber));
}

void Server::acceptConnections() {
    log(info, "Accepting client connection requests");

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wmissing-noreturn"
    while (true) {

        shared_ptr<sockaddr_in> cli_addr = make_shared<sockaddr_in>();
        socklen_t clilen = sizeof(cli_addr);

        int newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);

        this->clientsMap[newsockfd] = new Client(newsockfd);
    }
#pragma clang diagnostic pop
}

Server::~Server() {
    connector.join();
}

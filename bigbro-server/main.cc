/*=============================================================================
#     FileName: main.cc
#         Desc: driver for the server
#       Author: Max Lee
#        Email: hoso1312@gmail.com
#     HomePage: mallocsizeof.me
#      Version: 0.0.1
#   LastChange: 2017-07-09 18:23:49
=============================================================================*/
#include "main.h"
#include "server.h"

int main(int argc, char **argv) {
    (void) argv;
    (void) argc;
    Server server(4242);
}


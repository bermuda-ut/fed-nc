#pragma once

#include "client.h"
#include <vector>
using std::vector;

class Server {
    vector<Client> clients;
    public:
    int setup;
};


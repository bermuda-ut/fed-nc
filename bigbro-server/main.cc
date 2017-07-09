#include <iostream>
#include <vector>

using std::vector;
using std::cout;
using std::endl;
//using namespace std;

class Client {

};

class Server {
    vector<Client> clients;
    public:
    int setup;
};


int main(int argc, char **argv) {
    cout << "hello world" << endl;
}


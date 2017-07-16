"""
federated learning internet protocol
 
       __ _ _       
      / _| (_)      
     | |_| |_ _ __  
     |  _| | | '_ \ 
     | | | | | |_) |
     |_| |_|_| .__/ 
             | |    
             |_|    

python implementation
matt farrugia
"""

import socket

HOST="localhost"
PORT=4242

class model:
    def __init__(self, weights):
        self.n  = len(weights)
        self.ws = weights[:]
    def __str__(self):
        return "{} {}".format(self.n, " ".join(self.ws))

class flip:
    def __init__(self):
        self.socket = None
    def connect(self, host=HOST, port=PORT):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
    def disconnect(self):
        self.socket.close()
        self.socket = None

    # send messages
    def send_model(self, model):
        self._sendmsg("MODEL {}\n".format(model))

    def send_check(self):
        self._sendmsg("CHECK\n")

    def _sendmsg(self, message):
        msgbytes = message.encode('ascii')
        self.socket.send(msgbytes)

    # recv messages
    def recv_check(self):
        message = self._recvmsg()
        if message[:5] == "CHECK":
            return True
        else:
            return None

    def recv_model(self):
        message = self._recvmsg()
        if message[:5] == "MODEL":
            args = message.rstrip().split()
            n  = int(args[1])
            ws = list(map(float, args[2:]))
            assert(n == len(ws))
            return model(ws)
        else:
            return None

    def _recvmsg(self):
        msg = ""
        while msg[-1:] != "\n":
            msg += self._recv(1)
        return msg

    def _recv(self, nbytes):
        bs = self.socket.recv(nbytes)
        if bs:
            return bs.decode('ascii')
        else:
            raise Exception("socket disconnected")


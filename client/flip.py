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
    """
    a simple machine learning model to be sent between the client and server.
    at the moment, such a model consists only of a collection of weights
    """
    def __init__(self, weights):
        """create a new model to store a list of feature weights 'weights'"""
        self.n  = len(weights)
        self.ws = weights[:]

    def __str__(self):
        """
        a string representation of this model, for sending over a network:
        the string is formed first by the number of elements in the list of
        weights, then a space, then the string representation of the elements
        themselves

        >>> str(model([1.0, 2.0, 3.14]))
        "3 1.0 2.0 3.14"
        >>> str(model([]))
        "0 "
        >>> str(model([1, 2, 3, 4, 5, 6]))
        "6 1 2 3 4 5 6"
        """
        return "{} {}".format(self.n, " ".join(self.ws))


class flip:
    """
    flip.flip
    wrap a connection to a federated learning server or client, providing a 
    simple interface for sending the two protocol messages:
        MODEL - to send a model over the network
        CHECK - to request an updated model to be sent
    """
    def __init__(self, socket=None):
        """
        create a new connection object, optionally with an existing open TCP
        socket 'socket'
        if no socket is provided, the connection will start in a disconnected
        state
        """
        self.socket = socket

    def connect(self, host=HOST, port=PORT):
        """establish a connection to a specified (host, port)"""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def disconnect(self):
        """end a connection and return this socket to a disconnected state"""
        self.socket.close()
        self.socket = None


    ## send messages

    def send_model(self, model):
        """send a MODEL message containing model 'model' over the network"""
        self._sendmsg("MODEL {}\n".format(model))

    def send_check(self):
        """send a CHECK message over the network"""
        self._sendmsg("CHECK\n")

    def _sendmsg(self, message):
        """encode and send a string over the network"""
        msgbytes = message.encode('ascii')
        self.socket.send(msgbytes)


    ## recv messages

    def recv_check(self):
        """
        attempt to receive a CHECK message over the network
        returns True if the next message is a CHECK message; None otherwise
        """
        message = self._recvmsg()
        if message[:5] == "CHECK":
            return True
        else:
            return None

    def recv_model(self):
        """
        attempt to receive a MODEL message over the network
        returns the model contained in the message if the next message is a 
        MODEL message; None otherwise
        """
        message = self._recvmsg()
        if message[:5] == "MODEL":
            # the model message is of the format: "HEADER N W1 W2 ... WN\n"
            # where N is the number of weighs and W1 W2 ... WN are the weights
            terms = message.rstrip().split()
            n  = int(terms[1])
            ws = list(map(float, terms[2:]))
            assert(n == len(ws))
            return model(ws)
        else:
            return None

    def _recvmsg(self):
        """
        receive a complete message over the network (a string delimited by '\n')
        note: susceptible to memory overflow related attacks, where no \n is
        ever sent.
        """

        # receive characters until the message ends (with "\n")
        msg = ""
        while msg[-1:] != "\n":
            msg += self._recv(1)
        return msg

    def _recv(self, nbytes):
        """receive a single byte over the network, encoded as ascii"""
        bs = self.socket.recv(nbytes)
        if bs:
            return bs.decode('ascii')
        else:
            raise Exception("socket disconnected")

from time import *
import socketserver, socket
from typing import ValuesView
from TSSM import *
from LTE.LTE_conecting import *
from SCZ_service import *
print(y)

# Server || Hostname || Port

host = socket.gethostbyname(socket.gethostname())
port = 8888

class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """
    ThreadingMixIn and TCPServer
    """
    pass


class SCZ_server(socketserver.BaseRequestHandler):

    def Client(addr):
        """
        docstring
        """
        
        client=[]
        addr = socket.AddressFamily(vars)
        if addr not in client:
            client.append(addr)
        
        return addr
    Client(addr='i')
    
    def handle(self):
        """
        Get Data
        """
        data = self.request.recv(33554432).strip()
        if False:
            for i in range(1, 0, -1):
                print(i)
                sleep(1)
            LTE_encryption(LTE_input_data = data)
            #     
        print("Connection from client: {}".format(self.client_address[0]))
        print("Connection Time: {}".format(ctime()))
        print("Data: {}".format(data.decode()))
        
        self.request.sendall(data)
              
if __name__ == "__main__":
    with socketserver.TCPServer((host, port), SCZ_server) as server:
        print("Starting Server: ON")
        server.serve_forever()
        
    #server
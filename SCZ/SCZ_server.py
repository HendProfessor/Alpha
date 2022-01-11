from time import *
import socketserver
from TSSM import *
from .LTE.LTE_conecting import *
from .SCZ_service import *
print(y)

# Server 


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """
    ThreadingMixIn and TCPServer
    """
    pass

class SCZ_server(socketserver.BaseRequestHandler):

        #
    def LTE_starting(self):
        """
        LTE Starting
        """
        

    def handle(self):
        """
        Get Data
        """   
        data = self.request.recv(33554432).strip()
        for i in range(10, 0, -1):
            print(i)
            sleep(1)
        LTE_encryption(LTE_input_data = data)
        #     
        print("Connection from client: {}".format(self.client_address[0]))
        print("Connection Time: {}".format(ctime()))
        print("Data: {}".format(data.decode()))
        
        self.request.sendall(data)
              
    
        

if __name__ == "__main__":
    with socketserver.TCPServer(('', 8888), SCZ_server) as server:
        print("Starting Server")
        server.serve_forever()
        
        
    #server
from re import T
import socket
import socketserver
import ipaddress
import time

class connect_server(socketserver.TCPServer):
    """Connect to server"""
    def handle(self):
        hostadress = self.client_address[0]
        print(hostadress)
        self.request.sendall(hostadress)
        return hostadress
def send_data():
    """
    Send Data
    """
    entrance = input("Do you have serer IP address? Yes = y or No = n. (This is not the default value): ")
    if entrance == "y":
        host = input("Enter your server IP address: ")     
        print("Connecting to server in network")
    else:
        print("Connecting to server in localhost")
        localhost = socket.gethostbyname_ex(socket.gethostname())
        host = localhost[-1][-1]
    port = 8888
    print(host,port)
    while True:
        try:
        #    Connect server  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            print("Time: ",time.ctime())
            send_data = input("Send Data: ") 
            sock.send(send_data.encode())
            
    #    except:       

        except KeyboardInterrupt:
            print("Connecting to server Error")
            socket.close()
            break




import socket
import ipaddress
import time


def send_data():
    """
    Send Data
    """
    print("Connect client on")

    while True:
        try:
        #    Connect server  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((socket.gethostname(), 8888))
            print("Time: ",time.ctime())
            send_data = input("Send Data: ") 
            sock.send(send_data.encode())
            
    #    except:       

        except KeyboardInterrupt:
            socket.close()
            break


send_data()
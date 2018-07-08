import socket
import random
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

print( "UDP target IP:", UDP_IP)
print( "UDP target port:", UDP_PORT)
print( "message:", MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
#while True:
#x = random.randint(200,400)
#y =random.randint(200,400)
#message = str(x) + "," + str(y)
while True:
    x = random.randint(200,400)
    y =random.randint(200,400)
    message = str(x) + ',' + str(y)
    sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
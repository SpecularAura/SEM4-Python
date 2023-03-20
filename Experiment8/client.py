# TCP Client
# ==========
import socket
# Creating a TCP/ IP socket
clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connecting the socket to the server's port
serveraddress = ("localhost", 12345)
print("Connecting to the port %s port %s of server" % serveraddress)
clientsock.connect(serveraddress)
try:
        # Sending data
    senddata = ("This is Socket Programming in Python.")
    print("Sending the message.... %s" % senddata)
    clientsock.sendall(senddata.encode('utf-8'))
    # Receiving data
    recvdata = clientsock.recv(1024)
    print("Received data : %s" % recvdata.decode())
finally:
        # Closing the connection
    print("Closing the socket!!")
    clientsock.close()

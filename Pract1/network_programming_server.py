#import socket module

import socket

# create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket has been created")

#declare a host
host=""

#specify a connection port
port = 9090

#bind host and port to socket
s.bind((host,port))

#put the socket in a listening mode
s.listen(10)

print("server is listening at port:", port)

while True:
    #continue accepting connection from clients
    client_connection, client_addr=s.accept()

    print("Server Recieved connection from",client_addr)
    client_connection.send("thanks for connecting".encode())

    client_connection.close()
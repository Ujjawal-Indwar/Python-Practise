#import the socket module
import socket

#create a socket object
my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#specify the server port to connect to
port = 9090

#connect to the server 
my_socket.connect(('127.0.0.1', port))

#print the recieved message from server

print(my_socket.recv(1024).decode())

#close the server connection
my_socket.close()
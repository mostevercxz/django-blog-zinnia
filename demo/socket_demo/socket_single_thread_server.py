# coding:utf-8
# web address : http://pymotw.com/2/socket/tcp.html

from __future__ import print_function
import socket
import sys

def warning(*objs):
    print("warning: ", *objs, file=sys.stderr)

# create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a port
bind_address = ('localhost', 10000)
sock.bind(bind_address)

# Listening for incoming connections
sock.listen(1)
while True:
    warning("waiting for a connection")
    connection, client_address = sock.accept()
    try:
        warning("connection from " + client_address)

        #receive the data and return the data
        while True:
            data = connection.recv(16)
            warning("received: " + data)
            if data:
                warning("send data back to client")
                connection.sendall(data)
            else:
                warning("no more data anymore")
                break
    finally:
        connection.close()

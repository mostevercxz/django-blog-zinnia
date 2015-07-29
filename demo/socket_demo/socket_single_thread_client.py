#coding:utf-8

import sys
import socket

from common_func import warning

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
server_address=('localhost', 10000)
sock.connect(server_address)
warning("connect to server localhost at 10000")

try:
    message='this is all the content I want to send to the server'
    sock.sendall(bytes(message, "utf-8"))
    warning("send to server : " + message)

    # wait thte response
    received_size = 0
    expected_size = len(message)
    while received_size < expected_size:
        data = sock.recv(16)
        received_size += len(data)
        warning("received " + data.decode('utf-8'))
finally:
    warning("close the socket")
    sock.close()

"""
Rock Paper Scissors Client
"""

import socket

HOST = '127.0.0.1'
PORT = 12353

print("waiting for a connection with the server...")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    resp = s.recv(1024)
    while True:
        msg = input('My move is...')
        s.send(str.encode(msg))
        resp = s.recv(1024)
        print(resp.decode('utf-8'))
        
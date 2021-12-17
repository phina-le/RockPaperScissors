"""
Rock Paper Scissors Server
"""
import socket
import random

HOST = '127.0.0.1'
PORT = 12353
l = ['R', 'P', 'S']

"""
Game Logic
"""
def game(server_move, client_move):
    '''Takes in a server and client move and returns the result'''
    msg = ""
    if server_move == 'R' and client_move == 'S':
        msg = "Server Wins"
    elif server_move == 'S' and client_move == 'P':
        msg = "Server Wins"
    elif server_move == 'P' and client_move == 'R':
        msg = "Server Wins"
    elif server_move == 'S' and client_move == 'R':
        msg = "You win!"
    elif server_move == 'P' and client_move == 'S':
        msg = "You win!"
    elif server_move == 'R' and client_move == 'P':
        msg = "You win!"
    elif server_move == 'R'and client_move == 'R':
        msg = "It's a tie!"
    elif server_move == 'P'and client_move == 'P':
        msg = "It's a tie!"
    elif server_move == 'S'and client_move == 'S':
        msg = "It's a tie!"
    else:
        return "Invalid input"
    return "Server chose " + server_move + ". " + msg

#Server Communication
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        conn.send(str.encode('Type "R", "P", or "S" to play with me. Type nothing to end it.'))
        while True:
            resp = conn.recv(1024)
            sMsg = game(random.choice(l), resp.decode('utf-8')) #Server move is randomized
            conn.send(sMsg.encode())
            if not resp:
                break

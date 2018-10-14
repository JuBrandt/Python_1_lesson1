import socket
import json


ADDRESS = "localhost"
PORT = 7777

def get_server_socket():
    s = socket.socket()
    s.bind((ADDRESS, PORT))
    s.listen(10)
    data = json.loads(client.recv(1024).decode("utf-8"))
    print(data)
    return s

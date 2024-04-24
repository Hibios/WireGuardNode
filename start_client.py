import socket
import threading

def connect_to_node(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print(f"Connected to {host}:{port}")
    client.send("ping".encode('utf-8'))
    print(f"Received message: {client.recv(1024).decode('utf-8')}")

connect_to_node('10.0.0.3', 55555)

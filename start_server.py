import socket
import threading

class Node:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(1)
        print(f"Server started at {self.host}:{self.port}")

        while True:
            client, address = server.accept()
            print(f"Connection established with {address}")
            threading.Thread(target=self.handle_client, args=(client,)).start()

    def handle_client(self, client):
        while True:
            message = client.recv(1024).decode('utf-8')
            if message == "ping":
                print("Received ping. Sending pong.")
                client.send("pong".encode('utf-8'))

node = Node('10.0.0.3', 55555)
threading.Thread(target=node.start_server).start()

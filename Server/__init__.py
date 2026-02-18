import threading
import socket

clients = []

def add_client(conn):
    clients.append(conn)
    print("Client added")

HOST = "127.0.0.1"
PORT = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server started")

def handle_client():
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=add_client, args=(conn,)).start()

threading.Thread(target=handle_client).start()

while True:
    message = input("Enter message: ")

    for client in clients:
        try:
            client.send(message.encode())
        except:
            print("There's no clients")

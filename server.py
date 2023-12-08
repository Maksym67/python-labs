import socket
import threading

clients = []
log_file = "server_log.txt"

def show_message(message, sender):
    log_message(message)
    for client in clients:
        try:
            if client != sender:
                client.send(message.encode())
        except:
            clients.remove(client)

def log_message(message):
    with open(log_file, 'a') as file:
        file.write(message + '\n')

def client_thread(conn, addr):
    print(f"Connected by {addr}")
    name = conn.recv(1024).decode()

    while True:
        try:
            message = conn.recv(1024).decode()
            if not message:
                break
            print(f"Received from {name}: {message}")
            show_message(f"{name}: {message}", conn)
        except:
            break
    conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen()
    print('Server started')

    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=client_thread, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()

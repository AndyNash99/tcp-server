import socket
import threading

HEADER = 64
PORT = 5000
IP = socket.gethostbyname(socket.gethostname())
ADDRESS = (IP, PORT)
DISCONNECT_MESSAGE = "DESCONEXION"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)


def handle_client(conn, addr):
    print("New connection: " + addr + "connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode("utf-8")
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode("utf-8")
        if msg == DISCONNECT_MESSAGE:
            connected = False
        print(f"[{addr}] {msg}")

    conn.close()


def start():
    server.listen()
    print(f"Listening on {IP}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("Active connections: " + str(threading.activeCount() - 1))


print("Starting server...")
start()


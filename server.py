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
    print("New connection: " + str(addr) + " connected.")
    while True:
        msg_length = conn.recv(HEADER).decode("utf-8")
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode("utf-8")
            if msg == DISCONNECT_MESSAGE:
                break

            print(f"[{addr}] {msg}")
            message = msg.upper().encode("utf-8")
            msg_length = len(message)
            send_length = str(msg_length).encode("utf-8")
            send_length += b" " * (HEADER -len(send_length))
            conn.send(send_length)
            conn.send(message)

    conn.close()


def start():
    server.listen()
    print(f"Listening on {IP}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("Active connections: " + str(threading.active_count() - 1))


print("Starting server...")
start()


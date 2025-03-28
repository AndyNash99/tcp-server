import socket

HEADER = 64
PORT = 5000
IP = socket.gethostbyname(socket.gethostname())
ADDRESS = (IP, PORT)
DISCONNECT_MESSAGE = "DESCONEXION"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)


def send(msg):
    message = msg.encode("utf-8")
    msg_length = len(message)
    send_length = str(msg_length).encode("utf-8")
    send_length += b" " * (HEADER -len(send_length))
    client.send(send_length)
    client.send(message)
    msg_length = client.recv(HEADER).decode("utf-8")
    if msg_length:
        msg_length = int(msg_length)
        msg = client.recv(msg_length).decode("utf-8")
        print(msg)


while True:
    msg = input("Envía un mensaje: ")
    if msg:
        send(msg)

    if msg == DISCONNECT_MESSAGE:
        break

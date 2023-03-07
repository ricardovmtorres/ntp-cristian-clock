import socket
import threading
import time

IP = socket.gethostbyname(socket.gethostname())
PORT = 3333
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} se conectou.")

    connected = True
    while connected:
        data_client = conn.recv(SIZE).decode(FORMAT)
        if data_client == DISCONNECT_MSG:
            connected = False

        print(f"[{addr}] {data_client}")
        data_client = f"Data from client: {data_client}"

        data_atual = time.time()
        print(data_atual)

        conn.send(str(data_atual).encode(FORMAT))

    conn.close()

def main():
    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

if __name__ == "__main__":
    main()
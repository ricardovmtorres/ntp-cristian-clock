import socket
import threading
import time
import datetime

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
        
        data_chegada = time.time()
        print(data_chegada)

        if data_client == DISCONNECT_MSG:
            connected = False

        # Converte o timestamp em um objeto datetime e imprime
        dt_object = datetime.datetime.fromtimestamp(float(data_client))
        print("Hora e data do cliente:", dt_object.strftime("%m/%d/%Y %H:%M:%S"))

        print(f"[{addr}] {data_client}")
        data_client = f"Data from client: {data_client}"

        data_saida = time.time()
        print(data_saida)
        resposta = str(data_chegada)+";"+str(data_saida)
        conn.send(resposta.encode(FORMAT))

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
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    main()
import socket
import time
import datetime
import subprocess
import win32api

IP = socket.gethostbyname(socket.gethostname())
PORT = 3333
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")

    connected = True
    while connected:
        #msg = input("> ")
        #msg += ":"+ str(PORT)

        data_inicio = time.time()
        print(data_inicio)
        
        client.send(str(data_inicio).encode(FORMAT))

        if data_inicio == DISCONNECT_MSG:
            connected = False
        else:
            data_retorno = float(client.recv(SIZE).decode(FORMAT))
            print(f"[SERVER] {data_retorno}")
        
        # algoritimo de cristian
        horas = cristian(data_inicio, data_retorno)
        # atualizar hora
        atualiza_hora(horas)
        # esperar 30 segundos para recomeçar
        time.sleep(10)


def cristian(data_inicio, data_retorno):
    t3 = time.time()
    t4 = time.time()
    
    # Calcula o tempo de viagem médio e ajusta o relógio local
    tempo_medio = ((t4 - data_inicio) - (t3 - data_retorno)) / 2
    horario = data_retorno + tempo_medio
    
    return horario


def atualiza_hora(horas):
    # cria um objeto datetime a partir de um número float
    dt = datetime.datetime.fromtimestamp(horas)
    # extrai a parte do tempo do objeto datetime
    time_obj = dt.time()
    print(time_obj)

    # Cria um objeto datetime com a data atual e o horário definido pelo objeto time
    datetime_obj = datetime.datetime.combine(datetime.date.today(), time_obj)
    print(datetime_obj)

    # linux
    # Define o comando para mudar a hora do sistema e executa
    # cmd = ['sudo', 'date', '-u', datetime_obj.strftime('%m%d%H%M%Y.%S')]
    # subprocess.call(cmd)

    # windowns
    win32api.SetSystemTime(datetime_obj.year, datetime_obj.month, 0, datetime_obj.day, datetime_obj.hour, datetime_obj.minute, datetime_obj.second, 0)

if __name__ == "__main__":
    main()
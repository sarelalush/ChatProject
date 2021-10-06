import socket
import select
from protocol import SERVER_ADDRES, protocol_read_message , protocol_write_message 
def main():
    server = socket.socket()
    server.bind(SERVER_ADDRES)
    server.listen(5)

    clients = [server]

    while True:
        readables , _ , _ = select.select(clients , [] , [] , 0.1)
        for readable in readables:
            if readable == server:
                conn,addr = server.accept()
                clients.append(conn)
                print(f'new Client : {addr}')
            else:
                message = protocol_read_message(readable)
                if message in [b'',b'exit']:
                    readable.shutdown(socket.SHUT_RDWR)
                    readable.close()
                    clients.remove(readable)
                for client in clients:
                    if client != readable and client != server:
                        protocol_write_message(client,message)
    server.shutdown(socket.SHUT_RDWR)
    server.close()


if __name__ == "__main__":
    main()


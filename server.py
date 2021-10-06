import socket

from protocol import SERVER_ADDRES, protocol_read_message , protocol_write_message 
def main():
    server = socket.socket()
    server.bind(SERVER_ADDRES)
    server.listen(5)

    clients = []

    while True:
        conn , addr = server.accept()
        print(f'new Client : {addr}')
        message = protocol_read_message(conn)
        for client in clients:
            if client != conn:
                protocol_write_message(client,message)
    server.shutdown(socket.SHUT_RDWR)
    server.close()


if __name__ == "__main__":
    main()
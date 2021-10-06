import socket
import select
from protocol import SERVER_ADDRES , protocol_read_message , protocol_write_message
import sys

def main():
    client = socket.socket()
    client.connect(SERVER_ADDRES)
    to_read = [client , sys.stdin]
    finished = False
    while not finished:
        readables , _ , _ = select.select(to_read , [] , [] , 0.1)
        for readable in readables:
            if readable == client:
                from_server = protocol_read_message(readable)
                print(f'{from_server}')
            else:
                message = readable.readline().strip().encode()
                protocol_write_message(readable,message)
                if message == b'exit':
                    finished = True
    client.shutdown(socket.SHUT_RDWR)
    client.close()
if __name__ == "__main__":
    main()
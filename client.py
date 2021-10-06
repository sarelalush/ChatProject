import socket
from protocol import SERVER_ADDRES , protocol_read_message , protocol_write_message

def main():
    client = socket.socket()
    client.connect(SERVER_ADDRES)

    finished = False
    while not finished:
        message = input("> ")
        protocol_write_message(client,message)
        from_server = protocol_read_message(client)
        print(f'Server Message : {from_server}')
        if message == b'exit':
            finished = True
    client.shutdown(socket.SHUT_RDWR)
if __name__ == "__main__":
    main()
import struct

MESSEGE_FORMAT = struct.Struct('!I')

SERVER_ADDRES = ('127.0.0.1',1337)

def protocol_write_message(sock , message):
    message_len = len(message)
    message = MESSEGE_FORMAT.pack(message_len) + message
    sock.sendall(message)
def protocol_read_message():
    meta = sock.recv(MESSEGE_FORMAT.size)
    message_len = MESSEGE_FORMAT.unpack(meta)[0]
    return sock.recv(message_len)
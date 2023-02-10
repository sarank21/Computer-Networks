import socket
import os

IPAddr = socket.gethostbyname(socket.gethostname())
Port = 5666
formt = 'utf-8'

while True:
    servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servsock.bind((IPAddr, Port))
    servsock.listen()
    conn, addr = servsock.accept()
    filename = conn.recv(1024)
    filename_dec = filename.decode(formt)
    #print("Filename received "+filename_dec)
    n1 = conn.recv(1024)
    n2 = n1.decode(formt)
    #print("N is "+n2)
    n = int(n2)
    filepath=filename_dec+".txt"
    if os.path.isfile(filepath):
        fd = open(filepath, 'r')
    else:
        conn.send("SORRY!".encode(formt))
        continue
    fd.seek(0, os.SEEK_END)
    sz = fd.tell()
    fd.seek((sz-n), 0)
    data = fd.read()
    conn.send(data.encode(formt))
    conn.close()
    fd.close()
servsock.close()
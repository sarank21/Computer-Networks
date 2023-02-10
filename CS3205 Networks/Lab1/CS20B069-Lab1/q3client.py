import socket

IPAddr = socket.gethostbyname(socket.gethostname())
Port = 5666
formt = 'utf-8'

clisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
clisock.connect((IPAddr, Port))
filename = input("Enter filename: ")
clisock.send(filename.encode(formt))
n = input("Enter value of n: ")
clisock.send(n.encode(formt))
data = clisock.recv(1024).decode(formt)
#print("Data received: "+data)
if(data=="SORRY!"):
    print("Server says file does not exist")
else:
    f = open(filename+"1.txt", 'w')
    f.write(data)
    f.close()
clisock.close()
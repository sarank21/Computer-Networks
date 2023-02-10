import socket
import math

host_addr=socket.gethostbyname(socket.gethostname())
sersock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sersock.bind((host_addr, 7654))

while True:
    instr, client_addr = sersock.recvfrom(7654)
    data=instr.decode('utf-8')
    #print("Data is "+data)
    d = data.split()  
    op = d[0]
    var1 = d[1]
    var2  = d[2]
    if op=="add":
        msg=str(int(var1)+int(var2))
    elif op=="mul":
        msg=str(int(var1)*int(var2))
    elif op=="mod":
        msg=str(int(var1)%int(var2))
    elif op=="hyp":
        k1 = int(var1)
        k2 = int(var2)
        k3 = math.sqrt(k1*k1 + k2*k2)
        msg=str(k3)
    msg_enc=msg.encode('utf-8')
    sersock.sendto(msg_enc, client_addr)

sersock.close()
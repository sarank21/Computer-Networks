import socket

client=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host_addr=socket.gethostbyname(socket.gethostname())

while True:
    inp_msg = input()
    if(inp_msg=="end client"):
        break
    client.sendto(inp_msg.encode("utf-8"), (host_addr, 8765))
    serv_message, serv_addr=client.recvfrom(8765)
    data=serv_message.decode('utf-8')
    print("Server says: "+data)
client.close()
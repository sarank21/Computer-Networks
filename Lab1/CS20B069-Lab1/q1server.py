import socket

host_addr = socket.gethostbyname(socket.gethostname())
sersock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sersock.bind((host_addr, 5050))

while True:
    client_message, client_addr = sersock.recvfrom(5050)
    data=client_message.decode('utf-8')
    #print(f"Message received is {data}")
    sersock.sendto(client_message, client_addr)

sersock.close()
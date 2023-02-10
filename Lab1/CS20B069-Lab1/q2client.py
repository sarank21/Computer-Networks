import socket

client=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host_addr=socket.gethostbyname(socket.gethostname())

while True:
    msg = input()
    print(msg)
    if msg=="exit":
        print("[Exiting]")
        exit(0)
    client.sendto(msg.encode("utf-8"), (host_addr, 7654))
    server_message, server_addr=client.recvfrom(7654)
    data=server_message.decode('utf-8')
    print("Server message: "+data)

client.close()
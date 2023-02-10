#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>

#include <netinet/in.h>
#include <arpa/inet.h>

#include <netdb.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char server_message[256] = "You have reached the server. Demo for Laasya over";

    int ser_sock;
    ser_sock = socket(AF_INET, SOCK_STREAM, 0);  //Zero is for some flag bit

    struct sockaddr_in ser_address;         //Structure specifying transport address and port for an AF
    ser_address.sin_family = AF_INET;
    ser_address.sin_port = htons(9002);     //function to convert this integer to the Network byte order
    ser_address.sin_addr.s_addr = INADDR_ANY;   //No specific IP. Thus, local IP is used

        printf("Client IP address: %s\n", inet_ntoa(ser_address.sin_addr));

    bind(ser_sock, (struct sockaddr *) &ser_address, sizeof(ser_address));

    listen(ser_sock, 5);

    int client_sock;
    client_sock = accept(ser_sock, NULL, NULL);     //2nd param - structure for address of client. 3rd param - sizeof client address

    send(client_sock, server_message, sizeof(server_message), 0);  //Zero is for some flag bit

    close(ser_sock);
}
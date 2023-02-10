#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>

#include <netinet/in.h>
#include <arpa/inet.h>

#include <netdb.h>
#include <string.h>
#include <stdlib.h>

int main() {
    int cl_sock;
    cl_sock=socket(AF_INET, SOCK_STREAM, 0);
    
    struct sockaddr_in cl_address;
    cl_address.sin_family = AF_INET;
    cl_address.sin_port = htons(9002);
    cl_address.sin_addr.s_addr = INADDR_ANY;

    printf("Client IP address: %s\n", inet_ntoa(cl_address.sin_addr));

    int connnection_status = connect(cl_sock, (struct sockaddr *) &cl_address, sizeof(cl_address));
    if(connnection_status==-1) {
        printf("Error in connecting socket to port\n");
        exit(0);
    }

    char server_response[256];
    recv(cl_sock, &server_response, sizeof(server_response), 0);

    printf("Message from server is %s\n", server_response);

    close(cl_sock);
    return 0;
}
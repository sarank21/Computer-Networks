#include <stdio.h>
#include <netdb.h>
#include <arpa/inet.h>

int main(int argc, char *argv[])
{
    struct hostent *lh = gethostbyname("localhost");
    struct in_addr **a;
    a = (struct in_addr **)lh->h_addr_list;
    if (lh)
    {
        for(int i=0 ; a[i]!=NULL ; i++)
        printf("%s", inet_ntoa(*a[i]));
    }
    else
        herror("gethostbyname");

    return 0;
}
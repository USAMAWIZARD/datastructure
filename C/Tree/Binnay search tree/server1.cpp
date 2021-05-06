#include <iostream>
#include <stdio.h>
#include <string>

//Network related includes:
#include <sys/socket.h>
#include <netdb.h>
#include <arpa/inet.h>

//Target host details:
#define PORT 1234
#define HOST "74.74.74.74"

using namespace std;

//Function prototypes:
string MessageFormat(int, char**);
void MessageSend(string);

int main(int argc, char *argv[])
{
    //Parse arguments and format message:
    string message = MessageFormat(argc, argv);

    //Send the message out: 
    MessageSend(message);

    return 0;
}

string MessageFormat(int argc, char *argv[])
{
    //Massage the command line parameters
    // into my desired payload format.

    return message;
}

void MessageSend(string message)
{
    int sd, ret;
    struct sockaddr_in server;
    struct in_addr ipv4addr;
    struct hostent *hp;

    sd = socket(AF_INET,SOCK_DGRAM,0);
    server.sin_family = AF_INET;

    inet_pton(AF_INET, HOST, &ipv4addr);
    hp = gethostbyaddr(&ipv4addr, sizeof ipv4addr, AF_INET);
    //hp = gethostbyname(HOST);

    bcopy(hp->h_addr, &(server.sin_addr.s_addr), hp->h_length);
    server.sin_port = htons(PORT);

    connect(sd, (const sockaddr *)&server, sizeof(server));
    send(sd, (char *)message.c_str(), strlen((char *)message.c_str()), 0);
}
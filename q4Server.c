//We will be coding TCP sockets here and not udp sockets

#include<stdio.h>
#include<stdlib.h>
#include<sys/socket.h>
#include<unistd.h>
#include<string.h>
#include<arpa/inet.h>
#include<netinet/in.h>
#define PORT 8000
#define BUFFER_SIZE 1024

void handle_client(int clientSocket){
    char buffer[BUFFER_SIZE];
    int bytes_read;
    while((bytes_read=read(clientSocket,buffer,sizeof(buffer)-1))>0){
        buffer[bytes_read]='\0';
        printf("Client says : %s\n",buffer);
        char *response="Message received";
        write(clientSocket,response,strlen(response));
    }
    close(clientSocket);
    printf("Client disconnected \n");
}

//socket(domain,type,protocol) - SOCK_STREAM for tcp sockets
int main(){
    int serverSocket;
    serverSocket=socket(AF_INET,SOCK_STREAM,0);
    if(serverSocket==-1){
        perror("Socket() failed to get created");
        return 1;
    }

    int status;
    struct sockaddr_in address;
    socklen_t addrlen=sizeof(address);
    address.sin_family=AF_INET;
    address.sin_addr.s_addr=INADDR_ANY;
    address.sin_port=htons(PORT);
    status=bind(serverSocket,(struct sockaddr *)&address,addrlen);
    if(status==-1){
        perror("Failed to bind the socket");
        
        return 1;
    }

    int listenStatus=listen(serverSocket,5); //Backlog is set to 5 here which means the queuelength

    if(listenStatus==-1){
        perror("Failed to activate the sockter");
        
        return 1;
    }

    int clientSocket;
    struct sockaddr_in clientAddress;
    int clientLength=sizeof(clientAddress);
    while(1){
        clientSocket=accept(serverSocket,(struct sockaddr *)&clientAddress,&clientLength);
        if(clientSocket<0){
            perror("Connection failed");
            continue;
        }
        printf("connection accepted from \n");
        if(fork()==0){
            close(serverSocket);
            handle_client(clientSocket);
            exit(0);
        }
        close(clientSocket);
    }
    close(serverSocket);
}
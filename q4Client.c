#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#define SERVER_IP "127.0.0.1"
#define PORT 8000
#define BUFFER_SIZE 1024

int main(){
    int sock;
    struct sockaddr_in server_addr;
    char buffer[BUFFER_SIZE];

    if((sock=socket(AF_INET,SOCK_STREAM,0))<0){
        perror("Socket creation failed");
        return 1;
    }
    server_addr.sin_family=AF_INET;
    server_addr.sin_port=htons(PORT);
    if(inet_pton(AF_INET,SERVER_IP,&server_addr.sin_addr)<=0){
        perror("Invalid address / not supported");
        return 1;
    }
    if(connect(sock,(struct sockaddr *)&server_addr,sizeof(server_addr))<0){
        perror("Connection failed\n");
        close(sock);
        return 1;

    }
    printf("Connected to server.\nEnter your messageds : \n");
    while(1){
        printf("You : ");
        fgets(buffer,BUFFER_SIZE,stdin);

        write(sock,buffer,strlen(buffer));
        int bytes=read(sock,buffer,BUFFER_SIZE-1);
        if(bytes<=0){
            break;
        }
        buffer[bytes]='\0';
        printf("Server : %s\n",buffer);
    }
    close(sock);
    return 0;
}
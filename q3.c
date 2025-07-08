#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/utsname.h>
//the uname function
//int uname(struct utsname *name);
//return a pointer to utsname where the function return -1 if impossible allocation
//else return 0 and store system info in the variable given as input
//info present are
//char *sysname
//char *nodename
//char *release
//char *version
//char *machine
int main(){
    struct utsname sysinfo;

    if(uname(&sysinfo)==-1){
        perror("uname");
        return 1;
    }

    printf("System name : %s\n",sysinfo.sysname);
    printf("Node name : %s\n",sysinfo.nodename);
    printf("Release : %s\n",sysinfo.release);
    printf("Version : %s\n",sysinfo.version);
    printf("Machine : %s\n",sysinfo.machine);
    return EXIT_SUCCESS;
}
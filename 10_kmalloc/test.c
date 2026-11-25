#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>

#define MEMSIZE 64

int main(){
    int fd;
    char *text;

    text = malloc(MEMSIZE);
    if (!text){
        perror("malloc");
        return EXIT_FAILURE;
    }

    fd = open("/dev/hello0", O_RDWR);
    if (fd < 0){
        perror("open");
        free(text);
        return EXIT_FAILURE;
    }

    sprintf(text, "Hello from user space!");
    write(fd, text, strlen(text));
    lseek(fd, 0, SEEK_SET);
    memset(text, 0, MEMSIZE);

    read(fd, text, MEMSIZE);
    printf("Read from device: %s\n", text);


    free(text);
    return 0;
}


#include <stdio.h>


int main(
        int argc,  /* argument count */
        char** argv  /* argument vector */
) {
    printf("number of arguments: %d\n", argc);

    for(int i = 0; i < argc; i++) {
        printf("got arg: %s\n", argv[i]);
    }

    return 0;
}

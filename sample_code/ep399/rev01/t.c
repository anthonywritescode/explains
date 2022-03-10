#include <stdio.h>
#include <uuid/uuid.h>


int main(void) {
    uuid_t uuid;
    uuid_generate_random(uuid);

    printf("got uuid: %s\n", uuid);
    return 0;
}

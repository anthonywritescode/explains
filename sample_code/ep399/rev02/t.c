#include <stdio.h>
#include <uuid/uuid.h>


int main(void) {
    uuid_t uuid;
    char uuid_s[UUID_STR_LEN];

    uuid_generate_random(uuid);
    uuid_unparse(uuid, uuid_s);

    printf("got uuid: %s\n", uuid_s);
    return 0;
}

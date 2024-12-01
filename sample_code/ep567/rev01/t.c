#include <gssapi.h>

int main(void) {
    for (int i = 0; i < 10; i += 1) {
        gss_cred_id_t cred = 0;
        OM_uint32 minor = 0;
        OM_uint32 ret = gss_acquire_cred(
            &minor, GSS_C_NO_NAME, 0, GSS_C_NO_OID_SET,
            GSS_C_INITIATE, &cred, NULL, NULL
        );
        if (ret == GSS_S_COMPLETE) {
            printf("no error\n");
            gss_release_cred(&minor, &cred)
        } else {
            printf("got error: %d\n", ret)
        }
    }
}

from cffi import FFI


CDEF = '''\
typedef unsigned char uuid_t[16];

void uuid_generate(uuid_t out);
'''

ffibuilder = FFI()
ffibuilder.cdef(CDEF)
ffibuilder.set_source(
    '_uuidcffi',
    '#include <uuid/uuid.h>',
    libraries=['uuid'],
)

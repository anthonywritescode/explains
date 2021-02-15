import uuid

import _uuidcffi


_ffi = _uuidcffi.ffi
_lib = _uuidcffi.lib


def generate_uuid() -> uuid.UUID:
    buf = _ffi.new('uuid_t')
    _lib.uuid_generate(buf)
    return uuid.UUID(bytes=bytes(buf))

from typing import Tuple
from typing import TypeVar


T = TypeVar('T')
Vector3 = Tuple[T, T, T]


def make_vec_3d_int(scalar: int) -> Vector3[int]:
    return (scalar, scalar, scalar)


reveal_type(make_vec_3d_int(2))


def make_vec_generic(scalar: T) -> Vector3[T]:
    return (scalar, scalar, scalar)


reveal_type(make_vec_generic(15.0))

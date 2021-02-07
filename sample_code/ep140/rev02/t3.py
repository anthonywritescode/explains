from types import TracebackType
from typing import Callable
from typing import ContextManager
from typing import Generator
from typing import Generic
from typing import Optional
from typing import Tuple
from typing import Type
from typing import TypeVar


TRet = TypeVar('TRet')


class _MyContextManager(Generic[TRet]):
    def __init__(self, gen: Generator[TRet, None, None]) -> None:
        self.gen = gen

    def __enter__(self) -> TRet:
        try:
            return next(self.gen)
        except StopIteration:
            raise RuntimeError('generator did not yield')

    def __exit__(
            self,
            tp: Optional[Type[BaseException]],
            inst: Optional[BaseException],
            tb: Optional[TracebackType],
    ) -> Optional[bool]:
        if tp is None:
            try:
                next(self.gen)
            except StopIteration:
                return None
            else:
                raise RuntimeError('generator did not stop')
        else:
            try:
                self.gen.throw(tp, inst, tb)
            except StopIteration as e:
                if inst is e:
                    return False
                else:
                    return True
            except BaseException as e:
                if inst is e:
                    return False
                else:
                    raise


def my_contextmanager(
    func: Callable[..., Generator[TRet, None, None]],
) -> Callable[..., ContextManager[TRet]]:
    def my_contextmanager_callable(*args, **kwargs) -> ContextManager[TRet]:
        return _MyContextManager(func(*args, **kwargs))
    return my_contextmanager_callable


class FooError(RuntimeError):
    pass


@my_contextmanager
def my_ctx() -> Generator[Tuple[int, int], None, None]:
    print('before')
    try:
        yield (42, 99)
        print('after')
    except FooError as inst:
        print(f'suppressing {inst=}')
        return True
    except BaseException as inst:
        print(f'not suppressing {inst=}')
        raise


ctx = my_ctx()
print('before ctx')
with ctx:
    print('boom')
    raise FooError('wat')

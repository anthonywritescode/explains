import functools
from collections.abc import Callable

from mypy.plugin import AttributeContext, Plugin
from mypy.types import Type


def _lazy_attribute(ctx: AttributeContext, *, attr: str) -> Type:
    breakpoint()
    ...


class MyPlugin(Plugin):
    def get_attribute_hook(
        self,
        fullname: str,
    ) -> Callable[[AttributeContext], Type] | None:
        # fullname: lazy.Lazy.foo
        if fullname.startswith('lazy.Lazy.'):
            _, _, attr = fullname.rpartition('.')
            return functools.partial(_lazy_attribute, attr=attr)
        else:
            return None


def plugin(version: str) -> type[MyPlugin]:
    return MyPlugin

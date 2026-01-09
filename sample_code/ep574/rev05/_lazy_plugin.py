import functools
from collections.abc import Callable

from mypy.plugin import AttributeContext, Plugin
from mypy.types import AnyType, Instance, Type


def _lazy_attribute(ctx: AttributeContext, *, attr: str) -> Type:
    if not isinstance(ctx.default_attr_type, AnyType):
        return ctx.default_attr_type

    assert isinstance(ctx.type, Instance), ctx.type
    assert len(ctx.type.args) == 1, ctx.type
    assert isinstance(ctx.type.args[0], Instance), ctx.type
    breakpoint()

    return ctx.default_attr_type


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

import warnings


def foo() -> None:
    warnings.warn("foo is deprecated", stacklevel=2)

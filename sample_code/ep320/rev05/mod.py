import warnings


def foo() -> None:
    warnings.warn("foo is deprecated", SyntaxWarning, stacklevel=2)

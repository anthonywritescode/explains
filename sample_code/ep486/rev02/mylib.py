import warnings


def old_func():
    warnings.warn(
        DeprecationWarning('use new_func instead'),
        stacklevel=2,
    )

    return 5

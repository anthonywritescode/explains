import warnings


def old_func():
    warnings.warn(DeprecationWarning('use new_func instead'))

    return 5

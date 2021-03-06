"""
Providing iterator functions that are not in all version of Python we support.
Where possible, we try to use the system-native version and only fall back to
these implementations if necessary.
"""

from django.utils.six.moves import builtins
import itertools
import warnings

def is_iterable(x):
    "A implementation independent way of checking for iterables"
    try:
        iter(x)
    except TypeError:
        return False
    else:
        return True

def product(*args, **kwds):
    warnings.warn("django.utils.itercompat.product is deprecated; use the native version instead",
                  DeprecationWarning, stacklevel=2)
    return itertools.product(*args, **kwds)

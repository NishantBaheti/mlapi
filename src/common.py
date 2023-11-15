"""
Common Module
--------------
"""
from typing import Any


def dummy(first_arg: Any, second_arg: Any) -> str:
    """Dummy Function

    Parameters
    ----------
    first_arg : Any
        first argument
    second_arg : Any
        second argument

    Returns
    -------
    str
        return value
    """
    return f"{first_arg}-{second_arg}"

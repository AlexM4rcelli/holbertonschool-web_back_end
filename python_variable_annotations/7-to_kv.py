#!/usr/bin/env python3
"""
    Module to a function
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple. The first element of the tuple is the string k.
    The second element is the square of the int/float v and should
    be annotated as a float.
    """
    return (k, v**2)

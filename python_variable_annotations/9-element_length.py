#!/usr/bin/env python3
"""
    Module to variable annotations
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    """
    return [(i, len(i)) for i in lst]

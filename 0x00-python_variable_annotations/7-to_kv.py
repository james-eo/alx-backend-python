#!/usr/bin/env python3
"""
This module contains a function that creates a tuple
from a string and a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Creates a tuple from a string and a number.

    Args:
        k (str): The string.
        v (Union[int, float]): The number.

    Returns:
        Tuple[str, float]: The tuple with the string and the
        square of the number.
    """
    return (k, float(v ** 2))

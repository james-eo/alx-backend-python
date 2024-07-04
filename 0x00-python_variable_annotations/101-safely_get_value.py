#!/usr/bin/env python3
"""
This module contains a function that safely
gets a value from a dictionary.
"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping[Any, Any],
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely gets a value from a dictionary.

    Args:
        dct (Mapping[Any, Any]): The dictionary.
        key (Any): The key to look up.
        default (Union[T, None], optional): The default value if
        the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value from the dictionary or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default

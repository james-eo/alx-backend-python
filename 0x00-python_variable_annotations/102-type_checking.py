#!/usr/bin/env python3
"""
This module contains a function that zooms in on an array.
"""

from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zooms in on an array by repeating its elements.

    Args:
        lst (Tuple[int, ...]): The tuple of integers.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        List[int]: The zoomed-in list of integers.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

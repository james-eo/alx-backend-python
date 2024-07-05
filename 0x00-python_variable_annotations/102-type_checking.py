#!/usr/bin/env python3
"""
This module contains a function that zooms in on an array.
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zooms in on an array by repeating its elements."""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

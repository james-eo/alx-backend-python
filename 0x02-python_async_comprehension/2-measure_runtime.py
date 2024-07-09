#!/usr/bin/env python3
"""Module that contains Coroutine for parallel comprehension"""
import asyncio
from typing import List
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    using asyncio.gather, measures the total runtime, and returns it.


    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time

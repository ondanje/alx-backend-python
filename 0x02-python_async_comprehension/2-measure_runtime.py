#!/usr/bin/env python3
"""
importing asyncio for asynchorous programming and time module for
obtaining the time value
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.measure_runtime should
    measure the total runtime and return it.
    """
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.perf_counter()

    elasped_time = end_time - start_time

    return elasped_time

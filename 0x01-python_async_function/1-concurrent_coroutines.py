#!/usr/bin/env python3
"""
asyncio module to implement asynchronous programming
and importing List module from typing
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    async routine called wait_n that takes in 2 int
    arguments (in this order): n and max_delay.
    You will spawn wait_random n times with the specified max_delay
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]

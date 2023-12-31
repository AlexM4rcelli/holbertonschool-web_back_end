#!/usr/bin/env python3
"""
    Module to afunction
"""
import random, asyncio


async def async_generator() -> float:
    """
    Loop 10 times, each time yield a random number 
    between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

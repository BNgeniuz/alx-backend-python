#!/usr/bin/env python3
"""define asyncio"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """a random delays btn 0 and max_delay"""
    delay = random.uniform(0, max_delay)

    """wait for the delay"""
    await asyncio.sleep(delay)

    """return delay"""
    return delay

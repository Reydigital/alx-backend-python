#!/usr/bin/env python3

"""

This module contains an asynchronous coroutine.

"""



import asyncio

import random

wait_random = __import__('0-basic_async_syntax').wait_random



print(asyncio.run(wait_random()))

print(asyncio.run(wait_random(5)))

print(asyncio.run(wait_random(15)))

 """

     Args:

             max_delay: The maximum random time generated.

                 Returns:

                         The random generated value between 0 and max_delay.

                             """

                                 rand: float = random.uniform(0, max_delay)

                                     await asyncio.sleep(rand)



                                         return rand

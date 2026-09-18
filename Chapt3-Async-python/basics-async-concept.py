import asyncio
import time


# async function to simulate a task
# async def task():
#     print("step 1")
#     await asyncio.sleep(3)  # there can be a api call here, but for now we will just sleep for 3 seconds
#     print("step 2")


# # Event loop begins here
# asyncio.run(task())




# co-routine function to simulate a task (when to use one co-routine inside another co-routine)
async def process1():
    print("process 1 started")
    await asyncio.sleep(2)
    await process2()
    print("process 1 completed")


async def process2():
    print("process 2 started")
    await asyncio.sleep(2)
    print("process 2 completed")


# event loop begins here
asyncio.run(process1())



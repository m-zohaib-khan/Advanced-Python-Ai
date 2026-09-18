# Suppose your AI application needs information from three APIs:

import asyncio
import time

# weather api:
async def weather():
    print("Getting data from weather...")
    await asyncio.sleep(3)  # Simulating a network call
    print("Sunny")


# news api:
async def news():
    print("Getting news data...")
    await asyncio.sleep(3)  # Simulating a network call
    print("Breaking news: AI is transforming the world!")


# stock api:
async def stock():
    print("Getting stock prices...")
    await asyncio.sleep(3)  # Simulating a network call
    print("Market is bullish today!")


# event loop begins here
async def main():
    # use of async task:
    task = await asyncio.gather(weather(), news(), stock())  # co-rountine use inside it

    print("main completed")


# main code:
if __name__ == "__main__":
    asyncio.run(main())




#  simple example of async function: (event loop):
import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished") # the scheled of task is also depend on the time it takes to complete the task, so task 2 will finish first because it takes less time to complete than task 1.
 
async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
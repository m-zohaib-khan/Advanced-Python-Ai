# co-routine function to simulate a task (when to use one co-routine inside another co-routine)
import asyncio
import time


async def process1():
    print("process 1- first step")
    await asyncio.sleep(3)
    print("process 1- second step")


async def process2():
    print("process 2- first step")
    await asyncio.sleep(3)
    print("process 2- second step")



# event loop begins here
# def main():
#     asyncio.run(process1())
#     asyncio.run(process2())


# if __name__ == "__main__":
#     main()


# if i write it async:
async def main():

    # use of async task:
    task = await asyncio.gather(process1(), process2()) # co-rountine use inside it

    print("main completed")


asyncio.run(main())



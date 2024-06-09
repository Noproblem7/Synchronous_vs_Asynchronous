import time
from datetime import datetime
import asyncio


async def func_1():
    await asyncio.sleep(3)
    print("1-funksiya ishladi")


async def func_2():
    await asyncio.sleep(2)
    print("2-funksiya ishladi")


async def func_3():
    await asyncio.sleep(4)
    print("3-funksiya ishladi")


async def func_4():
    await asyncio.sleep(2)
    print("4-funksiya ishladi")


async def func_5():
    await asyncio.sleep(5)
    print("5-funksiya ishladi")


async def func_6():
    await asyncio.sleep(8)
    print("6-funksiya ishladi")


async def func_7():
    await asyncio.sleep(1)
    print("7-funksiya ishladi")


async def func_8():
    await asyncio.sleep(2)
    print("8-funksiya ishladi")


async def main():
    await asyncio.gather(func_1(), func_2(), func_3(), func_4(), func_5(), func_6(), func_7(), func_8())


if __name__ == "__main__":
    print(datetime.now())
    asyncio.run(main())
    print(datetime.now())

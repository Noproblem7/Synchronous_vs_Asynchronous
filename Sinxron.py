import time
from datetime import datetime


def func_1():
    time.sleep(2)
    print("1-funksiya ishladi")


def func_2():
    time.sleep(2)
    print("2-funksiya ishladi")


def func_3():
    time.sleep(2)
    print("3-funksiya ishladi")
    # func_4()
    # func_5()
    # func_6()


def func_4():
    time.sleep(2)
    print("4-funksiya ishladi")


def func_5():
    time.sleep(2)
    print("5-funksiya ishladi")
    # func_7()


def func_6():
    time.sleep(2)
    print("6-funksiya ishladi")


def func_7():
    time.sleep(2)
    print("7-funksiya ishladi")


def func_8():
    time.sleep(2)
    print("8-funksiya ishladi")


def func():
    print(datetime.now())
    print("funksiya ishladi")
    func_1()
    func_2()
    func_3()
    func_4()
    func_5()
    func_6()
    func_7()
    func_8()
    print(datetime.now())


if __name__ == "__main__":
    func()

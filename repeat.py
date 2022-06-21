from itertools import *


def repeat_nums():
    a = repeat(10, 3)
    for i in a:
        print(i)
    print("*" * 20)

    d = 1
    for i in a:
        if d > 10:
            break
        else:
            print(i)
        d += 1


if __name__ == "__main__":
    repeat_nums()

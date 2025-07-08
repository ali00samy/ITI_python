list = [" ", " ", " ", " ", " "]


def mario_pyramid1():
    height = 5

    for i in range(0, height + 1):
        print(" " * height + "*" * i)
        height -= 1


def mario_pyramid2():
    height = len(list)
    for i in range(height):
        print("".join(list[: height - i - 1]) + "*" * (i + 1))

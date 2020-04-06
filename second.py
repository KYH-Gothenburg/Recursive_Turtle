from turtle import *

WIDTH = 15
BRANCH_LENGTH = 120
ROTATION_LENGTH = 27

def tree(length, level):
    length *= 3/4
    left(ROTATION_LENGTH)
    forward(length)
    if level > 0:
        tree(length, level - 1)
    print(length)
    backward(length)
    right(2 * ROTATION_LENGTH)
    forward(length)

    if level > 0:
        tree(length, level -1)
    backward(length)
    right(2 * ROTATION_LENGTH)




def main():
    hideturtle()
    speed(10)
    left(90)
    tree(BRANCH_LENGTH, 11)
    done()


if __name__ == '__main__':
    main()

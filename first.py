from turtle import *


def square(n):
    if n < 1:
        return
    for i in range(4):
        forward(n)
        right(90)
    square(n-2)


def main():
    hideturtle()
    speed(10)
    for i in range(4):
        square(200)
        right(90)

    done()

if __name__ == '__main__':
    main()

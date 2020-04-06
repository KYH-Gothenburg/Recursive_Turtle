from turtle import *
import random

colors = ['red', 'blue', 'green', 'brown']

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def gen():
    i = 1
    while True:
        yield fib(i)
        i += 1

def circles(length):
    if length > 0:
        circle(length)
        right(90)
        circles(length-1)

def alice_circles(size, c):
    if size > 50:
        color(random.choice(colors))
        for _ in range(8):
            circle(size)
            right(45)
        alice_circles(size - 5, c+1)


def slinky(size):
    if size < 300:
        circle(size)
        right(27)
        slinky(size + 3)


def main():
    hideturtle()
    speed(10)
    left(90)
    penup()

    pendown()
    pensize(1)
    #alice_circles(150, 0)
    slinky(10)
    done()



if __name__ == '__main__':
    main()

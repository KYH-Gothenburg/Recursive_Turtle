from turtle import *
import random

colors = ['red', 'green', 'blue', 'yellow']

def thing(length):
    if length > 0:
        forward(length)
        right(45)
        thing(length-1)


def other_thing(length):
    if length > 0:
        c = random.choice(colors)
        print(c)
        color(c)
        forward(length)
        backward(length)
        right(1)
        other_thing(length-1)


def main():
    hideturtle()
    speed(10)
    other_thing(360)
    done()


if __name__ == '__main__':
    main()

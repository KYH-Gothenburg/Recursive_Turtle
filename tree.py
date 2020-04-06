from turtle import *

def tree(length):
    if length > 1:
        forward(length)
        right(20)
        tree(length-2)
        left(40)
        tree(length-2)
        right(20)
        backward(length)


def main():
    hideturtle()
    speed(10)
    left(90)
    penup()
    backward(100)
    pendown()
    color("green")
    tree(150)
    done()



if __name__ == '__main__':
    main()

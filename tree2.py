from turtle import *

def tree(length):
    if length > 10:
        if length < 25:
            color("red")
        else:
            color("green")
        forward(length)
        right(20)
        tree(length-10)
        left(40)
        tree(length-10)
        right(20)
        backward(length)


def main():
    hideturtle()
    speed(10)
    left(90)
    penup()
    backward(200)
    pendown()
    color("green")
    tree(100)
    done()



if __name__ == '__main__':
    main()

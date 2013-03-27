import turtle

t = turtle.Pen()


def mysquare(size, filled):
    if filled:
        t.begin_fill()
    for x in range(1, 9):
        t.forward(size)
        t.left(45)
    if filled:
        t.end_fill()

mysquare(50, True)
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

t.color(0.75, 1, 1)
mysquare(50, True)
t.color(0, 0, 0)
mysquare(50, False)


import turtle

pen = turtle.Turtle()
pen.speed(5)

def draw_square(length):
    for i in range(4):
        pen.forward(length)
        pen.right(90)

def draw_trangle(length):
    for i in range(3):
        pen.forward(length)
        pen.right(120)

def draw_rectangle(lenght_a, lenght_b):
    for i in range(2):
        pen.forward(lenght_a)
        pen.right(90)
        pen.forward(lenght_b)
        pen.right(90)

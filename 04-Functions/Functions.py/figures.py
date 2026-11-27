###
# Draw a square
#
def draw_square(pen, length):
    for i in range(4):
        pen.forward(length)
        pen.right(90)

###
# Draw a triangle (equilateral/isosceles with equal sides)
#
def draw_trangle(pen, length):
    for i in range(3):
        pen.forward(length)
        pen.left(120)

###
# Draw a rectangle
#
def draw_rectangle(pen, lenght_a, lenght_b):
    for i in range(2):
        pen.forward(lenght_a)
        pen.right(90)
        pen.forward(lenght_b)
        pen.right(90)

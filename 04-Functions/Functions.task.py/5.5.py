###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import figures
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Use the turtle from figures module
pen = figures.pen

## Draw figures
# Square 1
pen.penup()
pen.goto(-200, 150)
pen.pendown()
figures.draw_square(80)

# Square 2
pen.penup()
pen.goto(100, 150)
pen.pendown()
figures.draw_square(60)

# Triangle 1
pen.penup()
pen.goto(-200, 20)
pen.pendown()
figures.draw_trangle(80)

# Triangle 2
pen.penup()
pen.goto(100, 20)
pen.pendown()
figures.draw_trangle(60)

# Rectangle 1
pen.penup()
pen.goto(-200, -100)
pen.pendown()
figures.draw_rectangle(100, 50)

# Rectangle 2
pen.penup()
pen.goto(100, -100)
pen.pendown()
figures.draw_rectangle(80, 40)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()

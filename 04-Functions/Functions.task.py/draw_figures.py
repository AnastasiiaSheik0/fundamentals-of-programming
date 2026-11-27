###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import figures
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

## Draw figures

# First square
pen.penup()
pen.goto(-200, 150)
pen.pendown()
figures.draw_square(pen, 60)

# Second square
pen.penup()
pen.goto(100, 150)
pen.pendown()
figures.draw_square(pen, 80)

# First triangle
pen.penup()
pen.goto(-200, -50)
pen.pendown()
figures.draw_trangle(pen, 70)

# Second triangle
pen.penup()
pen.goto(100, -50)
pen.pendown()
figures.draw_trangle(pen, 90)

# First rectangle
pen.penup()
pen.goto(-200, -120)
pen.pendown()
figures.draw_rectangle(pen, 100, 50)

# Second rectangle
pen.penup()
pen.goto(100, -120)
pen.pendown()
figures.draw_rectangle(pen, 120, 60)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()

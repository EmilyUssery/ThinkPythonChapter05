#!/usr/bin/env python3

import turtle

def sierpinski(t, order, size):
    """Draws a Sierpinski Triangle

    :param t: The turtle object
    :param order: the level of recursion (higher values create more detailed triangles)
    :param size: the size of the largest triangle
    :return: None
    """
    if order == 0:
        # Draw a filled triangle
        t.begin_fill()
        for _ in range(3):
            t.forward(size)
            t.left(120)
        t.end_fill()
    else:
        # Recursively draw 3 smaller triangles
        sierpinski(t, order-1, size/2)
        t.forward(size/2)
        sierpinski(t, order-1, size/2)
        t.backward(size/2)
        t.left(60)
        t.forward(size/2)
        t.right(60)
        sierpinski(t, order-1, size/2)
        t.left(60)
        t.backward(size/2)
        t.right(60)

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("black")
# Set the width and height of the screen
screen.setup(width=500, height=500)

# Create a new turtle object, equivalent to Jupyter's make_turtle
my_turtle = turtle.Turtle()

# Set the turtle's shape and color
my_turtle.shape( "circle" )  # Other options: arrow, classic, square, triangle, and turtle
my_turtle.color( "green" )

# Draw with a turtle.
my_turtle.speed(10)  # Somewhat equivalent to Jupyter turtle's delay parameter (1 slow to 10 fast).
# Position my turtle at the bottom of my window.
my_turtle.penup()
my_turtle.goto(-200, -160)  # Position the turtle
my_turtle.pendown()
# Draw the Sierpinski Triangle
sierpinski(my_turtle, 3, 400)

# Close the turtle graphics window when clicked
turtle.exitonclick()
#!/usr/bin/env python3

import turtle

def snowflake(t:turtle, degree=60):
    n = 360 // degree
    for _ in range(n):
        koch( my_turtle, 120 )
        my_turtle.right( degree )


def koch(t:turtle, x):
    if x < 5:
        t.forward(x)
    else:
        koch(t, x/3)
        t.left(60)
        koch(t, x/3)
        t.right(120)
        koch(t, x/3)
        t.left(60)
        koch(t, x/3)

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
# Let's do the snowflake
# koch(my_turtle, 120)
snowflake(my_turtle, 60)

# Close the turtle graphics window when clicked
turtle.exitonclick()
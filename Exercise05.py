#!/usr/bin/env python

import turtle

def draw(t:turtle, length):
    angle = 50
    factor = 0.6

    if length > 5:
        t.forward( length )
        t.left( angle )
        draw(t, factor * length )
        t.right( 2 * angle )
        draw(t, factor * length )
        t.left( angle )
        t.back( length )

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
my_turtle.speed(5)  # Somewhat equivalent to Jupyter turtle's delay parameter (1 slow to 10 fast).

# HYPOTHESIS: I think this is going to spiral inward until length is less than 5 and then branch out
# WHAT IT DID: More or less what I assumed, but I'd describe it as a balanced tree structure with symmetric branches.
# When the factor is about half the value, its a binary branching.
draw(my_turtle, 100)

# Close the turtle graphics window when clicked
turtle.exitonclick()
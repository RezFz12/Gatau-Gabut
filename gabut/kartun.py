import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Mountain Image")
screen.bgcolor("white")

# Create a turtle object
bob = turtle.Turtle()

# Set turtle attributes
bob.speed(2)  # Set the drawing speed

# Draw the mountain
bob.penup()
bob.goto(-200, -200)
bob.pendown()
bob.color("brown")
bob.begin_fill()
bob.goto(-100, 200)
bob.goto(100, -100)
bob.goto(200, -200)
bob.goto(-200, -200)
bob.end_fill()

# Hide the turtle
bob.hideturtle()

# Exit on click
turtle.done()
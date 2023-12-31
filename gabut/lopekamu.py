import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")

turtle.pensize(2)

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

t.speed(50)
t.color("white", "red")

t.begin_fill()
t.left(140)
t.forward(111.65)
curve()

t.left(120)
curve()
t.forward(111.65)
t.end_fill()
t.hideturtle()

turtle.mainloop()
import turtle
e = turtle.Screen()
e.bgcolor("maroon")
e.setup(500, 500)
ae = turtle.Turtle()
ae.color("white")
length = 200
angle = 90
side = 4
for i in range(side):
    ae.forward(length)
    ae.right(angle)
turtle.done()


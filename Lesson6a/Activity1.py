import turtle
turtle.Screen().bgcolor("maroon")
turtle.Screen().setup(250, 500)
pol = turtle.Turtle()
length = 60
side = 6
angle = 360/side
for i in range(side):
    pol.forward(length)
    pol.right(angle)
turtle.done()
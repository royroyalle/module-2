import turtle
w = turtle.Screen()
w.bgcolor("purple")
w.title("Turtle")
n = turtle.Turtle()
n.color("white")
size=0
while True:
    for i in range(4):
        n.fd(size +1)
        n.left(90)
        size = size - 5
    size = size +1

import turtle
turtle.Screen().bgcolor("Orange")

turtle.title("Welcome to Turtle")
t = turtle.Turtle()
for i in range(3):
    t.forward(100)
    t.right(120)
    i += i

t.left(90)
t.penup()
t.forward(100)
t.pendown()

for i in range(2):
    t.forward(100)
    t.left(90)
    t.forward(150)
    t.left(90)
    i += i

t.right(90)
t.penup()
t.forward(100)
t.pendown()

for i in range(6):
    t.forward(100)
    t.left(60)
    i += i

turtle.done()
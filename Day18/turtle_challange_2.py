from turtle import Turtle, Screen
meow =Turtle()
for _ in range(15):
    meow.color("white")
    meow.forward(2)
    meow.color("black")
    meow.forward(2)

for _ in range(15):
    meow.forward(10)
    meow.penup()
    meow.forward(10)
    meow.pendown()


screen = Screen()
screen.exitonclick()
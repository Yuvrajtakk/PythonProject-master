import random
import turtle as t
# from turtle import Turtle, Screen

# meow = Turtle()
meow = t.Turtle()

# colors = ["dark green","blue", "light sea green","magenta","red", "maroon", "yellow","cyan" ]
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour =(r,g,b)
    return random_colour


angle = [0, 90, 180, 270]
meow.width(15)
meow.speed("fastest")
for _ in range(200):
    # meow.color(random.choice(colors))
    meow.color(random_color())
    # meow.left(random.choice(angle))
    meow.setheading(random.choice(angle))
    meow.forward(20)

# screen = Screen()
# screen.exitonclick()

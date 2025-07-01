import random
import turtle as t


meow = t.Turtle()
meow.speed("fastest")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour =(r,g,b)
    return random_colour

def circle(radius):
    meow.circle(radius)

# for angle in range(36):
#     meow.color(random_color())
#     meow.left(angle)
#     circle(100)
#     angle += 10

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        meow.color(random_color())
        circle(100)
        meow.setheading(meow.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
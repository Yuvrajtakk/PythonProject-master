# import colorgram
#
# rgb_colors = []
# colour = colorgram.extract('image.jpg',30)
# for color in colour:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as t
import random
color_list = [(226, 147, 98), (28, 102, 177), (161, 56, 90), (148, 79, 51), (225, 61, 96), (113, 174, 215), (244, 227, 95), (173, 20, 41), (233, 79, 51), (224, 126, 156), (118, 184, 130), (11, 172, 207), (165, 151, 25), (13, 58, 148), (83, 37, 23), (128, 37, 27), (37, 129, 78), (42, 192, 160), (14, 39, 92), (129, 238, 190), (244, 162, 151), (235, 162, 181), (100, 101, 186), (127, 214, 239), (66, 77, 38), (74, 31, 46)]
# dot = t.Turtle()
#
# dot.width(25)
# dot.color("white")
# dot.shape("circle")
#
# for _ in range(1,11):
#     for _ in range(1,11):
#         dot.showturtle()
#         dot.color("black")
#         dot.color(random.choice(color_list))
#         dot.forward(1)
#         dot.penup()
#         dot.forward(50)
#         dot.pendown()

t.colormode(255)
meow = t.Turtle()
meow.hideturtle()
meow.speed("fastest")
meow.penup()
meow.setheading(225)
meow.forward(300)
meow.setheading(0)
for _ in range(1,11):
    for _ in range(1,11):
        meow.dot(20, random.choice(color_list))
        meow.forward(50)
    meow.setheading(90)
    meow.forward(50)
    meow.setheading(180)
    meow.forward(500)
    meow.setheading(0)

screen = t.Screen()
screen.exitonclick()

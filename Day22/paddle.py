from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self,cord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(cord)

    def up(self):
        new_y = self.ycor() + 45
        self.goto(self.xcor(), new_y)
    def down(self):
        new_y = self.ycor() - 45
        self.goto(self.xcor(), new_y)


from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.highscore = 0
        with open("data.txt") as data :
            self.highscore = int(data.read())
        self.color("yellow")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_score()

    # def read_hscore_data(self):
    #     with open("data.txt") as file:
    #         hscore = file.read()
    #         return hscore
    # def write_hscore_data(self,score):
    #     with open("data.txt", mode= "w") as file:
    #         file.write(self.score)

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}",align=ALIGNMENT,font = FONT )

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt",mode= "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()


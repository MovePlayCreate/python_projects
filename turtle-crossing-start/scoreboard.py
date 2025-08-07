from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.penup()
        self.goto(-200, 270)
        self.write(f"Level: {self.score}", align="left", font=(FONT))

    def player_scores(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        #self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=(FONT))

from turtle import Turtle

POSITION1 = (-35, 250)
POSITION2 = (20, 250)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0

    def write_score(self):
        self.write(f"{self.score}", True, font=("Times New Romans", 24, "normal"))

    def position1(self):
        self.goto(POSITION1)
        self.write_score()

    def position2(self):
        self.goto(POSITION2)
        self.write_score()
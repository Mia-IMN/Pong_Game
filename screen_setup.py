from turtle import Turtle

class ScreenSetup(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.pensize(2)
        self.goto(x=0, y=300)
        self.setheading(270)

        while self.ycor() > -290:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

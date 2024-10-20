from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")

    def launch(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() - 10
        self.goto(new_x, new_y)
        if self.ycor() > 290:
            new_x = self.xcor() + 10
            new_y = self.ycor() - 10
            self.goto(new_x, new_y)
        if self.ycor() < -280:
            new_x = self.xcor() + 10
            new_y = self.ycor() + 10
            self.goto(new_x, new_y)
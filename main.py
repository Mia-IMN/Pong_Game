import time
from turtle import Screen
from scoreboard import Scoreboard
from screen_setup import ScreenSetup
from paddle import Paddle
from ball import Ball

PADDLE_XCOR = 370
screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

ScreenSetup()
Scoreboard().position1()
Scoreboard().position2()

r_paddle = Paddle((PADDLE_XCOR, 0))
l_paddle = Paddle((-PADDLE_XCOR, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "space")

ball = Ball()


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.launch()

screen.exitonclick()
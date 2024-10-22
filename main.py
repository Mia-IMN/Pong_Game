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
scoreboard = Scoreboard()
ScreenSetup()

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

    # To detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # To detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Detects when r_paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detects when l_paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()
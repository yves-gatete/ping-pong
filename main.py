from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


LEFT_POS = (350, 0)
RIGHT_POS = (-350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)


#paddles
r_paddle = Paddle(LEFT_POS)
l_paddle = Paddle(RIGHT_POS)

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

pong = Ball()
scores = Scoreboard()

game_on = True
while game_on:
    time.sleep(pong.move_speed)
    screen.update()
    pong.move()

    # detect colision with top and bottom walls
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce_up_down()

    # detect collision with paddle
    if pong.distance(l_paddle) < 50 and pong.xcor() < -320 or pong.distance(r_paddle) < 50 and pong.xcor() > 320:
        pong.bounce_left_right()
    
    # if right paddle misses
    if pong.xcor() > 380:
        pong.reset_position()
        scores.l_scores()
        scores.update_scoreboard()

    # if left paddle misses
    if pong.xcor() < - 380:
        pong.reset_position()
        scores.r_scores()
        scores.update_scoreboard()


screen.exitonclick()
"""
Ping Pong Game

Main entry point for the Ping Pong (Pong) game. Sets up the screen, paddles, ball, and scoreboard,
and runs the main game loop that handles physics and score updates.

Controls:
  - Right paddle: Up/Down arrow keys
  - Left paddle: W/S keys
"""

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Paddle starting positions (x, y)
LEFT_POS = (350, 0)
RIGHT_POS = (-350, 0)

# Set up the game window
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)  # Turn off auto screen updates for smooth animation

# Create paddles (right and left)
r_paddle = Paddle(LEFT_POS)
l_paddle = Paddle(RIGHT_POS)

# Keyboard controls
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Create ball and scoreboard
pong = Ball()
scores = Scoreboard()

# Main game loop
# The loop updates the screen, moves the ball, checks for collisions, and updates the score.
game_on = True
while game_on:
    # Control frame rate by sleeping according to ball.move_speed
    time.sleep(pong.move_speed)
    screen.update()
    pong.move()

    # Detect collision with top and bottom walls and bounce vertically
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce_up_down()

    # Detect collision with paddles (distance check + x position range)
    if (pong.distance(l_paddle) < 50 and pong.xcor() < -320) or (pong.distance(r_paddle) < 50 and pong.xcor() > 320):
        pong.bounce_left_right()

    # If right paddle misses the ball (ball crosses right boundary)
    if pong.xcor() > 380:
        pong.reset_position()
        scores.l_scores()
        scores.update_scoreboard()

    # If left paddle misses the ball (ball crosses left boundary)
    if pong.xcor() < -380:
        pong.reset_position()
        scores.r_scores()
        scores.update_scoreboard()

screen.exitonclick()
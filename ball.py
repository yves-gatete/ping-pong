"""
Ball Class

Represents the ball in the Ping Pong game. Handles movement, bouncing, and resetting.
"""

from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        """Initialize the ball at the center with movement properties."""
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # How much the ball moves each frame in x and y directions
        self.x_increase = 10
        self.y_increase = 10
        # Controls the frame delay; lower is faster
        self.move_speed = 0.1

    def move(self):
        """Move the ball by its current x and y increments."""
        new_x = self.xcor() + self.x_increase
        new_y = self.ycor() + self.y_increase
        self.goto(new_x, new_y)

    def bounce_up_down(self):
        """Reverse the vertical direction when the ball hits top/bottom walls."""
        self.y_increase *= -1

    def bounce_left_right(self):
        """Reverse the horizontal direction when the ball hits a paddle.

        Also slightly increases speed to make the game progressively harder.
        """
        self.x_increase *= -1
        # speed up by 10% (reduce sleep time)
        self.move_speed *= 0.9

    def reset_position(self):
        """Send the ball back to the center and reverse its x direction.

        This is used when a player misses the ball and a point is scored.
        """
        self.goto(0, 0)
        self.bounce_left_right()

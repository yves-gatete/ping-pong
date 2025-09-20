"""
Paddle Class

Represents a paddle in the Ping Pong game. Inherits from Turtle and can move up or down.
"""

from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        """Initialize the paddle at the given position."""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)
        
    def go_up(self):
        """Move the paddle up by 20 units."""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    def go_down(self):
        """Move the paddle down by 20 units."""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
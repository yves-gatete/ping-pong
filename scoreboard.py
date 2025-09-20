"""
Scoreboard Class

Handles the display and updating of the score for both players.
"""

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        """Initialize the scoreboard and display the initial scores."""
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        # Left and right player scores
        self.l_score = 0
        self.r_score = 0
        # Draw the initial scoreboard
        self.update_scoreboard()

    def l_scores(self):
        """Increase the left player's score by 1."""
        self.l_score += 1

    def r_scores(self):
        """Increase the right player's score by 1."""
        self.r_score += 1

    def update_scoreboard(self):
        """Update the scoreboard display with current scores."""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 80, 'normal'))
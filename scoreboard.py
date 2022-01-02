from turtle import Turtle


class Scoreboard(Turtle):
    """ handles everything connected to the score"""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """ updates the scoreboard """
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("courier", 25, "normal"))

    def update_score(self):
        """ adds to score whenever food is eaten"""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """ writes game over when the game is over"""
        self.home()
        self.write(f"GAME OVER", align="center", font=("courier", 25, "normal"))

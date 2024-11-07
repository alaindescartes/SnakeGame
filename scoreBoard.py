from turtle import Turtle

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.scoreboard = Turtle()
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.scoreboard.color("white")
        self.scoreboard.goto(0, 430)
        self.display_score()

    def display_score(self):
        """
        displays the scoreboard
        """
        # Clear the previous score and write the new score
        self.scoreboard.clear()
        self.scoreboard.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        """
        increases score by 1
        """
        # Increase the score and update the display
        self.score += 1
        self.display_score()
    def display_message(self, message):
        """
        displays a message
        :param message: mesage to be displayed
        """
        self.scoreboard.clear()
        self.scoreboard.write(message, align="center", font=("Arial", 24, "normal"))

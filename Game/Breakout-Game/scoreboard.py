from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-50, 260)
        self.write(f"Score: {self.score}",  align="center", font=("Arial", 10, "normal"))
        self.goto(50, 260)
        self.write(f"Lives: {self.lives}", align="center", font=("Arial", 10, "normal"))

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("You Lose", align="center", font=("Arial", 40, "normal"))

    def you_win(self):
        self.clear()
        self.goto(0,0)
        self.write("You Win", align="center", font=("Arial", 40, "normal"))
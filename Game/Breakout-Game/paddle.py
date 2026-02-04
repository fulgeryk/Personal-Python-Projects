from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=7)
        self.goto(position)

    def move_left(self):
        if self.xcor() > -330:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())

    def move_right(self):
        if self.xcor() < 310:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())
from turtle import Turtle

class Block(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(color)
        self.penup()
        self.goto(x,y)

    def destroy(self):
        self.hideturtle()

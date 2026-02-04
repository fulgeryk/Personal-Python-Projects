from turtle import Screen


class GameScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Breakout Game")
        self.screen.tracer(0)

    def update(self):
        self.screen.update()

    def listen(self):
        self.screen.listen()

    def onkey(self, key, func):
        self.screen.onkey(key=key, fun=func)

    def exit_on_click(self):
        self.screen.exitonclick()
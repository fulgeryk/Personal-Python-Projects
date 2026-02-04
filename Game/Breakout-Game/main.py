from screen import GameScreen
from paddle import Paddle
from ball import Ball
from blocks import Block
from scoreboard import ScoreBoard
import time

Y_POS = -260
X_POS = 0
COLORS = ["red", "orange", "yellow", "green", "blue", "coral"]
ROWS = 6
COLS = 15
X_SPACING = 50
Y_SPACING = 35
START_X_BLOCK = -350
START_Y_BLOCK = 220

gamescreen = GameScreen()
scoreboard = ScoreBoard()
ball = Ball()
pad = Paddle((X_POS, Y_POS))
gamescreen.listen()
gamescreen.onkey("Left", pad.move_left)
gamescreen.onkey("Right", pad.move_right)
list_of_blocks = []
for r in range (0,ROWS):
    for c in range (0,COLS):
        x = START_X_BLOCK + c*X_SPACING
        y = START_Y_BLOCK - r*Y_SPACING
        color = COLORS[r]
        list_of_blocks.append(Block(x,y,color))

game_is_on = True
ball_attached = True

def change_on_space():
    global ball_attached
    ball_attached = False
    if ball.y_move < 0:
        ball.bounce_y()

gamescreen.onkey("space", change_on_space)

while game_is_on:
    gamescreen.update()
    time.sleep(ball.move_speed)
    if ball_attached:
        pad_pos = pad.position()
        ball.follow_paddle(pad_pos[0], pad_pos[1])
    else:
        ball.move()
    #Collision with x walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()
    #Collision with y walls
    if ball.ycor() > 280:
        ball.bounce_y()

    if not ball_attached:
        #Detect collision with paddle
        if ball.distance(pad) < 50 and ball.ycor() < -230:
            ball.move_speed *= 0.9
            ball.bounce_y()

    #Detect with objects:
    for i in list_of_blocks:
        if ball.distance(i) < 35:
            ball.bounce_y()
            i.destroy()
            scoreboard.point()
            list_of_blocks.remove(i)
            break

    #If you miss the ball
    if ball.ycor() < -270:
        scoreboard.lose_life()
        ball.reset_position()
        pad.goto(X_POS, Y_POS)
        ball_attached = True
        if scoreboard.lives == 0:
            scoreboard.game_over()
            game_is_on = False

    if not list_of_blocks:
        scoreboard.you_win()
        game_is_on = False

gamescreen.exit_on_click()
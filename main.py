from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from board import Board
import time

"""
@bref: juego de pong en el que la pantalla detecta que Tecla es presionada para mover los paddles,
sin embargo tiene la limitacion, debido a la libreria turtle, que cuando se presionan 2 teclas, 
solo obedece a la ultima que se presiono. 
"""


screen = Screen()
screen.bgcolor("black")
screen.setup(width=850, height=650)
screen.title("Pong Game")
screen.tracer(0)

screen.listen()

l_paddle = Paddle(xcor=-350)
r_paddle = Paddle(xcor=350)

ball = Ball()
score = Scoreboard()
board = Board()

screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    #collision with the paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 328) or (ball.distance(l_paddle) < 50 and ball.xcor() < -328):
        ball.bounce_x()
        ball.move_speed *= 0.9

    #detect when paddle miss the ball
    if ball.xcor() > 380:
        ball.reset_pos()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_pos()
        score.r_point()

    if score.l_score == 5 or score.r_score == 5:
        game_is_on = False
        score.goto(0, 0)
        score.write("Game Over", align="center", font=("Courier", 25, "bold"))

screen.exitonclick()


from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from board import Board
import time

"""
@bref: debido a las limitaciones de la libreria turtle al presionar 2 teclas al mismo tiempo, 
se implemento esta mejora:
consiste en cambiar los estados 1/0 de una variable para cada tecla, cada que se presiona o se suelte,
de esta manera en el ciclo while se inspeccionan éstas variables y se realiza el mov de los paddles,
de esta forma disminuye la interferencia de los jugadores al mover al mismo tiempo el paddle.
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

#variables para cada tecla de cada jugador
w_press = False
s_press = False
up_press = False
down_press = False

#funciones que modifican el estado de las variables
def wpress_y():
    global w_press
    w_press = True

def wpress_n():
    global w_press
    w_press = False

def spress_y():
    global s_press
    s_press = True

def spress_n():
    global s_press
    s_press = False

def uppress_y():
    global up_press
    up_press = True

def uppress_n():
    global up_press
    up_press = False

def downpress_y():
    global down_press
    down_press = True

def downpress_n():
    global down_press
    down_press = False
#al presionar o soltar una tecla modifica el estado de las variables
screen.onkeypress   (wpress_y, "w")
screen.onkeyrelease (wpress_n, "w")
screen.onkeypress   (spress_y, "s")
screen.onkeyrelease (spress_n, "s")
screen.onkeypress   (uppress_y, "Up")
screen.onkeyrelease (uppress_n, "Up")
screen.onkeypress   (downpress_y, "Down")
screen.onkeyrelease (downpress_n, "Down")

#---- modificacion de teclas
# screen.onkeypress(l_paddle.move_up, "w")
# screen.onkeypress(l_paddle.move_down, "s")
# screen.onkeypress(r_paddle.move_up, "Up")
# screen.onkeypress(r_paddle.move_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    #inspeccion de las variables para el mov de los paddles
    if w_press: l_paddle.move_up()
    elif s_press: l_paddle.move_down()

    if up_press: r_paddle.move_up()
    elif down_press: r_paddle.move_down()

    #rebote al llegar a la parte superior o inferior
    if (ball.ycor() > 275) or (ball.ycor() < -275):
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

    #condicion para terminar el juego
    if score.l_score == 5 or score.r_score == 5:
        game_is_on = False
        score.goto(0, 0)
        score.write("Game Over", align="center", font=("Courier", 25, "bold"))

screen.exitonclick()


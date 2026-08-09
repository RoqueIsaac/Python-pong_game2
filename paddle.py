from turtle import Turtle

class Paddle(Turtle):
    """Creacion de Paddle,
    xcor = posicion_x del paddel,
    ycor se omite como argumento, por default es 0
    """
    def __init__(self, xcor, ycor=0):
        super().__init__()
        self.new_ycor = ycor
        self.new_xcor = xcor
        self.penup()
        self.goto(self.new_xcor, self.new_ycor)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)


    def move_up(self):
        self.new_ycor = self.ycor() + 20
        self.setpos(self.new_xcor, self.new_ycor )


    def move_down(self):
        self.new_ycor = self.ycor() - 20
        self.setpos(self.new_xcor, self.new_ycor )



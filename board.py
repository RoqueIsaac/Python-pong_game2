from turtle import Turtle


class Board(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.teleport(x=0, y=-290)
        self.left(90)
        self.color("white")
        self.width(4)
        self.STEP = 20
        # while self.ycor() < 285:
        #     self.pd()
        #     self.fd(self.STEP)
        #     self.pu()
        #     self.fd(self.STEP)

        self.pu()
        self.goto(0, 290)
        self.setheading(0)
        self.pd()
        self.fd(395)
        self.setheading(-90)
        self.fd(580)
        self.setheading(180)
        self.fd(790)
        self.setheading(90)
        self.fd(580)
        self.setheading(0)
        self.fd(400)

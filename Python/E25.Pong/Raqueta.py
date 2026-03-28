from turtle import Turtle


class raqueta(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()

    def mover_arriba(self):
        nueva_y=self.ycor()+20
        self.goto(self.xcor(),nueva_y)
    
    def mover_abajo(self):
        nueva_y=self.ycor()-20
        self.goto(self.xcor(),nueva_y)
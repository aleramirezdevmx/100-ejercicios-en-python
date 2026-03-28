from turtle import Turtle


class bola(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.penup()
        self.x_movimiento=10
        self.y_movimiento=10
        self.velocidad=0.1

    def mover_inicial(self):
        y=self.ycor()+ self.y_movimiento
        x=self.xcor()+ self.x_movimiento
        self.goto(x,y)

    def balanceo_y(self):
        self.y_movimiento*=-1

    def balanceo_x(self):
        self.x_movimiento*=-1
        self.velocidad*=0.9
    
    def posicion_inicial(self):
        self.goto(0,0)
        self.balanceo_x()
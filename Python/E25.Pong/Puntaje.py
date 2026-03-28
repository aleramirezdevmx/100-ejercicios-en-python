from turtle import Turtle

class puntaje(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r1_puntaje=0
        self.r2_puntaje=0
        self.actual_puntaje()
        
    def actual_puntaje(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.r2_puntaje,align="center", font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.r1_puntaje,align="center", font=("Courier",80,"normal"))

    def r2_marcador(self):
        self.r2_puntaje+=1
        self.actual_puntaje()

    def r1_marcador(self):
        self.r1_puntaje+=1
        self.actual_puntaje()

    
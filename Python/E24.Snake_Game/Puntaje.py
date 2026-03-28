from turtle import Turtle

class Puntaje(Turtle):

    def __init__(self):
        super().__init__()
        self.puntaje=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(f"Puntaje: {self.puntaje}",align="center", font=("Arial", 14,"normal"))
    
    def juego_perdido(self):
        self.clear()
        self.goto(0,0)
        self.write("¡PERDISTE!",align="center", font=("Arial", 16,"normal"))
        
    

    def incrementar_puntaje(self):
        self.puntaje+=1
        self.clear()
        self.write(f"Puntaje: {self.puntaje}",align="center", font=("Arial", 14,"normal"))
        
    

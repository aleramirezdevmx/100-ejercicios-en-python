from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.nivel=1
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        self.color("white")
        self.write(f"Nivel: {self.nivel}", align="left",font=FONT)

    def actualizar_nivel(self):
        self.clear()
        self.write(f"Nivel: {self.nivel}", align="left",font=FONT)

    def incrementar_nivel(self):
        self.nivel+=1
        self.actualizar_nivel()

    def perder(self):
        self.goto(0,0)
        self.write("¡PERDISTE!", align="center",font=FONT)
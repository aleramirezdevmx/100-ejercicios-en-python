from turtle import Turtle,Screen
from Raqueta import raqueta
from Pelota import bola
import time
from Puntaje import puntaje

screen=Screen()

screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

texto=Turtle()
texto.color("White")
texto.hideturtle()

linea = Turtle()
linea.color("white")
linea.penup()
linea.hideturtle()
linea.goto(0, 300)
linea.setheading(270)  # apuntar hacia abajo

for _ in range(30):
    linea.pendown()
    linea.forward(10)
    linea.penup()
    linea.forward(10)


raqueta1=raqueta()
raqueta2=raqueta()

raqueta1.color("red")
raqueta1.goto(350,0)

raqueta2.color("blue")
raqueta2.goto(-350,0)

screen.listen()
screen.onkey(raqueta1.mover_arriba,"w")
screen.onkey(raqueta2.mover_arriba,"Up")
screen.onkey(raqueta1.mover_abajo,"s")
screen.onkey(raqueta2.mover_abajo,"Down")

pelota=bola()
marcador=puntaje()

juego_encendido=True


while juego_encendido:
    time.sleep(pelota.velocidad)
    pelota.mover_inicial()
    screen.update()

    if pelota.ycor()>280 or pelota.ycor()<-280:
        pelota.balanceo_y()
    
    if pelota.distance(raqueta1)<50 and pelota.xcor()>340:
        pelota.balanceo_x()
    if pelota.distance(raqueta2)<50 and pelota.xcor()<-340:
        pelota.balanceo_x()
    
    if pelota.xcor()>380:
        pelota.posicion_inicial()
        marcador.r2_marcador()

    if pelota.xcor()<-380:
        pelota.posicion_inicial()
        marcador.r1_marcador()

    if marcador.r1_puntaje==5:
        texto.goto(0,0)
        linea.clear()
        marcador.clear()
        texto.write("Gano el equipo rojo",align="center", font=("Courier",20,"normal"))
        juego_encendido=False

    elif marcador.r2_puntaje==5:
        texto.goto(0,0)
        linea.clear()
        marcador.clear()
        texto.write("Gano el equipo azul",align="center", font=("Courier",20,"normal"))
        juego_encendido=False

    
screen.exitonclick()

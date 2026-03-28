from turtle import Screen
import time
from Snake import Snake
from Food import Food
from Puntaje import Puntaje

#Crear pantalla
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
puntaje=Puntaje()

screen.listen()
screen.onkey(snake.arriba, "Up")
screen.onkey(snake.abajo, "Down")
screen.onkey(snake.izquierda, "Left")
screen.onkey(snake.derecha, "Right")

iniciar_juego= True
while iniciar_juego:
    screen.update()
    time.sleep(0.1)

    snake.mover()

    #detectar colision con la comida
    if snake.cabeza.distance(food) <15:
        food.nueva_locacion()
        snake.crecer()
        puntaje.incrementar_puntaje()
  
    #detectar colision con la pared
    if snake.cabeza.xcor() >280 or snake.cabeza.xcor() <-280 or snake.cabeza.ycor() <-280 or snake.cabeza.ycor() >280:
        iniciar_juego=False
        puntaje.juego_perdido()
    
    #detectar colision con la cola
    for segmento in snake.segmentos[1:]:
        if snake.cabeza.distance(segmento)<10:
            iniciar_juego=False
            puntaje.juego_perdido()


screen.exitonclick()

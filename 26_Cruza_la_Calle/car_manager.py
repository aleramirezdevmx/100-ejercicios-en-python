from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.carros = []
        self.velocidad_carro = STARTING_MOVE_DISTANCE

    def crear_carro(self):
        aleatoriedad= random.randint(1,10)
        if aleatoriedad==1:
            nuevo_carro=Turtle("square")
            nuevo_carro.shapesize(stretch_wid=1,stretch_len=2)
            nuevo_carro.penup()
            nuevo_carro.color(random.choice(COLORS))
            y_posicion=random.randint(-250,250)
            nuevo_carro.goto(300, y_posicion)
            self.carros.append(nuevo_carro)
        
    def mover_carro(self):
        for car in self.carros:
            car.backward(self.velocidad_carro)

    def nivel(self):
        self.velocidad_carro+= MOVE_INCREMENT
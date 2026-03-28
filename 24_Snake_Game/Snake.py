from turtle import Turtle


POSICION_INICIAL= [(0,0),(-20,0),(-40,0)]
DISTANCIA=20
ARRIBA=90
ABAJO=270
IZQUIERDA=180
DERECHA=0
class Snake:

    def __init__(self):
        self.segmentos=[]
        self.crear_snake()
        self.cabeza=self.segmentos[0]

    def crear_snake(self):
        for posicion in POSICION_INICIAL:
            self.otro_segmento(posicion)
    
    def otro_segmento(self,posicion):
        nuevo_segmento=Turtle("square")
        nuevo_segmento.color("white")
        nuevo_segmento.penup()
        nuevo_segmento.goto(posicion)
        self.segmentos.append(nuevo_segmento)

    def crecer(self):
        self.otro_segmento(self.segmentos[-1].position())
    
    def mover(self):
        for seg_num in range(len(self.segmentos)-1, 0, -1):
            nueva_x=self.segmentos[seg_num-1].xcor()
            nueva_y=self.segmentos[seg_num-1].ycor()
            self.segmentos[seg_num].goto(nueva_x,nueva_y)
        self.cabeza.forward(DISTANCIA)

    def arriba(self):
        if self.cabeza.heading()!=ABAJO:
            self.cabeza.setheading(ARRIBA)

    def abajo(self):
        self.cabeza.setheading(ABAJO)

    def izquierda(self):
        self.cabeza.setheading(IZQUIERDA)

    def derecha(self):
        self.cabeza.setheading(DERECHA)
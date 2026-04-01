import turtle

# 1. Configurar la pantalla
screen = turtle.Screen()
screen.setup(width=1200, height=800)
# Reemplaza con el nombre de tu archivo .gif
screen.bgpic("mapa.gif") 

# 2. Función para obtener y mostrar coordenadas
def obtener_coordenadas(x, y):
    print(f"Coordenadas: x={x}, y={y}")
    # Opcional: dibujar un punto donde se hizo clic
    t.goto(x, y)
    t.dot(10, "red")

# 3. Registrar el evento de clic (1 = clic izquierdo)
screen.onscreenclick(obtener_coordenadas, 1)

# 4. Configurar la tortuga para marcar puntos
t = turtle.Turtle()
t.penup()
t.hideturtle()

# Escuchar eventos y mantener la ventana abierta
screen.listen()
screen.mainloop()
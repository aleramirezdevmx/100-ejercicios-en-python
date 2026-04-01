import turtle
import pandas

screen=turtle.Screen()
screen.title("Estado de Mexico")
screen.setup(width=1200,height=800)
image="mapa.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("estados.csv")
estados=data["estado"].to_list()
estados_adivinados=[]

while len(estados_adivinados)<32:
    respuesta=screen.textinput(title=f"{len(estados_adivinados)}/32 Adivina el estado", prompt="Menciona un estado:").title()
    if respuesta=="Salir":
        aprender = []
        for estado in estados:
            if estado not in estados_adivinados:
                aprender.append(estado)
        aprender_estados=pandas.DataFrame(aprender)
        aprender_estados.to_csv("estados_por_aprender.csv")
        break
    if respuesta in estados:
        estados_adivinados.append(respuesta)
        t=turtle.Turtle()
        t.shape("circle")
        t.shapesize(stretch_wid=0.5, stretch_len=0.5)
        t.penup()
        datos_estado=data[data.estado==respuesta]
        t.goto(datos_estado.corx.item(),datos_estado.cory.item())
        
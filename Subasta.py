import os

def limpiar_pantalla():
  if os.name == 'nt': # Para Windows
    os.system('cls')

def mejor_postor(ofertas):
    i=0
    ganador=""
    for nombre in ofertas:
        if i<ofertas[nombre]:
            i=ofertas[nombre]
            ganador=nombre
        else:
            i=i
    print(f"El mejor postor es {ganador} con: ${i}")

print("Bienvenido a la subasta")
ofertas={}
existe=True

while existe:
    nombre=input("¿Cuál es tu nombre?")
    oferta=int(input("¿Cuánto ofreces?$"))
    ofertas[nombre]=oferta

    condicion=input("¿Hay otro postor 'S' o 'N'?").lower()
    if condicion=="s":
        existe=True
        limpiar_pantalla()
    else:
        existe=False
        limpiar_pantalla()

mejor_postor(ofertas)
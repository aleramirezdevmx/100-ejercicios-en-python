import random

print("Bienvenido al adivinador de números")
print("Elige un número entre 1 y 100")
nivel_input = input("Elige el nivel: \n a. Fácil \n b. Difícil \n\n")


if nivel_input == "a":
    print("Elegiste el nivel fácil, tienes 10 intentos")
    nivel_intentos = 10
elif nivel_input == "b":
    print("Elegiste el nivel difícil, tienes 5 intentos")
    nivel_intentos = 5
else:
    print("Nivel no válido. Usando nivel fácil (10 intentos).")
    nivel_intentos = 10


def aleatorio():
    n_aleatorio = random.randint(1, 100)
    return n_aleatorio

def comparacion(adivinando, numero_random):
    if adivinando < numero_random:
        return "Muy bajo"
    elif adivinando > numero_random:
        return "Muy alto"
    elif adivinando == numero_random:
        return "Ganaste"

def intento():
    try:
        adivinado = int(input("Adivina el número: "))
        return adivinado
    except ValueError:
        print("Por favor, introduce un número válido.")
        return None

def ciclo(intentos_disponibles, numero_secreto):
    global bandera
    
    for i in range(intentos_disponibles):
        print("Tienes", intentos_disponibles - i, "intentos para descubrir el número")
        
        adivinado = intento()
        
        if adivinado is None:
            continue
            
        resultado = comparacion(adivinado, numero_secreto)
        print(resultado)
        
        if resultado == "Ganaste":
            bandera = 1
            break
        
    if bandera == 0:
        print(f"Perdiste: se te acabaron los intentos. El número era {numero_secreto}") 

num_aleatorio = aleatorio()
bandera = 0

ciclo(nivel_intentos, num_aleatorio)
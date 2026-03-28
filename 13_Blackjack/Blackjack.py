import random
import os

def m_carta():
    cartas=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    carta=random.choice(cartas)
    return carta

def puntaje(cartas):
    """Calcula el puntaje, ajustando los Ases de 11 a 1 si es necesario."""
    # Blackjack: 21 con solo 2 cartas
    if sum(cartas) == 21 and len(cartas) == 2:
        return 0 # 0 para indicar Blackjack

    # Corregido: Maneja múltiples Ases
    puntuacion = sum(cartas)
    num_ases = cartas.count(11)

    while puntuacion > 21 and num_ases > 0:
        puntuacion -= 10 # Cambio de 11 a 1 (11 - 10 = 1)
        num_ases -= 1
        
    return puntuacion

def comparacion(puntaje_usuario, puntaje_computadora):
    """Compara los puntajes finales."""
    
    # 1. Chequeo de Blackjack
    if puntaje_usuario == 0:
        return "Ganaste, tienes el Blackjack! 👑"
    if puntaje_computadora == 0:
        return "Perdiste, la computadora tiene el Blackjack. 💻"
        
    # 2. Chequeo de Pasarse (Bust)
    if puntaje_usuario > 21:
        return "Te pasaste de 21, perdiste. 💥"
    if puntaje_computadora > 21:
        return "La computadora se pasó de 21, ¡Ganaste! 🎉"

    # 3. Comparación Final
    if puntaje_usuario == puntaje_computadora:
        return "Empate. 🤝"
    elif puntaje_usuario > puntaje_computadora:
        return "Ganaste. ✅"
    else: # puntaje_computadora > puntaje_usuario
        return "Perdiste. ❌"
    
def jugar(): 
    cartas_usuario=[]
    cartas_computadora=[]
    juego_terminado=False

    for _ in range(2):
        cartas_usuario.append(m_carta())
        cartas_computadora.append(m_carta())

    # --- Turno del Usuario ---
    while not juego_terminado:
        puntaje_usuario = puntaje(cartas_usuario)
        puntaje_computadora = puntaje(cartas_computadora)
        
        # Muestra la información del juego
        print(f"\nTus cartas son: {cartas_usuario}, puntaje actual: {puntaje_usuario}")
        print(f"La primer carta de la computadora es: [{cartas_computadora[0]}]")

        # Verifica si el juego termina inmediatamente (Blackjack o Pasarse)
        if puntaje_usuario == 0 or puntaje_computadora == 0 or puntaje_usuario > 21:
            juego_terminado = True
        else:
            eleccion_usuario = input("Teclea 's' si quieres otra carta o teclea 'n' si no quieres otra carta: ")
            if eleccion_usuario.lower() == "s":
                cartas_usuario.append(m_carta())
            else:
                juego_terminado = True

    # --- Turno de la Computadora (Solo si el usuario no se pasó) ---
    # Es crucial calcular el puntaje final del usuario ANTES de que juegue la computadora
    puntaje_usuario = puntaje(cartas_usuario) 

    # CORREGIDO: La computadora solo juega si el usuario NO se ha pasado.
    if puntaje_usuario <= 21 and puntaje_usuario != 0: 
        while puntaje_computadora != 0 and puntaje_computadora < 17:
            cartas_computadora.append(m_carta())
            puntaje_computadora = puntaje(cartas_computadora)

    # --- Resultados Finales ---
    print("\n" + "=" * 30)
    # Volvemos a calcular los puntajes finales por si el As cambió de 11 a 1 
    # en la última jugada de la computadora o si el usuario hizo un cambio.
    puntaje_usuario = puntaje(cartas_usuario) 
    puntaje_computadora = puntaje(cartas_computadora)
    
    print(f"Tu mazo final es: {cartas_usuario}, puntaje final: {puntaje_usuario}")
    print(f"Mazo final de la computadora: {cartas_computadora}, puntaje final: {puntaje_computadora}")
    print(comparacion(puntaje_usuario, puntaje_computadora))
    print("=" * 30)

while input("¿Quieres jugar Blackjack? Teclea 's' o 'n': ").lower() == "s":
    os.system('cls' if os.name == 'nt' else 'clear') # Mejor manejo para Windows y Linux/Mac
    jugar()
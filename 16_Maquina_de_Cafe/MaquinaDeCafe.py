espresso = {
    "nombre": "Espresso",
    "agua": 50,
    "cafe": 18,
    "precio": 15
}

latte = {
    "nombre": "Latte",
    "agua": 200,
    "leche": 150,
    "cafe": 24,
    "precio": 25
}

cappuccino = {
    "nombre": "Cappuccino",
    "agua": 250,
    "leche": 100,
    "cafe": 24,
    "precio": 30
}

MENU = {
    "espresso": espresso,
    "latte": latte,
    "cappuccino": cappuccino
}

resources = {
    "agua": 300,
    "leche": 200,
    "cafe": 100,
    "dinero": 0
}

INGREDIENTES = ["agua", "leche", "cafe"]

def imprimir_reporte():
    print("\n--- REPORTE ---")
    print(f"Agua: {resources['agua']}ml")
    print(f"Leche: {resources['leche']}ml")
    print(f"Café: {resources['cafe']}g")
    print(f"Dinero: ${resources['dinero']}")

def verificar_recursos(tipo_cafe):
    for ingrediente in INGREDIENTES:
        if ingrediente in tipo_cafe:
            if tipo_cafe[ingrediente] > resources[ingrediente]:
                print(f"Lo siento, no hay suficiente {ingrediente}.")
                return False
    return True

def pedir_monedas():
    try:
        total = 0
        total += int(input("¿Cuántas monedas de 1 peso? ")) * 1
        total += int(input("¿Cuántas monedas de 2 pesos? ")) * 2
        total += int(input("¿Cuántas monedas de 5 pesos? ")) * 5
        total += int(input("¿Cuántas monedas de 10 pesos? ")) * 10
        return total
    except ValueError:
        print("Entrada inválida. Intenta de nuevo.")
        return None

def procesar_pago(tipo_cafe):
    print("\nPor favor, inserte monedas.")
    total = pedir_monedas()

    if total is None:
        return False

    if total < tipo_cafe["precio"]:
        print("Dinero insuficiente. Se devuelve el dinero.")
        return False
    else:
        cambio = total - tipo_cafe["precio"]
        if cambio > 0:
            print(f"Tu cambio es: ${cambio}")
        resources["dinero"] += tipo_cafe["precio"]
        return True

def hacer_cafe(tipo_cafe):
    if not verificar_recursos(tipo_cafe):
        return

    if not procesar_pago(tipo_cafe):
        return

    for ingrediente in INGREDIENTES:
        if ingrediente in tipo_cafe:
            resources[ingrediente] -= tipo_cafe[ingrediente]

    print(f"\n☕ Aquí tienes tu {tipo_cafe['nombre']}. ¡Disfrútalo!")

def main():
    print("☕ Máquina de café iniciada")
    
    while True:
        eleccion = input("\n¿Qué deseas? (espresso/latte/cappuccino/reporte/salir): ").lower()

        if eleccion == "salir":
            print("¡Hasta luego!")
            break
        elif eleccion == "reporte":
            imprimir_reporte()
        elif eleccion in MENU:
            hacer_cafe(MENU[eleccion])
        else:
            print("Opción no válida.")

# Llamar funcion main
main()
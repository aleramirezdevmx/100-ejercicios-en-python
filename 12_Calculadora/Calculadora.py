import os

logo = """
 _____________________
|  _________________  |
| | Pythonista      | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|

"""

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

operaciones = {
    "+":suma,
    "-":resta,
    "*":mult,
    "/":div
}
def calculadora():
    print(logo)
    acumulado=True
    a_1=float(input("Introduzca el primer número: "))
    while acumulado:
        for simbolo in operaciones:
            print(simbolo)
        operacion=input("¿Qué operación desea realizar? ")
        b_1=float(input("Introduzca el siguiente número:"))
        resultado= operaciones[operacion](a_1,b_1)
        print(f"{a_1} {operacion} {b_1}= {resultado}")

        eleccion=input(f"Escribe 's' para continuar calculando con {resultado} o teclea 'n' para empezar un nuevo calculo: ")

        if eleccion=="s":
            a_1=resultado

        else:
            acumulado=False
            os.system('cls')
            calculadora()

calculadora()
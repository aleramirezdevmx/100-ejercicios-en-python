"""
Ejercicio 14:
Programa para determinar si un número es primo, la salida será
True: Si es primo
False: Si no es primo
"""

count=0
while count==0:
    num1=int(input("¿qué número quieres revisar si es primo?"))

    def primo(num):
        #Caso especial para 2
        if num == 2:
            return True
        #Caso especial para 1
        if num == 1:
            return False
        #Ciclo para revisar número por número el posible primo
        for i in range(2, num):
            if num % i == 0:
                return False   
        return True

    print(primo(num1))
    count=int(input("\n¿Quieres revisar otro número? Teclea \n 0: Sí \n 1: No\n\n"))


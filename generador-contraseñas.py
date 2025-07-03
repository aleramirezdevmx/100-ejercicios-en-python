import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bienvenido al generador de contraseñas")
nr_letras= int(input("¿Cuántas letras quieres que tenga tu constraseña?\n")) 
nr_simbolos = int(input(f"¿Cuántos símbolos quieres que tenga tu contraseña?\n"))
nr_numeros= int(input(f"¿Cuántos números quieres que tenga tu contraseña?\n"))

lista_password=[]

for char in range(0,nr_letras):
    lista_password.append(random.choice(letras))

for char in range (0,nr_simbolos):
    lista_password.append(random.choice(simbolos))

for char in range(0,nr_numeros):
    lista_password.append(random.choice(numeros))

random.shuffle(lista_password)

password=""
for char in lista_password:
    password+=char

print(f"Tu contraseña es: {password}")



alfabeto = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
]

def cesar(mensaje_original,mov_numero,encriptacion):
    cifrado_cesar=""
    for letra in mensaje_original:
        if letra not in alfabeto:
            cifrado_cesar+=letra
        else:
            if encriptacion=='encriptar':
                cambio_pos=(alfabeto.index(letra)+mov_numero)%len(alfabeto)
            elif encriptacion=='desencriptar':
                cambio_pos=(alfabeto.index(letra)-mov_numero)%len(alfabeto)
            else:
                print("Introduce un proceso válido.")
            cifrado_cesar+=alfabeto[cambio_pos]
    
    print(f"Aquí tienes el resultado encriptado: {cifrado_cesar}.\n")


continuar=True

while continuar:

    direccion=input("Bienvenido al sistema de cifrado Cesar, desea 'encriptar' o 'desencriptar': \n")
    mensaje=input("Introduce el mensaje que deseas cifrar:\n").lower()
    mov=int(input("¿Cuántas posiciones desea mover el alfabeto?\n"))

    cesar(mensaje_original=mensaje,mov_numero=mov,encriptacion=direccion)

    estado=input("Teclee 's' si desea continuar o teclee 'N' si desea salir.\n").lower()
    if estado=="s":
        continuar=True
    elif estado=="n":
        continuar=False
    else:
        print("Ingrese una acción correcta")

CADENA="[name]"

with open("./Input/Names/invited_names.txt") as nombres_file:
    nombres=nombres_file.readlines()
    print(nombres)

with open("./Input/Letters/starting_letter.txt") as carta_file:
    contenido_carta=carta_file.read()
    for nombre in nombres:
        nuevo_nombre=nombre.strip()
        nueva_carta=contenido_carta.replace(CADENA,nuevo_nombre)
        print(nueva_carta)
        with open(f"./Output/ReadyToSend/carta_para_{nuevo_nombre}.txt", "w") as carta_completa:
            carta_completa.write(nueva_carta)

import random
animales = [
    "perro", "gato", "conejo", "leon", "tigre", "elefante", "jirafa", "oso", "lobo", "zorro",
    "caballo", "vaca", "cerdo", "oveja", "cabra", "gallina", "pato", "ganso", "pavo", "burro",
    "raton", "murcielago", "ardilla", "mapache", "nutria", "hipopotamo", "rinoceronte", "cebra", "mono", "gorila",
    "chimpance", "cocodrilo", "iguana", "camaleon", "serpiente", "tortuga", "pez", "delfin", "ballena", "tiburon",
    "calamar", "pulpo", "pingüino", "foca", "hamster", "koala", "canguro", "pantera", "halcon", "aguila"
]

ahorcado = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


seleccion=random.choice(animales)

for letra in seleccion :
    print("_",end="")
   

fin_juego=False
palabra=[]
vidas=6
while not fin_juego:
    
    letra_u=input("\nIngrese una letra: ").lower()
    adiv=""
    for letra in seleccion:
        if letra_u==letra:
            adiv+=letra
            palabra.append(letra_u)  
        elif letra in palabra:
            adiv+=letra
        else:
            adiv+="_"
            
    if letra_u not in seleccion:
        vidas-=1
        if vidas==0:
            fin_juego=True
            print("PERDISTE.")

    print(adiv)
    

    if "_" not in adiv:
        fin_juego=True
        print("GANASTE.")
    
    print(ahorcado[6-vidas])
   

        


    
      
 
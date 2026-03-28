import random
piedra='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

tijera="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

imagenes=[piedra, papel, tijera]

humano=int(input("¿Qué eliges? Escríbe 0 para piedra, 1 para papel o 2 para tijeras\n"))
if humano>=0 and humano<=2:
    print(f"Elección de usuario{imagenes[humano]}\n")

computadora=random.randint(0,2)
print(f"Elección de computadora{imagenes[computadora]}\n")

if humano>=3 or humano<0:
    print("Escribe un número correcto")
elif humano==computadora:
    print("Empate")
elif computadora==0 and humano==2:
    print("Perdiste")
elif humano>computadora:
    print("Ganaste")
elif humano==0 and computadora==2:
    print("Ganaste")
elif computadora>humano:
    print("Perdiste")

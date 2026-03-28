print("Bienvenido a La Pizzeria")
tamaño=input("¿Qué tamaño de pizza desea ordenar? C, M, o G:")
extra_pepperoni=input("¿Desea agregar extra pepperoni? S o N:")
extra_queso=input("¿Desea agregar queso extra? S o N:")
cuenta=0
if tamaño== "C":
    cuenta+=15
elif tamaño =="M":
    cuenta+=20
elif tamaño =="G":
    cuenta+=25
else:
    print("Selecciona un tamaño correcto")

if extra_pepperoni=="S":
    if tamaño=="C":
        cuenta+=2
    else:
        cuenta+=3
if extra_queso=="S":
        cuenta=+1

print(f"El costo de tu pizza es: ${cuenta}.")


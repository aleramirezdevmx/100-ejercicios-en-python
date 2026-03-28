entrada=input("¿Qué año quieres revisar si es bisiesto?: ")
year=int(entrada)

def bisiesto(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

a_bisiesto=bisiesto(year)

print(f"¿Es {year} un año bisiesto? : {a_bisiesto}")

#Mensaje de bienvenida con función print()
print("Bienvenido a la calculadora de cuenta y propinas")

#Asignación de variables, conversión de variables mediante casting, uso de función round() e input()
cuenta = round(float(input("¿Cuál es el valor de la cuenta sin propina?")),2)
porcentaje=round(float(input("¿Qué porcentaje de propina deseas dejar?")),2)
comensales=int(input("¿Entre cuantas personas van a dividir la cuenta?"))

#Uso de operaciones aritméticas para calcular total a pagar por persona
total_cabeza=round((cuenta*(1+porcentaje/100))/comensales,2)

#Impresión del total a pagar por persona
print("Cada persona debe pagar: $" + str(total_cabeza))

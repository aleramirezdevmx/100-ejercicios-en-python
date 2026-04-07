from tkinter import *

def millas_km():
    millas=float(millas_entrada.get())
    km=round(millas*1.609,2)
    km_resultado.config(text=f"{km}")

window = Tk()
window.title("Millas a Kilometros")
window.config(padx=20,pady=20)

millas_entrada = Entry(width=7)
millas_entrada.grid(column=1,row=0)

millas_etiqueta = Label(text="Millas")
millas_etiqueta.grid(column=2,row=0)

etiqueta_igual = Label(text="es igual a: ")
etiqueta_igual.grid(column=0,row=1)

km_resultado = Label(text="0")
km_resultado.grid(column=1,row=1)

km_etiqueta = Label (text="km")
km_etiqueta.grid(column=2,row=1)

calcular = Button(text="Calcular", command=millas_km)
calcular.grid(column=1,row=2)

window.mainloop()
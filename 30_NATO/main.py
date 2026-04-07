import pandas
import csv


data=pandas.read_csv("nato.csv")
diccionario={row.letter:row.code for (index, row) in data.iterrows()}


palabra=input("Introduce una palabra: ").upper()

lista= [diccionario[letra] for letra in palabra]
print (lista)



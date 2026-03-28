from prettytable import PrettyTable
table = PrettyTable(padding_width=5)

table.add_column("Nombre del Pokemón",["Pikachu","Charizard","Bulbasaur","Squirtle","Gengar","Eevee","Lugia","Ho-Oh","Blaziken","Gardevoir","Rayquaza","Lucario","Garchomp","Darkrai","Zoroark","Reshiram","Greninja","Sylveon","Decidueye","Mimikyu","Incineroar","Corviknight","Dragapult","Toxtricity","Sprigatito","Fuecoco","Quaxly"])

table.add_column("Tipo de Pokemón",["Eléctrico","Fuego / Volador","Planta / Veneno","Agua","Fantasma / Veneno","Normal","Psíquico / Volador","Fuego / Volador","Fuego / Lucha","Psíquico / Hada","Dragón / Volador","Lucha / Acero","Dragón / Tierra","Siniestro","Siniestro","Dragón / Fuego","Agua / Siniestro","Hada","Planta / Fantasma","Fantasma / Hada","Fuego / Siniestro","Volador / Acero","Dragón / Fantasma","Eléctrico / Veneno","Planta","Fuego","Agua"])

table.add_column("Generación",["Kanto","Kanto","Kanto","Kanto","Kanto","Kanto","Johto","Johto","Hoenn","Hoenn","Hoenn","Sinnoh","Sinnoh","Sinnoh","Unova","Unova","Kalos","Kalos","Alola","Alola","Alola","Galar","Galar","Galar","Paldea","Paldea","Paldea"])

print(table)
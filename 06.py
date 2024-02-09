# Desempaquetado de tuplas con el ciclo for

tuple = ("001", "Manzana", "rojo"),("002", "Pera", "verde")

for code, fruit, color in tuple:
    print(f"La {fruit}  tiene el codigo {code} y es de color {color}")

fruits_tuple = ("001", "Manzana", "rojo"), ("002", "Pera", "verde"), ("003", "Naranja", "naranaja")
print(fruits_tuple, "\n")

for code, fruit, color in fruits_tuple:
    print(f"La {fruit} tien el codigo {code} y es de color {color}")


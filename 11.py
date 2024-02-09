# Ejercicio practico

names_tupla = ("Ana", "Maria", "Carlos", "Valentina")

print(names_tupla, "\n")
validator = 0
while validator==0:
    number = int(input("Introduce un numero entre 0 y 4: "))
    if 0 <= number <= 4:
        print(f"El nombre es {names_tupla[number]}")
        validator=1
    else:
        print("¡Error!: Numero invalido, vuelve a intentar. \n")
        

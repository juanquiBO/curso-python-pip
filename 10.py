# Ejercicio practico

Tupla_original=(5,8,3,3,1,6,2)

print(f"Tupla Original: {Tupla_original} \n")

num = int(input("¿Cual de estos numeros quieres modificar por 0?: "))

Tupla_original=list(Tupla_original)

len_tuple= len(Tupla_original)

for index in range(len_tuple):
    if Tupla_original[index] == num:
        Tupla_original[index] = 0

Tupla_original=tuple(Tupla_original)

print(f" \n Tupla modificada: {Tupla_original}")


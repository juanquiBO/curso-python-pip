# Concatenacion de tuplas

tupla1 = (1,2,3)
tupla2=(4,5,6)

tupla_concatenada = tupla1 + tupla2

print(tupla_concatenada)

tupla_concatenada2 = tupla2 + tupla1

print(tupla_concatenada2)

tupla1 += tupla2

print(tupla1)

tupla3 = (1,2,3)
lista = [4,5,6]

tupla_concatenada = tupla3+tuple(lista)

print(tupla_concatenada)

print("****** Usnado el operador + *******")
tupla1 = (1,2,3)
tupla2=(4,5,6)

print(f"tupla 1: {tupla1} | tupla 2: {tupla2}")
tupla_concatenada = tupla1+tupla2
print(tupla_concatenada, "\n")

print("****** Usnado el operador += *******")
tupla1 = (1,2,3)
tupla2=(4,5,6)

print(f"tupla 1: {tupla1} | tupla 2: {tupla2}")
tupla1+=tupla2
print("Tupla 1", tupla1, "\n")


print("****** Usnado el operador tuple() *******")
tupla1 = (1,2,3)
lista=[4,5,6]

print(f"tupla 1: {tupla1} | tupla 2: {tupla2}")
tupla_concatenada = tupla1+tuple(lista)
print("Tupla concatenada", tupla_concatenada, "\n")


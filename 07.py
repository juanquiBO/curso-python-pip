# La funcion tuple

#tuple (objeto_iterable)

# Solo se puede trabajar con un solo argumento

# Emplo 1 - crear una coordenada con tuple()
x=10
y=5
coordenada = tuple([x, y])
print(coordenada)

# Ejemplo 2 - convertir un String a tupla
print("****** Ejemplo #2 ****** \n")
string = input("Introduce un String: ")
texto = "Hola"

tupla_de_string = tuple(string)
print(tupla_de_string)

# # Ejemplo 3 - convertir un String a tupla
print("****** Ejemplo #3 ****** \n")
numbers_dict = {
                "uno": 1,
                "dos": 2,
                "tres": 3
}
print(numbers_dict, "\n")
tupla_claves = tuple(numbers_dict)
print(tupla_claves)

# # Ejemplo 4 - convertir un diccionario a tupla (valores)
print("****** Ejemplo #4 ****** \n")
numbers_dict = {
                "uno": 1,
                "dos": 2,
                "tres": 3
}
print(numbers_dict, "\n")
numbers_tuple = tuple(numbers_dict.values())
print(f"La tupla es: {numbers_tuple} \n")

# # Ejemplo 5 - convertir un diccionario a tupla (items)
print("****** Ejemplo #4 ****** \n")
numbers_dict = {
                "uno": 1,
                "dos": 2,
                "tres": 3
}
print(numbers_dict, "\n")
numbers_tuple = tuple(numbers_dict.items())
print(f"La tupla es: {numbers_tuple} \n")
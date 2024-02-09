# Elementos de segmentacion

# nombre_tupla[inicio: final : saltos]

tupla_vocales = ("a", "e", "i", "o", "u")

#tupla_vocales[0:2]

#tupla_vocales[::2]

#tupla_vocales[0:4:2]

print(f"{tupla_vocales[0:5:2]}")

print(f"{tupla_vocales[::2]}")

print(f"{tupla_vocales[-3]}")

# Acceder a los elementos de una tupla mediante el operador de segmentacion

vowels_tuple = ("a", "e", "i", "o", "u")

print(vowels_tuple, "\n")

print(f"Posiciones[0:2] -> {tupla_vocales[0:2]}")

print(f"Posiciones[::2] -> {tupla_vocales[::2]}")

print(f"Posiciones[-3:] -> {tupla_vocales[-3:]}")




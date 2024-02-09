# la funcion ZIP

# zip(objeto_iterable, objeto_iterable, ...)

names = ("Luis", "Diego", "Andres", "Carlos")

eges = [15, 30, 26, 12, 40]

combination1= zip(names, eges)
print(combination1)

combination = list(zip(names, eges))
print(combination)

for name, age in zip(names, eges):
    print(name, age)


names = ("Luis", "Diego", "Andres", "Carlos")
eges = [15, 30, 26, 12, 40]
text = "JuanCarlos"

print(names)
print(eges)
print(text)

print("\n Funcion zip() como iterable: \n")
combination = zip(names, eges, text)
print(combination)

print("\n Funcion zip() con la funcion list(): \n")
combination = list(zip(names, eges, text))
print(combination)

print("\n Funcion zip() con la funcion tuple(): \n")
combination = tuple(zip(names, eges, text))
print(combination)

print("\n Funcion zip() con for: \n")

for name, ege, s_text in zip(names, eges, text):
    print(name, ege, s_text)






# Subconjuntos ussubset()

conjunto_a = {1,2,3,4,5}
conjunto_b = {1,2,3,4,5}

# Conjunto b es subconjunto del conjunto a?

z=conjunto_b.issubset(conjunto_a)

print(z)

y=conjunto_a.issubset(conjunto_b)

#print(y)

p = conjunto_b

es_subconjunto = conjunto_b <= conjunto_a
print("Utilizando el operador <= :", es_subconjunto)

es_subconjunto = conjunto_b < conjunto_a
print("Utilizando el operador < :", es_subconjunto)
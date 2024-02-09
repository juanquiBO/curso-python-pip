# conjuntos la funcion set()

conjunto = {}
conjunto1 = {1, "e", 9, "t"}

#conjunto2 = set(objeto_iterable)

conjunto = {5,1,3,2,4}

print(conjunto)

print("Conjuntos creados con llaves {} \n")

print("Ejemplo #1 {5,1,3,2,4}" )
print(conjunto)

conjunto2 ={-1,0, 5, -2, -1, 4}
print("Ejemplo #2 {-1,0, 5, -2, -1, 4}")
print(conjunto2)

conjunto3={"e", "o", "a", "u", "i"}
print("Ejemplo #3 {'e', 'o', 'a', 'u', 'i'}")
print(conjunto3)

conjunto4={"e", 5, "o", "0", "a", 2, -1}
print("Ejemplo #3 {e, 5, o, 0, a, 2, -1}")
print(conjunto4)

# Python elimina duplicados
conjunto5={5, 1, 1, 1, 3, 5}
print("Ejemplo #5 {5, 1, 1, 1, 3, 5}")
print(conjunto5)

# conjunto6 = {5, [3,2,4], 1,0,6}
# print(conjunto6)

list = ["e", 5, "o", "0", "a", 2, -1]
conjunto = set(list)
print(conjunto)

conjunto = set("Hola")
print(conjunto)


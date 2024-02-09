# Ejercicio 19

datos_tuple= (("Eduardo",26), ("Maria",30),("Gerardo",20),("Valentina",22))
print(datos_tuple)
datos_lista=list(datos_tuple)
print(datos_lista)

longitud_lista = len(datos_lista)

for i in range(longitud_lista):
    for j in range(i+1, longitud_lista):
        if datos_lista[i][1]>datos_lista[j][1]:
            aux=datos_lista[i]
            datos_lista[i], datos_lista[j]=datos_lista[j], aux
print(datos_lista)
print(f"La persona de menor edad es: {datos_lista[0]}") 
print(f"La persona de mayor edad es: {datos_lista[-1]}") 
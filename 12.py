# ejercicio practico #18

tupla1 = (1,2,3,4,5)
tupla2 = (8,6,7,8,9)

ad_tuples =[]

for x, y in zip(tupla1, tupla2):
    ad_tuples.append(x+y)

print("Tupla 1:". ljust(13), tupla1)
print("".ljust(14) + "+")
print("Tupla 2:". ljust(13), tupla2)
print("".ljust(14) + "===================")
print("Suma:". ljust(13), tuple(ad_tuples))

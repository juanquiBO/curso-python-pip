# El metodo issuperset()
# Un superconjunto contine todos los elementos del otro elemento

A= {1,2,3,4,5}
B={1,2,3,4,5}

print(f"Conjunto A: {A} \n Conjunto B: {B}\n")
print("¿A es superconjunto de b? \n")

z=A.issuperset(B)
print(z)

x=A >= B
print(x)

y=A > B
print(y)


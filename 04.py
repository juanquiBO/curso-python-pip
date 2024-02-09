# Inmutabilidad de las tuplas
nums_tuple = (1,2,3,4,5)

print(nums_tuple)

info_tuple = ([1,2,3], {"uno": 1, "dos": 2}, (3, 2))

info_tuple[0][1]=99

print(info_tuple)

info_tuple[1]["dos"]=88

print(info_tuple)
"""
#nums_tuple[0] = 5
"""



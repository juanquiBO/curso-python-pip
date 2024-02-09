def increment(x):
  return x+1

def hig_ord_func(x, func):
  return x + func(x)

result = hig_ord_func(2, increment)

print(result)


increment_v2=lambda x:x+1

hig_ord_func_v2= lambda x, fuc: x+fuc(x)

result_v2 = hig_ord_func_v2(2, increment)
print(result)

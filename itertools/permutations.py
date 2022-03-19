from itertools import permutations, product

a = [1,2]
b = [3]
prod = product(a,b)
print(list(prod))

x = [1,2,3]
perm = permutations(x)
print(list(perm))

c = [x for x in range(5) if x%2 !=0 ]
print(c)
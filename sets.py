odds = {1,3,5,7,9}
evens = {1,2,4,6,8}
primes = {2,3,5}

u = odds.union(evens)
print(u) # it will not print the elements which is there is both the list

i = odds.intersection(evens)
print(i) # it its found the samee elements then it will print
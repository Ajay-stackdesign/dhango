from collections import OrderedDict 

oD = {}

oD["a"] = 1
oD["b"] = 2
oD["c"] = 3
oD["d"] = 4
print(oD)

outside = OrderedDict()

outside["e"] = 1
outside["f"] = 2
outside["g"] = 3
outside["h"] = 4
print(outside)


# important point: 
# if the value of the element changes its key value remained unchanged

inside = {}

inside["x"] = 1 
inside["y"] = 2
inside["z"] = 3
for key,value in inside.items():
    print(key,value)

inside["y"] = 4

for key,value in inside.items():
    print(key,value)

print(inside)
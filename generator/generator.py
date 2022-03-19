def show(a,b):
    while a <= b:
        yield a
        a +=1

result = show(1,5)
# print(result)  

print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
# # print(next(result))
# print(type(result))
# print(result)
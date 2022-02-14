# def fact(num):
#     if num == 1:
#         return num
#     else:
#         result = num * fact (num -1)
#         return result
#         # print(num * fact(num -1))
#
# number = 5
#
# factor = fact(number)
# print(factor)
#
#
#
# arraay = [2,2,3,4]
#
# print(arraay[::-1])
#
#
# print alternate elements of an arrat:

def alternate(arr):
    output = []

    for i in range(1,len(arr)+1):
        if  arr[i] % 2 == 0:
            output.append(i)
        return output

a = [1,2,3,4,5]
result = alternate(a)
print(result)



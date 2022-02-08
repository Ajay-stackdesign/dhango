def fact(num):
    if num == 1:
        return num
    else:
        result = num * fact (num -1)
        return result
        # print(num * fact(num -1))

number = 5
factor = fact(number)
print(factor)




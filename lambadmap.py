# # lambda map filter reduce


# from typing import final


# x = lambda a: a + 10;
# print(x(10))

# def x(a):
#     print(a+10)

# x(10)

# y = lambda x,z: x+z

# print(y(10,10))

# #differnce between def() and lambda()

# # using def function
# def y(a):
#     return a*a;

# print(y(20))

# # using lambda function

# x = lambda y : y*y ; 
# print(x(10))

# # li = [x for x in range(10) if x%2 == 0]

# # print(li)

# # example1 : python lambda fiunction with list comprehension;


# max = lambda x , y : "ajay" if(x > y) else "sahani"

# print(max(10,12))

# # Using lambda() function with filter():

# '''the filter function in pyhon takes in a function and list as argumnets
# this offers an elegant way to filter out all the elemnts of a sequence "sequence",
# for whih the function returns true. here is a small program'''

# li = [1,2,3,4,5,6,7]

# final_list = list(filter(lambda x: (x%2 !=0), li))
# print(final_list)

# lis = [2,3,4,5]

# final_lis = list(map(lambda x: (x%2 == 0), lis))

# print(final_lis)

# from functools import reduce

# l1 = [1,2,3,4,5]
# sum = reduce((lambda x,y : x+y),l1)
# print(sum)

from functools import reduce


l3 = [ 1,2,3,4,5]

sum1  = list(map(lambda x: (x == 2) ,l3))
print(sum1)


animals = ["cat","dog"]
sum3 = list(map(lambda x: str.upper(x),animals))
print(sum3)


snakes = ["anaconda","indian rock python"]
snake = list(map(lambda ani : str.lower(ani),snakes))
print(snake)




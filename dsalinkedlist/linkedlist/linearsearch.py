#
#  #  linear search problems data structure
#
# # input = [2,3,4,5,10,2];
# #
# # query = 10;
# # n = len(input);
#
# def linearSearch( arr , n , x ):
#
#     for i in range(0, n):
#         if(arr[i] == x):
#             return i
#     return -1;
#
# arr = [2,3,4,5,10,2];
# n = len(arr)
# x = 10
#
# result = linearSearch(arr,n,x)
# if(result == -1):
#     print("x is not preesend in the arr")
# else:
#     print("x is present in the arr")
#
#
# # but this is the worst case as we have to move to the every point in the list
#
# def linearSearching(list, j , p):
#     for x in range(0, j):
#         if(list[x] == p):
#             return i;
#     return -1;
#
# list = [2,3,4,5,10,2];
# j = len(arr)
# p = 10
#
# result = linearSearching(list,j,p)
# if(result == -1):
#     print("x is not preesend in the arr")
# else:
#     print("x is present in the arr")
#


def linearSearch(arr, n, query):

    for x in range(0,n):
        if(arr[x] == query):
            return x;
    return -1

arr = [10,50,30,70,80,60,20,90,40]
n = len(arr)
query = 20

result = linearSearch(arr,n,query)
if(result == query):
    print("value is present")
else:
    print("value is not present")

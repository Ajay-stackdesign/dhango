
#  finding the element:

def linear__search(arr, n , query):

    for i in range (0,n):
        if (arr[i] == query):
            return i
    return -1;

arr = [10,14,19,26,27,31,33,35,42,44]
n = len(arr)
query = 33

result = linear__search(arr,n,query)
if(result == -1):
    print("query is not present")
else:
    print("query is present")


def search(list, l, answer):

    for x in range(0, length):
        if(list[x] == answer):
            return x;
    return -1

list [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18];
l = len(list)
answer = 11

res = search(list, l, answer)
if(res == -1):
    print("answer is not found")
else:
    print("answer is found")
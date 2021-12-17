
 #  linear search problems data structure

# input = [2,3,4,5,10,2];
#
# query = 10;
# n = len(input);

def linearSearch( arr , n , x ):

    for i in range(0, n):
        if(arr[i] == x):
            return i
    return -1;

arr = [2,3,4,5,10,2];
n = len(arr)
x = 10

result = linearSearch(arr,n,x)
if(result == -1):
    print("x is not preesend in the arr")
else:
    print("x is present in the arr")


# but this is the worst case as we have to move to the every point in the list



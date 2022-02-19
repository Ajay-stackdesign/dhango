def countOfElements( a, n, x):
    count = 0
    for i in range(0, n):
        if a[i] <=x:
            count+=1
    return count
arr = [1,2,2,2,3]
n = len(arr)
result = countOfElements(arr, n, 2)
print(result)

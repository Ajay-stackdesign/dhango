def migratoryBirds(arr):
    count = 0
    for i in range(0, len(arr)):
        for j in range(0+1, len(arr)-2):
            if arr[i] == arr[j]:
                count +=1
                result  = arr[i]
    return result


arr = [1,4,4,4,5,3]
result = migratoryBirds(arr)
print(result)









arr = [1,4,4,4,5,3]
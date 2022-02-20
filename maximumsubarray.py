def maximum(arr, n):
    array = []
    sum = 0

    for i in range(0, n):
        for j in range(1, n):
            if arr[i] < arr[j] and arr[i] <= arr[j]:
                array.append(i)
                sum += 0
                # arr[i] = arr[i+1]
                # arr[j] = arr[j+1]
            else:
                break
    return array

arr = [1,2,3]
n =3
result = maximum(arr, n)
print(result)
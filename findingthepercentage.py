def finding(arr):
    length = len(arr)
    sum = 0
    for i in range(0, len(arr)):
        sum += arr[i]
        summing = (sum / 3)
        # summing.toFixed(2)
    return summing

arr = [ 25, 26.5, 28]
result = finding(arr)
print(result)
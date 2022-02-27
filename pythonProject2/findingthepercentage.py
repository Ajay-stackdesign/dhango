# def finding(arr):
#     length = len(arr)
#     sum = 0
#     for i in range(0, len(arr)):
#         sum += arr[i]
#         summing = (sum / 3)
#         # summing.toFixed(2)
#     return summing
#
# arr = [ 25, 26.5, 28]
# result = finding(arr)
# print(result)



def getMinMax(a, n):
    for i in range(0, n):
        if a:
            return max(a)
        else:
            return 1


a = [{1, 2, 3, 4, 5}]

n = 5
result = getMinMax(a,n)
print(result)


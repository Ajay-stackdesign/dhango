def sub( array, n):
    i = array[0]
    j = array[1]
    k = array[-1]

    # length = len(n)

    for i in range(0, n):
        for j in range(1,n):
            for k in range(0,n):
                if array[0] < array[1] and array[1] < array[-1]:
                    return 1
                else:
                    return 0
# arr = [1,2,1,1,3]
# arr=[1,2,1,1,2,1,2,3]
arr = [1,2,1,2,1,1,2,1,23,122,1]
result = sub(arr,5)
print(result)
# # arr = [1,1,2]


# def sub(arr, n):
#     i = arr[0]
#     j = arr[1]
#     for i in range(0, n):
#         if arr[i] >= arr[j]:
#             return 0
#         elif arr[i] < arr[j]:
#             return 1
#         else:
#             return "undefined"
#
# arr = [1,2,1,1,2,3]
# n = 6
#
# result = sub(arr, n)
# print(result)
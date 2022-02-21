def binarySearch(nums, target):
    lo = 0
    li = len(nums) - 1
    while lo <= li:
        mid = lo + li // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return mid + 1
        elif nums[mid] > target:
            return mid - 1
    return -1
nums = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 38
result = binarySearch(nums, target)
print(result)
# def binarySearch(arr, l, r, x):
#     # Check base case
#     if r >= l:
#
#         mid = l + (r - l) // 2
#
#         # If element is present at the middle itself
#         if arr[mid] == x:
#             return mid
#
#         # If element is smaller than mid, then it
#         # can only be present in left subarray
#         elif arr[mid] > x:
#             return binarySearch(arr, l, mid - 1, x)
#
#         # Else the element can only be present
#         # in right subarray
#         else:
#             return binarySearch(arr, mid + 1, r, x)
#
#     else:
#         # Element is not present in the array
#         return -1
#
# # Driver Code
# arr = [2, 3, 4, 10, 40, 50, 60]
# x = 4
#
# # Function call
# result = binarySearch(arr, 0, len(arr) - 1, x)
#
# if result != -1:
#     print("Element is present at index % d" % result)
# else:
#     print("Element is not present in array")

# algorithm for this code:

def binary_Search(arr, query):
    lo = 0
    li = len(arr) - 1

    while lo <= li:
#         mid = len(arr) // 2
#
#         if arr[mid] == query:
#             return mid
#
#         elif arr[mid] < query:
#             return mid+1
#         elif arr[mid] > query:
#             return mid-1
#         return -1
#
# arr = [2,3,4,5,6,7,9]
# query = 4
#
# result = binary_Search(arr,query)
# print(result)
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return
#
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr [mid:]
#
#     merge_sort(left)
#     merge_sort(right)
#
#     merge_sort_list(left, right, arr)
#     # binar_search(arr, )
#
# def merge_sort_list(a, b, arr):
#     lena = len(a)
#     lenb = len(b)
#
#     i = j = k = 0
#
#     while i < lena and j < lenb:
#         if a[i] <= b[j]:
#             arr[k] = a[i]
#             i+=1
#         else:
#             arr[k] = b[j]
#             j+=1
#         k+=1
#
#     while i < lena:
#         arr[k] = a[i]
#         i+=1
#         k+=1
#
#     while j < lenb:
#         arr[k] = b[j]
#         j+=1
#         k+=1

def binar_search(arr , query):
    lo = 0
    li = len(arr) - 1

    while lo <= li:
        mid = len(arr) // 2

        if arr[mid] == query:
            return mid
        elif arr[mid] < query:
            return mid -1
        elif arr[mid] > query:
            return mid+1
        return -1



if __name__ == '__main__':
    arr = [1,3,2]
    merge_sort(arr)
    print(binar_search(arr,2))
    print(arr)




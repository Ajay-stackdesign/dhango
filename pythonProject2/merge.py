def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists(a,b,arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1

    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1

if __name__ == '__main__':
    test_cases = [
        # [10, 3, 15, 7, 8, 23, 98, 29],
        # [],
        # [3],
        # [9,8,7,2],
        # [1,2,3,4,5]
        [5,2,3,1],
        [5, 1, 1, 2, 0, 0],
    ]
    # # arr = [10, 3, 15, 7, 8, 23, 98, 29]
    #
    for arr in test_cases:
    # arr = [314,6,329, 16,20,90,80,550]
        merge_sort(arr)
        print(arr)


# def merge_sort(nums):
#     if len(nums) <= 1:
#         return
#
#     mid = len(nums) // 2
#     left = nums[:mid]
#     right = nums[mid:]
#
#     merge_sort(left)
#     merge_sort(right)
#
#     lenA = len(left)
#     lenB = len(right)
#     i = j = k = 0
#
#     while i < lenA and j < lenB:
#         if left[i] <= right[j]:
#             nums[k] = left[i]
#             i += 1
#
#         else:
#             nums[k] = right[j]
#             j += 1
#         k += 1
#
#     while i < len(left):
#         nums[k] = left[i]
#         i += 1
#         k += 1
#     while j < len(right):
#         nums[k] = right[j]
#         j += 1
#         k += 1
#
# if __name__ =='__main__':
#     # input = [
#     #     [5, 2, 3, 1],
#     #     [5, 1, 1, 2, 0, 0],
#     # ],
#     #
#     # for nums in input:
#     nums = [5,2,4,1]
#     merge_sort(nums)
#     print(nums)
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
#
# def binar_search(arr, query):
#     lo = 0
#     li = len(arr) - 1
#
#     while lo <= li:
#         mid = len(arr) // 2
#
#         if arr[mid] == query:
#             return mid
#         elif arr[mid] > query:
#             return mid - 1
#         elif arr[mid] < query:
#             return mid+1
#         return -1
#
#
#
# if __name__ == '__main__':
#     arr = [1,3,2]
#     merge_sort(arr)
#     print(binar_search(arr, 2.5000))
#     print(arr)

# def mutate_string(string,position, character):
#     string.replace(position[5], character)
#     return string
#
#
# if __name__ == '__main__':
#     # s = input()
#     s= 'abracadabra'
#     index = 5
#     c = 'k'
#     s_new = mutate_string(s,index, c)
#     print(s_new)

# def mutate_string(string, position, character):
#     lis=list(string)
#     lis[position]=character
#     return ''.join(lis)
#
# if __name__ == '__main__':
#     s = 'abracadabra'
#     c = 'k'
#     index = [5]
#     s_new = mutate_string(s, index, c)
#     print(s_new)

# def swap_case(s):
#     string = s.swapcase()
#     return string
#
# if __name__ == '__main__':
#     s = 'HackerRank.com presents "Pythonist 2"'
#     result = swap_case(s)
#     print(result)
# def print_full_name(first, last):
#     # Write your code here
#     print("hello", first, last, "! you have delved into python")
# if __name__ == '__main__':
#     first_name = 'Ross'
#     last_name = 'Taylor'
#     print_full_name(first_name, last_name)
# def print_full_name(first, last):
#     # Write your code here
#     print("hello", first, last ,"! you have delved into python")
# if __name__ == '__main__':
#     first_name = "python"
#     last_name = "developer"
#     print_full_name(first_name, last_name)


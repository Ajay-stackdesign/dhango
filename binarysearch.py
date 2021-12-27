def binarySearch(nums, target):
    lo = 0
    li = len(nums) - 1

    while lo <= li:
        mid = lo + li // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return mid - 1
        elif nums[mid] > target:
            return mid + 1
        return -1


nums = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

result = binarySearch(nums, target)

if result == -1:
    print("target is not found")
else:
    print("target is found")

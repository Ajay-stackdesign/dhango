def mergeSort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left)
    mergeSort(right)
    merge_sort_list(left,right,arr)

def merge_sort_list(a,b,arr):
    lenA = len(a)
    lenB = len(b)
    i = j = k = 0

    while i < lenA and j < lenB :
        if a[i] <= b[j]:
            a[k] = a[i]
            i +=1
        else:
            a[k] = a[j]
            j +=1
        k +=1

    while i< lenA:
        a[k] = a[i]
        i +=1
        k +=1

    while j < lenB :
        a[k] = a[j]
        j +=1
        k +=1

if __name__ == '__main__':
    arr = [21,23,4,2,3,5,3,4]
    mergeSort(arr)
    print(arr)


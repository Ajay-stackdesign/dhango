def mergeSort(a,b):
    sorted_list = []
    lena = len(a)
    lenb = len(b)
    i = j = 0

    while i < lena and j < lenb:
        if a[i] <= a[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(a[j])
            j+=1
    return sorted_list

if __name__ == '__main__':
    a = [23, 12, 32, 15]
    b = [7,9,45,51]
    print(mergeSort(a, b))

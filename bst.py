# element = []
# element.append(4)
# element.append(5)
# element.pop()
# print(element)

# def bubble_sort(element):
#     size = len(element)
#     for i in range(size-1):
#         swapped = False;
#         for j in range(size-1-i):
#             if element[j] > element[j+1]:
#                 temp = element[j]
#                 element[j] = element[j+1]
#                 element[j+1] = temp
#                 swapped = True
#         if not swapped:
#             break
# if __name__ =='__main__':
#     elements = [34,2,3,4,33,2,53]
#     bubble_sort(elements)
#     print(elements)

# def bubble_sort(elements):
#     size = len(elements)
#
#     for i in range(size-1):
#         swapped = False
#         for j in range(size-1-i):
#             if elements[j] > elements[j+1]:
#                 temp = elements[j]
#                 elements[j] = elements[j+1]
#                 elements[j+1] = temp
#                 swapper = True
#
#             if elements[j] == 2:
#                 print(elements[j])
#         if not swapped:
#             break
#
# if __name__ == '__main__':
#     elements = [1, 3, 2, 5, 4]
#     bubble_sort(elements)

def countSwaps(a):
    size = len(a)
    for i in range(size - 1):
        swapped = 0;
        for j in range(size - 1 - i):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                swapped += 1
    print("Array is sorted in", swapped, "swaps.")
    
    print("First Element:", a[0])
    print("Last Element:", a[-1])
if __name__ == '__main__':
    # a = [1, 2, 3]
    a = [3, 2, 1]
    countSwaps(a)
    # countSwaps(b)



def insertion_sort(elements):
    for i in range(1, len(elements)):
        # print(i)
        anchor = elements[i]
        # print(anchor)
        j = i - 1
        # print(j)
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            # print(elements[j+1])
            j = j - 1
            print(j)
        elements[j+1] = anchor
        # print(elements[j + 1])

if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    insertion_sort(elements)
    # print(elements)
    #
    # tests = [
    #     [11,9,29,7,2,15,28],
    #     [3, 7, 9, 11],
    #     [25, 22, 21, 10],
    #     [29, 15, 28],
    #     [],
    #     [6]
    # ]
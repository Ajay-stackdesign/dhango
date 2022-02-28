def maxIndexDiff(N,A):
    for i in range(0, N):
        for j in range(1,N):
            if A[i] < A[j]:
                j = j-i
            elif a[1] < a[7]:
                j = j-i
            else:
                return -1
    print(j)

a = [34, 8, 10, 3, 2, 80, 30, 33, 1]
maxIndexDiff(9, a)
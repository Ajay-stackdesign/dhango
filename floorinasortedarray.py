def findFloor(A, N, X):
    # Your code here
    c = -1
    for i in range(N):
        if A[i] > X:
            return c
        else:
            c = i
            # print(i)
    return c

A = [1,2,8,10,11,12,19]
N = 7
X = 5
result = findFloor(A, N, X)
print(result)


l = "chris alan"
print(l.capitalize())
def divisibleSumPairs(n, k, ar):
    # Write your code here
    count = 1
    for i in range(0, len(ar)):
        for j in range(0+i, len(ar)):
            if (ar[i] + ar[j] % k) == 0:
                count+=1
                
    return count

n = 6
k = 3
ar=[1, 3, 2, 6, 1, 2 ]

result = divisibleSumPairs(n,k,ar)
print(result)

def isAnagram(self, a, b):
    # code here
    if len(a) != len(b):
        return False
    d = {}
    for i in list(a):
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    e = {}
    for i in list(b):
        if i in e:
            e[i] += 1
        else:
            e[i] = 1
    return e == d
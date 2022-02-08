num = 200
s = 0
temp = num

while temp > 0 :
    c = temp % 10
    s = s + c**3
    temp = temp // 10
if num == s:
    print("armstrong number")
else:
    print("not a number")

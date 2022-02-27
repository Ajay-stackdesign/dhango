# i = 525
#
# rev = 0
# x = i
#
# while (i>0):
#     rev = (rev*10) + i % 10
#     i = i // 10
#
# if(x == rev):
#     print("number is palindrome")
# else:
#     print("nnumber is not palindrome")

def pal(num):
    number = num[::-1]
    if number == num :
        print("palindrome number")
    else:
        print("not a palindrome")


num = "madam"
pal(num)
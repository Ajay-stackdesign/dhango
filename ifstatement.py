def max_num(num1,num2,num3) :
    if num1 >= num2 and num1 >= num3 :
        return "num1 is maximum" ;
    elif num2 >= num1 and num2 >= num3 :
        return "num2 is greater";
    else :
        return "num3 is greater";

greater = max_num(10,20,40)
print(greater)

is_male = True;
is_female = False

if is_male or is_female :
    print("he is neither men nor women")
else:
    print("he is something else")


num4 = float(input("enter the number"));
op = input("enter the operator")
num5 = float(input("enter the number"))

if op == "+" :
    print(num4 + num5);
elif op == "-" :
    print(num4 - num5);
elif op == "*" :
    print(num4 * num5);
elif op == "/" :
    print(num4 / num5);
else :
    print("enter a valid operator")

    



monthConversion = {
    "id" : 2434,
    "name" : "dharmen"
}

print(monthConversion["id"]) #accessing values
print(monthConversion.get("id"))

#updating a key value

monthConversion["id"] = 2435;
print(monthConversion.get("id"))

marks = int(input("enter the numenr "))
if marks > 80 :
    print("A")
elif marks <=80 :
    print("B")
elif marks <= 60 :
    print("C")
elif marks <= 50 :
    print("D")
elif marks <= 45 : 
    print("E")
else:
    print("F")
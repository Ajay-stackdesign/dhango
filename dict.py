myDict = {
    "name": "ajay",
    "age": 15,
    "school": "sdv"
}

value = myDict.get("name")
print(value)
print(myDict)


myDict2 = dict(name="ajay",age=13,school="sdv")
print(myDict2)


myDict3 = {
    "name": "ajay",
    "age": 22,
    "school": "sdv",
    "div": "A"
}
myDict3["name"] = "geeta"
del myDict3["name"]

print(myDict3.get("name"))
print(myDict3["age"])

dict = {
    "name": "ajay",
    "age": 24,
    "school": "sdv"
}
try:
    print(dict["lastName"])
except:
    print("error")

myTuple = (8,7)
dict1 = {myTuple: 15}
print(dict1)


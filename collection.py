#collections: Counter, namedtuple, OrderedDict, defaultdict,deque;

# from collections import Counter

# a = "aaabbbbbbbcccc";

# my_count = Counter(a); # It willl  count how muchthe letter has repited

# print(my_count.values())
# print(my_count.most_common(1)[0][0])

# from collections import Counter;

# a = "aaabcbcbcb";
# my_count = Counter(a)
# print(my_count)
# print(list(my_count.elements())) 
# print(my_count.keys())

# from collections import namedtuple;

# point = namedtuple('point',"x,y");
# pt = point(1 , -4)
# print(pt)

from collections import namedtuple

# employ = namedtuple("employer",["name","salary","age"])
# point = employ("ajay",34444,23);
# print(point[1])
# print("the name of the employer",point.name);
# print("the salary of the employer",point.salary);
# print("the age of the employer",point.age)

student = namedtuple("student",["name","div","number"])

point = student("ajay","a",23)
print("working as a full stack developer",point.name)
print("got a cerificate",point.div)






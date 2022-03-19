
def decor(func):
    def inner():
        print("hello world")
        func()
        print("hello world")
    return inner

def num():
    print("hello world1")
    print("hello world2")

result_fun = decor(num)
result_fun()
# print(result_fun)
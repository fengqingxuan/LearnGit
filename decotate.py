def debug(func):
    def wrapper(*args,**kwarys):
        print("start")
        func(*args,**kwarys)
        print("end")
    return wrapper
@debug
def function1():
    print("方法一")

@debug
def function2():
    print("方法二")

@debug
class cat:
    def __init__(self):
        print("new")
# function1()
# function2()
cat1=cat()
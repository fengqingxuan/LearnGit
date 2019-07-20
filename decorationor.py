#装饰器函数修饰函数 求和函数
def decort1(func):
    c=150
    d=200
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        result=result*c/d
        return result
    return wrapper

@decort1
def sum_func(a,b,c):
    return a+b+c
#装饰器函数修饰类-单例模式
def singModle(cls):
    a_dict={}
    def wrapper(*args,**kwargs):
        if cls not in a_dict:
            a_dict[cls]=cls(*args,**kwargs)
        return a_dict[cls]
    return wrapper

def singModle2(cls):
    width=100
    height=75
    def wrapper(*args,**kwargs):
        model=cls(*args,**kwargs)
        model.width=width
        model.height=height
        return model
    return wrapper
@singModle2
@singModle
class student:
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex

#类装饰器装饰函数
class metamodel:
    def __init__(self,function):
        self.function=function
        self.c=150
        self.d=200
    def __call__(self, *args, **kwargs):
        print("开始调用函数%s"%self.function)
        result=self.function(*args,**kwargs)
        result=result*self.c/self.d
        print("调用完成")
        return result
@metamodel
def sum_func(a,b):
    return a+b

#类装饰器修饰类 增加属性
class classModel:
    def __init__(self,cls):
        self.cls=cls
        self.width=170
        self.weight=120
    def __call__(self, *args, **kwargs):
        print("开始调用类",self.cls.__name__)
        smodel=self.cls(*args,**kwargs)
        smodel.width=self.width
        smodel.weight=self.weight
        print("结束调用",self.cls.__name__)
        return smodel
@classModel
class stu:
    def __init__(self,name,age):
        self.name=name
        self.age=age

if __name__=='__main__':
    # print(sum_func(100,200,100))
    # a_dict={}
    # a_dict['a']='aaaa'
    # a_dict[2]='bbbb'
    # print('a' in a_dict)
    # print(a_dict['a'])
    # xiaoming=student('xiaoming','man')
    # print(xiaoming.height)
    # print(id(xiaoming))
    # xiaoli=student('xiaoli','woman')
    # print(id(xiaoli))
    # print(sum_func(100,300))
    stu1=stu("fqx","24")
    print(stu1.weight)
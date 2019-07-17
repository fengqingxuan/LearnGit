from abc import ABCMeta,abstractmethod

#一、接口模式
# 定义:一种特殊的类,声明了若干方法,要求继承该接口的类必须实现这种方法
#     作用:限制继承接口的类的方法的名称及调用方式,隐藏了类的内部实现
class Payment(metaclass=ABCMeta):
    @abstractmethod#定义抽象方法的关键字
    def pay(self,money):
        pass

    # @abstractmethod
    # def pay(self,money):
    #     raise NotImplementedError

class AiliPay(Payment):
    def pay(self,money):
        print("使用支付宝支付%s元"%money)

class ApplePay(Payment):
    def pay(self,money):
        print("使用苹果支付%s元"%money)

#二、单例模式
# 定义:保证一个类只有一个实例,并提供一个访问它的全局访问点
#      适用场景:当一个类只能有一个实例而客户可以从一个众所周知的访问点访问它时
#      优点:对唯一实例的受控访问,相当于全局变量,但是又可以防止此变量被篡改
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance=super(Singleton, cls).__new__(cls)
        return cls._instance
class Myclass(Singleton):
    def __init__(self,name):
        if name:
            self.name=name

#三、简单工厂模式
# 定义:不直接向客户暴露对象创建的实现细节,而是通过一个工厂类来负责创建产品类的实例
#      角色:工厂角色,抽象产品角色,具体产品角色
#      优点:隐藏了对象创建代码的细节,客户端不需要修改代码
#      缺点:违反了单一职责原则,将创建逻辑集中到一个工厂里面,当要添加新产品时,违背了开闭原则
class Payment(metaclass=ABCMeta):
    #抽象产品角色
    @abstractmethod
    def pay(self,money):
        pass

class AiliPay(Payment):
    #具体产品角色
    def __init__(self,enable_yuebao=False):
        self.enable_yuebao=enable_yuebao
    def pay(self,money):
        if(self.enable_yuebao):
            print("使用余额宝支付%d元"%money)
        else:
            print("使用支付宝支付%d"%money)
class ApplePay(Payment):
    #具体产品角色
    def pay(self,money):
        print("使用苹果支付%d"%money)
class PaymentFactory:
    def create_payment(self,method):
        if method=='alipay':
            return AiliPay()
        elif method=='yuebao':
            return AiliPay(True)
        elif method=='applepay':
            return ApplePay()
        else:
            return NameError

#四、工厂方法模式
 # 定义:定义一个创建对象的接口(工厂接口),让子类决定实例化哪个接口
 #     角色:抽象工厂角色,具体工厂角色,抽象产品角色,具体产品角色
 #     适用场景:需要生产多种,大量复杂对象的时候,需要降低代码耦合度的时候,当系统中的产品类经常需要扩展的时候
 #     优点:每个具体的产品都对应一个具体工厂,不需要修改工厂类的代码,工厂类可以不知道它所创建的具体的类,隐藏了对象创建的实现细节
 #     缺点:每增加一个具体的产品类,就必须增加一个相应的工厂类
class Payment(metaclass=ABCMeta):
     def pay(self,money):
         pass
class PaymentFactory1(metaclass=ABCMeta):
    def create_paymethod(self):
        pass
class AliPay(Payment):
    def pay(self,money):
        print("使用支付宝支付%s元"%money)
class AliPayFactory(PaymentFactory1):
    def create_paymethod(self):
        return AliPay()
class ApplePay(Payment):
    def pay(self,money):
        print("使用苹果支付%s元"%money)
class AppleFactory(PaymentFactory1):
    def create_paymethod(self):
        return ApplePay()

#五、抽象工厂模式
class Shell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass
class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_CPU(self):
        pass
class OS(metaclass=ABCMeta):
    @abstractmethod
    def showOS(self):
        pass
class phonefactory(metaclass=ABCMeta):
    def create_shell(self):
        pass
    def create_cpu(self):
        pass
    def create_os(self):
        pass
class BigShell(Shell):
    def show_shell(self):
        print('大屏幕')
class SmallShell(Shell):
    def show_shell(self):
        print('小屏幕')
class BigCPU(CPU):
    def show_CPU(self):
        print('大CPU')
class SmallCPU(CPU):
    def show_CPU(self):
        print('小CPU')
class BigOS(OS):
    def showOS(self):
        print('大OS')
class SmallOS(OS):
    def showOS(self):
        print('小OS')
class BigFactory(phonefactory):
    def create_shell(self):
        return BigShell()
    def create_cpu(self):
        return BigCPU()
    def create_os(self):
        return BigOS()
class SmallFactory(phonefactory):
    def create_shell(self):
        return SmallShell()
    def create_cpu(self):
        return SmallCPU()
    def create_os(self):
        return SmallOS()
class Phone:
    def __init__(self,shell,cpu,os):
        self.shell=shell
        self.cpu=cpu
        self.os=os
    def show_info(self):
        print('手机信息')
        self.shell.show_shell()
        self.cpu.show_CPU()
        self.os.showOS()
def make_phone(factory):
    shell=factory.create_shell()
    cpu=factory.create_cpu()
    os=factory.create_os()
    return Phone(shell,cpu,os)
if __name__=='__main__':
    # a=Myclass('a')
    # print(a)
    # print(a.name)
    # b=Myclass('b')
    # print(b)
    # print(b.name)
    # print(a)
    # print(a.name)
    factory=PaymentFactory()#简单工厂模式
    pay_method=factory.create_payment('alipay')
    pay_method.pay(100)
    fac1=AliPayFactory()#工厂方法模式
    fa2=AppleFactory()
    ali_method1=fac1.create_paymethod()
    app_method1=fa2.create_paymethod()
    ali_method1.pay('200')
    app_method1.pay('150')
    #抽象工厂模式
    p1=make_phone(SmallFactory())
    p1.show_info()

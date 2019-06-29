#栈-- 先进后出
class Stock():
    def __init__(self):
        #初始化一个list容器
        self.__list=[]
    #push(item) 添加一个元素到栈顶
    def push(self,item):
        self.__list.append(item)
    #pop()  弹出栈顶元素
    def pop(self):
        if self.is_empty():
            return
        else:
            return self.__list.pop()
    #peek() 返回栈顶元素
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.__list[-1]
    #is_empty() 判断栈是否为空
    def is_empty(self):
        return not self.__list
    #size() 返回栈元素个数
    def size(self):
        return len(self.__list)

if __name__=='__main__':
    #Stock()  创建一个新空栈
    stock=Stock()
    print(stock.is_empty())
    stock.push(3)
    stock.push(5)
    stock.push(-1)
    print(stock.is_empty())
    print(stock.size())
    print(stock.pop())
    print(stock.peek())
    print(stock.size())
    print(stock.pop())
    print(stock.pop())
    print(stock.pop())
    print(stock.size())

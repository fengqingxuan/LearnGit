#双端队列，可自由在某一端加入或删除元素
class DbQueue():
    def __init__(self):
        # 初始化一个list容器
        self.__list=[]

    #从队头添加item
    def add_front(self,item):
        self.__list.append(item)
    #从队尾添加item
    def add_rear(self,item):
        self.__list.insert(0,item)
    #从队头删除item
    def remove_front(self):
        if self.is_empty():
            return
        else:
            return self.__list.pop()
    #从队尾删除item
    def remove_rear(self):
        if self.is_empty():
            return
        else:
            return self.__list.pop(0)
    #判断队列是否为空
    def is_empty(self):
        return not self.__list
    #返回队列大小
    def size(self):
        return len(self.__list)

if __name__=='__main__':
    dbQueue=DbQueue()
    dbQueue.add_front(2)
    dbQueue.add_front(5)
    dbQueue.add_front(9)
    dbQueue.add_rear(20)
    dbQueue.add_rear(50)
    # print(dbQueue.remove_rear())
    # print(dbQueue.remove_rear())
    # print(dbQueue.remove_rear())
    print(dbQueue.remove_rear())
    print(dbQueue.remove_rear())
    print(dbQueue.remove_front())
    print(dbQueue.remove_front())
    print(dbQueue.remove_front())
    # print(dbQueue.remove_front())
    # print(dbQueue.remove_front())
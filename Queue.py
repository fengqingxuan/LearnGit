#普通队列，先进先出
class Queue():
    def __init__(self):
        #初始化一个list容器
        self.__list=[]
    #enqueue(item) 往队列添加元素
    def enqueue(self,item):
        self.__list.append(item)
    #dequeue()	从队列头部删除元素
    def dequeue(self):
        if self.is_empty():
            return
        else:
            return self.__list.pop(0)
    #is_empty()	判断是否为空
    def is_empty(self):
        return not self.__list
    #size()		返回队列大小
    def size(self):
        return len(self.__list)

if __name__=='__main__':
    queue=Queue()
    queue.enqueue(3)
    queue.enqueue(10)
    queue.enqueue(15)
    print(queue.is_empty())
    print(queue.size())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.is_empty())
    print(queue.size())

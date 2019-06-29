class Node():
    def __init__(self,val):
        self.item=val
        self.next=None
#单向循环链表
class SingleCilcleList():
    def __init__(self,node=None):
        self.__head=node
# is_empty length  travel  add  append  insert  remove  search
    def is_empty(self):
        return self.__head==None
    def length(self):
        count=0
        if self.is_empty():
            return count
        curl=self.__head
        while curl.next!=self.__head:
            count+=1
            curl=curl.next
        count+=1
        return count

    def travel(self):
        if self.is_empty():
            print("")
        else:
            curl=self.__head
            while curl.next!=self.__head:
                print(curl.item,end=' ')
                curl=curl.next
            print(curl.item)

    def add(self,val):
        node=Node(val)
        if self.is_empty():
            self.__head=node
            node.next=node
        else:
            curl=self.__head
            while curl.next!=self.__head:
                curl=curl.next
            curl.next=node
            node.next=self.__head
            self.__head=node

    def append(self,val):
        node=Node(val)
        if self.is_empty():
            self.__head=node
            node.next=node
        else:
            curl=self.__head
            while curl.next!=self.__head:
                curl=curl.next
            curl.next=node
            node.next=self.__head

    def insert(self,pos,val):
        node=Node(val)
        if pos<=0:
            self.add(val)
        if pos>=self.length():
            self.append(val)
        count=0
        curl=self.__head
        while curl.next!=self.__head:
            count += 1
            if count==pos:
                node.next=curl.next
                curl.next=node
                return
            else:
                curl=curl.next

    def search(self,val):
        curl=self.__head
        if self.is_empty():
            return False
        while curl.next!=self.__head:
            if(val==curl.item):
                return True
            curl=curl.next
        if val==curl.item:
            return True
        return False

    def remove(self,val):
        curl=self.__head
        pre=None
        if self.is_empty():
            return
        while curl.next!=self.__head:
            if curl.item==val:
                #首元素
                if curl==self.__head:
                    fina=self.__head
                    while fina.next!=self.__head:
                        fina=fina.next
                    fina.next=curl.next
                    self.__head=curl.next
                #中间元素
                else:
                    pre.next=curl.next
                return
            else:
                pre=curl
                curl=curl.next
        #末尾元素
        if curl.item==val:
            if curl==self.__head:
                self.__head=None
            else:
                pre.next=self.__head
        return


if __name__=="__main__":
    lb=SingleCilcleList()
    print(lb.is_empty())
    print(lb.length())
    lb.add(10)
    lb.travel()
    lb.remove(10)
    lb.travel()
    lb.append(10)
    lb.append(3)
    lb.append(16)
    lb.travel()
    lb.add(3)
    lb.travel()
    print(lb.search(11))
    lb.insert(2,5)
    lb.travel()
    lb.append(5)
    lb.append(5)
    lb.travel()
    lb.remove(5)
    lb.travel()
    print(lb.search(5))
    lb.remove(5)
    lb.travel()
    print(lb.search(5))
    lb.remove(5)
    lb.travel()
    print(lb.search(5))
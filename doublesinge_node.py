class Node():
    def __init__(self,val):
        self.item=val
        self.pre=None
        self.next=None
#双向链表
class DoubleSinge():
    def __init__(self,node=None):
        self.__head__=node
    def is_empty(self):
        return self.__head__ is None
    def length(self):
        count=0
        curl=self.__head__
        while curl!=None:
            count+=1
            curl=curl.next
        return count
    def travel(self):
        curl=self.__head__
        while curl!=None:
            print(curl.item,end=" ")
            curl=curl.next
        print("")
    def add(self,val):
        node=Node(val)
        if self.is_empty():
            self.__head__=node
        else:
            curl=self.__head__
            node.next=curl
            curl.pre=node
            self.__head__=node
            node.pre=None
    def append(self,val):
        node=Node(val)
        curl=self.__head__
        if self.is_empty():
            self.__head__=node
        else:
            while curl.next!=None:
                curl=curl.next
            curl.next=node
            node.pre=curl
    def insert(self,pos,val):
        count=0
        node=Node(val)
        curl=self.__head__
        if pos<=0:
            self.add(val)
            return
        if pos>=self.length():
            self.append(val)
            return
        while curl!=None:
            count += 1
            if(pos==count):
                curl.next.pre=node
                node.next=curl.next
                curl.next=node
                node.pre=curl
            else:
                curl=curl.next

    def search(self,val):
        curl=self.__head__
        count=0
        while curl!=None:
            if curl.item==val:
                return count
            count+=1
            curl=curl.next
        return -1

    def remove(self,val):
        curl=self.__head__
        while curl!=None:
            if val==curl.item:
                if curl.pre:
                    curl.pre.next=curl.next
                else:
                    self.__head__=curl.next
                if curl.next:
                    curl.next.pre=curl.pre
                return
            else:
                curl=curl.next


if __name__=='__main__':
    lb = DoubleSinge()
    print(lb.is_empty())
    print(lb.length())
    lb.add(10)
    lb.travel()
    # lb.remove(10)
    # lb.travel()
    lb.append(10)
    lb.append(3)
    lb.append(16)
    lb.travel()
    lb.add(3)
    lb.travel()
    lb.insert(5,1)
    lb.travel()
    print(lb.search(3))
    lb.remove(3)
    lb.travel()
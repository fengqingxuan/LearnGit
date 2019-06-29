class Node():
    def __init__(self,val):
        self.elem = val
        self.next = None
#单向链表
class LianBiao():
    def __init__(self,node=None):
        self.__head__=node
# is_empty length  travel  add  append  insert  remove  search
    def is_empty(self):
        cur=self.__head__
        return(cur==None)
    def add(self,val):
        node=Node(val)
        curl=self.__head__
        node.next=curl
        self.__head__=node
    def append(self,val):
        curl=self.__head__
        node=Node(val)
        if self.is_empty():
            self.__head__=node
        else:
            while curl.next!=None:
                curl=curl.next
            curl.next=node
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
            print(curl.elem,end=' ')
            curl=curl.next
        print('')
    def insert(self,xl,val):
        node=Node(val)
        count=0
        curl=self.__head__
        if xl<=0:
            self.add(val)
        elif xl>=self.length():
            self.append(val)
        else:
            while curl!=None:
                count += 1
                if(count==xl):
                    node.next=curl.next
                    curl.next=node
                else:
                    curl=curl.next
    def search(self,val):
        curl=self.__head__
        count=0
        while curl !=None:
            if(curl.elem==val):
                print(count)
                return
            else:
                count+=1
                curl=curl.next
        print('-1 不存在')
    def remove(self,val):
        curl=self.__head__
        pre=None
        while curl!=None:
            if val==curl.elem:
                if pre==None:
                    self.__head__=curl.next
                else:
                    pre.next=curl.next
                    return
            pre=curl
            curl=curl.next

if __name__=="__main__":
    lb=LianBiao()
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
    lb.search(11)
    lb.insert(2,5)
    lb.travel()
    lb.append(5)
    lb.append(5)
    lb.travel()
    lb.remove(5)
    lb.travel()
    lb.search(5)
    lb.remove(5)
    lb.travel()
    lb.search(5)
    lb.remove(5)
    lb.travel()
    lb.search(5)

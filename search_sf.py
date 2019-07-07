#
def binary_search(alist,item):
    #二分查找-递归 时间复杂度最优1  最差nlogn
    n=len(alist)
    c=n//2
    while n>=1:
        if alist[c]==item:
            return True
        elif alist[c]<item:
            return binary_search(alist[c+1:],item)
        else:
            return binary_search(alist[0:c],item)
    return False

def binary_search2(alist,item):
    #二分查找-非递归
    n=len(alist)
    first=0
    end=n-1
    while first<=end:
        mid=(first+end)//2
        if alist[mid]==item:
            return True
        elif alist[mid]>item:
            end=mid-1
        else:
            first=mid+1
    return False


if __name__=='__main__':
    list=[9,12,23,52,70,88]
    print(binary_search(list,70))
    print(binary_search(list, 100))
    print(binary_search2(list, 70))
    print(binary_search2(list,100))
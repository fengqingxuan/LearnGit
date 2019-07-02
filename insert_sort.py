#冒泡排序
#平均情况O(n²) 最好情况O(n) 最坏情况O(n²) 辅助空间(1) 稳定性：稳定
#
def bubble_sort(alist):
    lenth = len(alist)
    #执行多少次循环
    for j in range(0,lenth-1):
        #一次循环，选择一个值
        for i in range(0,lenth-1-j):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]

#冒泡排序-优化  本身为有序序列时间复杂度为O（n） 稳定
def bubble_sort2(alist):
    lenth=len(alist)
    for i in range(lenth-1):
        count=0
        for j in range(lenth-1-i):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
                count+=1
        if count==0:
            return

#选择排序  不稳定
#平均情况O(n²) 最好情况O(n²) 最坏情况O(n²) 辅助空间(1) 稳定性：不稳定
def select_sort(alist):
    lenth=len(alist)
    for i in range(0,lenth-1):
        for j in range(i+1,lenth):
            if alist[i]>alist[j]:
                alist[i],alist[j]=alist[j],alist[i]
#插入排序 -while写法
#平均情况O(n²) 最好情况O(n) 最坏情况O(n²) 辅助空间(1) 稳定性：稳定
def insert_sort(alist):
    lenth=len(alist)
    for i in range(1,lenth):
        j=i
        while j>0:
            if alist[j]<alist[j-1]:
                alist[j],alist[j-1]=alist[j-1],alist[j]
                j-=1
            else:
                break  #break是优化

#插入排序 双for写法 稳定
def insert2_sort(alist):
    lenth=len(alist)
    for i in range(1,lenth):
        for j in range(i,0,-1):
            if alist[j]<alist[j-1]:
                alist[j-1],alist[j]=alist[j],alist[j-1]

#希尔排序
#平均情况O(nlogn-n²) 最好情况O(n^1.3) 最坏情况O(n²) 辅助空间(1) 稳定性：不稳定
def shell_sort(alist):
    n=len(alist)
    c=n//2
    while c>0:
        for i in range(c,n):
            while i>0:
                if alist[i]<alist[i-c]:
                    alist[i],alist[i-c]=alist[i-c],alist[i]
                    i-=c
                else:
                    break
        c=c//2


#快速排序 时间复杂度最优nlogn  最差n*n
#平均情况O(nlogn) 最好情况O(nlogn) 最坏情况O(n²) 辅助空间(nlogn-n) 稳定性：不稳定
def quick_sort(alist,start,end):
    if start >= end:
        return
    mid_val=alist[start]
    low=start
    high=end
    while low<high:
        while low<high and alist[high]>mid_val:
            high-=1
        alist[low]=alist[high]
        while low<high and alist[low]<mid_val:
            low+=1
        alist[high]=alist[low]
    alist[low]=mid_val
    quick_sort(alist,start,low-1)
    quick_sort(alist,low+1,end)

#归并排序 最优最差，时间复杂度都为nlogn，空间额外开销
#平均情况O(nlogn) 最好情况O(nlogn) 最坏情况O(nlogn) 辅助空间(n) 稳定性：稳定
def merge_sort(alist):
    lenth=len(alist)
    if lenth==1:
        return alist
    c=lenth//2
    left_lis=merge_sort(alist[:c])
    right_lis=merge_sort(alist[c:])
    left_pos,right_pos=0,0
    result=[]
    while left_pos<len(left_lis) and right_pos<len(right_lis):
        if left_lis[left_pos]<=right_lis[right_pos]:
            result.append(left_lis[left_pos])
            left_pos+=1
        else:
            result.append(right_lis[right_pos])
            right_pos+=1
    result+=left_lis[left_pos:]
    result+=right_lis[right_pos:]
    return result


if __name__=='__main__':
    list=[45,26,93,17,56,13,85]
    print(list)
    # bubble_sort(list)#冒泡排序
    # bubble_sort2(list)#冒泡排序-优化
    #select_sort(list)#选择排序
    # insert_sort(list)#插入排序
    # insert2_sort(list)#插入排序 双for写法
    # quick_sort(list,0,len(list)-1)#快排
    # shell_sort(list)#希尔排序
    list=merge_sort(list)#归并排序
    print(list)


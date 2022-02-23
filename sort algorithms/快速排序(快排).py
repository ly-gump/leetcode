#时间复杂度 平均O(nlog2n) 最坏O(n^2)
#空间复杂度 一般O(log2n)  最坏O(n) 需要栈空间实现递归
#快速排序在表已基本有序的情况下不合适
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, first, last):
    if first < last:
        print(first,last)   #first,last在quickSortHelper(alist, first, splitPoint-1)发生变化 ？
        splitPoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitPoint-1)
        quickSortHelper(alist, splitPoint+1, last)  #逻辑难理解！！该如何自己编呢？

def partition(alist, first, last):
    pivotvlue = alist[first]

    leftmark = first+1
    rightmark = last
    done = False

    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvlue: # bugfix: 先比较index, 不然数组会越界，值和pivotvlue比
            leftmark += 1
        while rightmark >= leftmark and alist[rightmark] >= pivotvlue:
            rightmark -= 1

        if leftmark > rightmark: #需要到leftmark左边的数比rightmark右边的数小 且包括整个alist
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    alist[rightmark], alist[first] = alist[first], alist[rightmark]
    return rightmark    #返回一个下标 这个下标对应的数字序正确！

alist = [54,26,93,17,77,31,44,55,20]  #一个partition到 [31,26,20,17,44,54,77,55,93]
alist2 = [1]
quickSort(alist)
print(alist)


if __name__ == "__main__":
    test_data = [3,2,111,3,-1,0,0,1,0,2,4]

    res_stable = sorted(test_data)
    quickSort(test_data)
    print(test_data)
    print(res_stable)
    assert all(map(lambda x: x[0] == x[1], zip(res_stable, test_data)))
    #zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
    #Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。


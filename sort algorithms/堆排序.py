#堆是具有以下性质的完全二叉树：每个结点的值都大于或等于其左右孩子结点的值，称为大顶堆；或者每个结点的值都小于或等于其左右孩子结点的值，称为小顶堆。
#堆排序的基本思想是：将待排序序列构造成一个大顶堆，此时，整个序列的最大值就是堆顶的根节点。将其与末尾元素进行交换，此时末尾就为最大值。
# 然后将剩余n-1个元素重新构造成一个堆，这样会得到n个元素的次小值。如此反复执行，便能得到一个有序序列了。

#堆排序 建堆O(n),筛选排序O(nlogn).找出若干个数中最大/最小的前k个数，用堆排序是最好的。
def heapSort(alist):
    if alist == None or len(alist) == 0:
        return
    length = len(alist)
    output = []
    #这样操作是为了模仿堆(二叉树)？
    for i in range(length):
        tempLen = len(alist)
        for j in range(tempLen//2-1, -1, -1):
            preIndex = j
            preVal, heap = alist[preIndex], False
            while 2 * preIndex < tempLen - 1 and not heap:
                curIndex = 2 * preIndex + 1
                if curIndex < tempLen - 1: #取下标为curIndex与curIndex+1中较大的那个
                    if alist[curIndex] < alist[curIndex+1]:
                        curIndex += 1
                if preVal >= alist[curIndex]:
                    heap = True
                else:
                    alist[preIndex] = alist[curIndex]
                    preIndex = curIndex
            alist[preIndex] = preVal
        print(alist)
        output.insert(0, alist.pop(0)) #每次取出最大的那个值，最后即为正确顺序
    return output

test = [2, 6, 5, 9, 10, 3, 7]
print(heapSort(test))
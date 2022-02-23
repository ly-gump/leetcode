#希尔排序(Shell's Sort)是插入排序的一种又称“缩小增量排序”（Diminishing Increment Sort），是直接插入排序算法的一种更高效的改进版本。
#希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至 1 时，整个文件恰被分成一组，算法便终止。
# 一般的初次取序列的一半为增量，以后每次减半，直到增量为1。当增量减到1时，整个要排序的数被分成一组，排序完成。
# 希尔排序是非稳定排序算法。(由于多次插入排序，我们知道一次插入排序是稳定的，不会改变相同元素的相对顺序，但在不同的插入排序过程中，
# 相同的元素可能在各自的插入排序中移动，最后其稳定性就会被打乱，所以shell排序是不稳定的。)
# 希尔排序的时间的时间复杂度为O(n^1.5)，希尔排序时间复杂度的下界是n*log2n

# python实现希尔排序
def shellSort(alist):
    sublistcount= len(alist)//2 #按增量分组
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        print('gap=%d'%sublistcount,alist)
        sublistcount = sublistcount//2
    return alist

def gapInsertionSort(alist, start, gap):
    """按gap增量来排顺序"""
    for i in range(start+gap, len(alist), gap):
        currentValue = alist[i]
        position = i

        while position >= gap and alist[position-gap] > currentValue:
            alist[position] = alist[position-gap]
            position = position-gap
        alist[position] = currentValue

list0= [9,3,5,7,4,6,2,33,77,100,55]
gapInsertionSort(list0,0,3) #排列9，7，2，100
print(list0)
alist = [54,26,93,17,77,31,44,55,20]
print(shellSort(alist))
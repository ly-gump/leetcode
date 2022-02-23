'''
还是需要先理解原理再来看程序 否则太难懂 思想：
从低位开始将待排序的数按照这一位的值放到相应的编号为0~9的桶中。等到低位排完得到一个子序列，再将这个序列按照次低位的大小进入相应的桶中，
一直排到最高位为止，数组排序完成。

基数排序：一般情况，每个节点有d位关键字，必须执行t=d次分配和收集操作。分配的代价O(n),收集的代价O(rd)(rd为基数)，总代价O(d*(n+rd))
        适用于以数字和字符串为关键字的情况。
实现基数排序RadixSort, 分为:
最高位优先(Most Significant Digit first)法
最低位优先(Least Significant Digit first)法
'''

# 最低位优先法
def radixSortLSD(alist):
    if len(alist) == 0:
        return
    if len(alist) == 1:
        return alist
    tempList = alist
    maxNum = max(alist)
    radix = 10
    while maxNum * 10 > radix:
        newArr = [[], [], [], [], [], [], [], [], [], []]
        for n1 in tempList:
            testnum = n1 % radix
            testnum = testnum // (radix / 10) #得到个位，十位，百位的数字 并依次newarr中
            for n2 in range(10):
                if testnum == n2:
                    newArr[n2].append(n1)
        tempList = []
        for i in range(len(newArr)):
            for j in range(len(newArr[i])):
                tempList.append(newArr[i][j])
        radix *= 10
    return tempList


print(radixSortLSD([10, 12, 24, 23, 13, 52, 15, 158, 74, 32, 254, 201, 30, 19]))
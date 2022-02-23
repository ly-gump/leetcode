#归并排序比较占用内存，但却是效率高且稳定的排序算法
def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf) #必要！需要将两个子列表也排序
        mergeSort(righthalf)  #这样就能将两个子序列排序！！！ mergeSort就是将列表排序

        i = 0; j = 0; k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)




class Solution(object):
    def BubbleSort(self,nums):
        """
        冒泡排序(比较排序)：前后比较-交换
        时间复杂度： O(n^2)
        空间复杂度： O(1)
        :param list:
        :return:
        """
        swap=True
        passnum=len(nums)-1
        while passnum>=1 and swap:
            swap=False
            for i in range(passnum):
                if nums[i]>nums[i+1]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
                    swap=True
            passnum-=1
        return nums

    def selectionSort(self,nums):
        """
        选择排序：选择较小的数据放在前面
        时间复杂度：O(n^2)
        空间复杂度：O(1)
        :param nums:
        :return:
        """
        n=len(nums)
        for i in range(n-1):
            minindex=i
            for j in range(i+1,n):
                if nums[j]<nums[minindex]:
                    minindex=j
            nums[i],nums[minindex]=nums[minindex],nums[i]
        return nums

    def insertionSort(self,nums):
        """
        插入排序：逐个插入到前面的有序数中
        时间复杂度：O(n^2)
        空间复杂度：O(1)
        :param nums:
        :return:
        """
        n=len(nums)
        for i in range(n):
            value=nums[i]
            index=i
            while index>0 and nums[index-1]>value:
                nums[index]=nums[index-1]
                index-=1
            nums[index]=value

        return nums

    def shellSort(self,nums):
        """
        希尔排序：从大范围到小范围进行比较-交换 类似冒泡和插入的联合
        时间复杂度：O(n^2) 优化后可达O(n^1.5)
        空间复杂度：O(1)
        :param nums:
        :return:
        """
        n=len(nums)
        def gap(alist,start,gap):
            """
            按gap增量来排序
            """
            for i in range(start+gap,n,gap):
                value=nums[i]
                index=i
                while index>=gap and nums[index-gap]>value:
                    nums[index]=nums[index-gap]
                    index-=gap
                nums[index]=value

        sublistcount=n//2 #按增量分组
        while sublistcount>0:
            for start in range(sublistcount):
                gap(nums,start,sublistcount)
            print("gap=%d"%sublistcount,nums)
            sublistcount//=2

        return nums

    def mergeSort(self,nums):
        """
        归并排序：分治法2-4-8插入排序
        时间复杂度： O(nlog(n)) 每次合并的平均复杂度为O(n) 二叉树的最大深度为log(n)
        空间复杂度：O(n)
        :param nums:
        :return:
        """
        n=len(nums)
        if n>1:
            mid=n//2
            left=nums[:mid]
            right=nums[mid:]

            self.mergeSort(left)
            self.mergeSort(right)

            i=0;j=0;k=0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    nums[k]=left[i]
                    i+=1
                else:
                    nums[k]=right[j]
                    j+=1
                k+=1

            while i<len(left):
                nums[k]=left[i]
                i+=1
                k+=1

            while j<len(right):
                nums[k]=right[j]
                j+=1
                k+=1

    def quickSort(self,nums):
        """
        快速排序：选取一个基准值，小数在左大数在右
        时间复杂度：O(nlog(n))-O(n^2)
        空间复杂度：O(nlog(n)
        :param nums:
        :return:
        """
        def partition(nums,first,last):
            pivotvalue=nums[first] #基准值
            leftmark=first+1
            rightmark=last
            done=False

            while not done:
                while nums[leftmark]<=pivotvalue and leftmark<=rightmark:
                    leftmark+=1
                while nums[rightmark]>=pivotvalue and rightmark>=leftmark:
                    rightmark-=1
                if leftmark>rightmark:
                    done=True
                else:
                    nums[leftmark],nums[rightmark]=nums[rightmark],nums[leftmark]
            nums[first],nums[rightmark]=nums[rightmark],nums[first]
            return rightmark

        def quickSortHelper(nums,first,last):
            if first<last:
                splitpoint=partition(nums,first,last)

                quickSortHelper(nums,first,splitpoint-1)
                quickSortHelper(nums,splitpoint+1,last)

        quickSortHelper(nums,0,len(nums)-1)


    def heapSort(self,nums):
        """
        堆排序：利用最大堆和最小堆的特性
        时间复杂度：O(nlog(n))
        空间复杂度：O(1)
        :param nums:
        :return:
        """














lying=Solution()
nums=[1,7,3,10,77,33,100,99,52]
print(lying.BubbleSort(nums))
nums=[1,7,3,10,77,33,100,99,52]
print(lying.selectionSort(nums))
nums=[1,7,3,10,77,33,100,99,52]
print(lying.insertionSort(nums))
nums=[1,7,3,10,77,33,100,99,52]
print(lying.shellSort(nums))
nums=[1,7,3,10,77,33,100,99,52]
lying.mergeSort(nums)
print(nums)
nums=[1,7,3,10,77,33,100,99,52]
lying.quickSort(nums)
print(nums)










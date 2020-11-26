'''
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
'''

# quick sort
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_s = [str(num) for num in nums]
        self.quicksort(nums_s, 0, len(nums_s)-1)s
        return str(int("".join(nums_s))) #為什麼不直接 ''.join(nums_s), 因為[0,0] output "00", 而用str(int("".join(nums_s))) 可以解決 int("".join(['0','0'])) ->0

    def quicksort(self, nums, l, r): #sort inplace
        def partition(nums, l, r):
            p = l-1 #一開使放在index 0的左邊
            pivot = nums[r]
            for i in range(l, r):
                if nums[i] + pivot > pivot + nums[i]:  # '3' + '23' = '323'  ,'323'>'233' True
                    p += 1
                    nums[i], nums[p] = nums[p], nums[i] #nums[i] 需擺在右邊
            p += 1
            nums[r], nums[p] = nums[p], nums[r] #換pivot
            return p #位置P已排序完成 之後針對它的左右進行排序
                        
        if l<r:  #記得l<r 才做sort l=r 不需作動回報None
            mid = partition(nums, l, r)
            self.quicksort(nums, l, mid-1)
            self.quicksort(nums, mid+1, r)

'''
nums = [3,30,34,5,9]
nums_s = [str(num) for num in nums]
nums_s
['3', '30', '34', '5', '9']
'''



# merge sort
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        num = [str(x) for x in nums]
        num = self.mergeSort(num)
        return str(int("".join(num))) #str(int("".join(['2','5']))) -> '25'
    
    def mergeArray(self,left, right):
        """
            merge the left and right array
        """
        res = []
        i = j = 0
        while i < len(left) and j < len(right): #左右逐一對比
            if int(left[i] + right[j]) < int(right[j] + left[i]): #以誰擺前面產生最大值為依據
                res.append(right[j])
                j += 1
            else:
                res.append(left[i])
                i += 1
        while i < len(left):
            res.append(left[i])
            i += 1
        
        while j < len(right):
            res.append(right[j])
            j += 1
        return res
                
    def mergeSort(self,lists):
        if len(lists) <= 1:
            return lists
        mid = int(len(lists)//2)
        left = self.mergeSort(lists[:mid])
        right = self.mergeSort(lists[mid:])
        return self.mergeArray(left,right)





        
            









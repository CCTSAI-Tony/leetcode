# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place and use only constant extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

# 思路: 倒序操作判斷前一元素是否比自己大, 若有則再從新倒序遍歷找到第一個比自己大的元素來交換位置, 交換後針對前面交換位置以後序列做reverse
# 若無, 整個序列 reverse 變成最小的permutation 
# 利用2 pointer 來做二次倒序遍歷
# time complexity O(n)
# 5724310 => 57 2! 4310 => 57 3! 4210(reverse) => 5730124
class Solution:
    def nextPermutation(self, nums):
	    i = j = len(nums)-1
	    while i - 1 > 0 and nums[i-1] >= nums[i]: #記得>=, 前一個元素值相等也一樣符合條件ex: Input: [5,1,1]
	        i -= 1  #倒序操作
	    if i == 0:   # nums are in descending order
	        nums.reverse() #反轉
	        return 
	    k = i - 1    # find the last "ascending" position 
	    while nums[j] <= nums[k]:  #記得<=, 要找比自己大的元素, 相等也不考慮
	        j -= 1
	    nums[k], nums[j] = nums[j], nums[k]  #倒序找比自己大的元素交換位置
      #開始做reverse 序列, 請記起來基本語句
	    l, r = k+1, len(nums)-1  # reverse the second part >小的在前面 => implace modified
	    while l < r:
	        nums[l], nums[r] = nums[r], nums[l]
	        l +=1 ; r -= 1
	        #如果要在一行中书写多条句，就必须使用分号;分隔每个语句，否则Python无法识别语句之间的间隔


#重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums) - 1
        while i - 1 >= 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        k = i - 1
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        l, r = i, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1



#重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i - 1 >= 0 and nums[i] > nums[i-1]:
                while r >= i:
                    if nums[r] > nums[i-1]:
                        nums[r], nums[i-1] = nums[i-1], nums[r]
                        l, r = i, len(nums) - 1
                        while l < r:
                            nums[l], nums[r] = nums[r], nums[l]
                            l += 1
                            r -= 1
                        return nums
                    r -= 1
            elif i == 0:
                l, r = i, len(nums) - 1
                while l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
        return nums












        '''
        a  b  c  123

        a  c  b  132

        b  a  c  213

        b  c  a  231

        c  a  b  312

        c  b  a  321

        115 aab

        151 aba

        511 baa

        2  3  1  231
              ij

           i   j
        k  i   j
 
        k  ij

        3  2  1
        k  ij
           
           l  r

        3  1  2  ans! 
           r  l

        1234
        1243
        1324
        1342
        1423
        1432 > 2431>2134
        2134
        2143
        2314
        2341
        2413
        2431
        3124
        3142
        3214
        3241
        3412
        3421
        4123
        4132
        4213
        4231
        4312 >4321
        4321

        2  4  3  1
                 ij
              i
           i
        k  i     j
        k  i  j

        3  4  2  1
        k  i  j
           l     r

        3  1  2  4 ok
              lr

        1  2  4  3
                 ij
              i  j
           k  i  j
        1  3  4  2
           k  i  j
              l  r
        1  3  2  4 ok
              r  l   


a = [1,30,5,3,2,70,8]
a[1:].sort()
a[1:]
[30, 5, 3, 2, 70, 8], .sort() 只能對整條序列起作用, 並不能針對切割序列做排序

a = [1,30,5,3,2,70,8]
sorted(a[1:])
[2, 3, 5, 8, 30, 70], 所以要使用sorted() 來對切割序列做排序




















        '''





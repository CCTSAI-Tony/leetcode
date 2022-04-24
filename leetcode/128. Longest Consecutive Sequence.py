'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

#搭配leetcode 128一起服用
#time complexity O(n)
#這題是求sequence, 所以不必連續字串
#思路: 先用set來消除重複元素, 找longest consecutive sequence 只需一個元素代表即可, 此題概念首尾貪吃蛇
#若一個元素在consecutive sequence上, 往前往後查找其他成員值, 一定可以把全部元素找出來, 
#這此題, 把找出來的元素從set拿掉=> 因為每個元素只會被pop or remove 1 次, 所以time complexity O(n)
class Solution:
    def longestConsecutive(self, num):
        num=set(num)
        maxLen=0
        while num:  #切記不能用for loop, 因為nums set.remove() 遍歷過程size會變小 => 導致alarm, 增加item倒不會alarm
            n=num.pop()
            i=n+1 #找是否有元素 =  n+ 1
            l1=0
            l2=0
            while i in num:
                num.remove(i) #set.remove() O(1) time complexity
                i+=1
                l1+=1
            i=n-1  #換找是否有 n-1 元素在裡面
            while i in num:
                num.remove(i)
                i-=1
                l2+=1
            maxLen=max(maxLen,l1+l2+1)  #+1, 記得把自己加進去
        return maxLen


#自己重寫, 刷題用這個
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_nums = set(nums)
        max_len = 0
        while new_nums:
            l1 = 0
            l2 = 0
            n = new_nums.pop()
            i = n + 1
            while i in new_nums:
                new_nums.remove(i)
                l1 += 1
                i += 1
            i = n - 1
            while i in new_nums:
                new_nums.remove(i)
                l2 += 1
                i -= 1
            max_len = max(max_len, l1+l2+1)
        return max_len


#重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        while nums: 
            num = nums.pop()
            l = 0
            temp = num - 1
            while temp in nums:
                nums.remove(temp)
                temp -= 1
                l += 1
            r = 0
            temp = num + 1
            while temp in nums:
                nums.remove(temp)
                temp += 1
                r += 1
            max_len = max(max_len, l + r + 1)
        return max_len

#重寫第三次, time complexity O(n), space complexity O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        while nums:
            n = nums.pop()
            l1 = 0
            l2 = 0
            i = n + 1
            while i in nums:
                nums.remove(i)
                l1 += 1
                i += 1
            i = n - 1
            while i in nums:
                nums.remove(i)
                l2 += 1
                i -= 1
            max_len = max(max_len, l1 + l2 + 1)
        return max_len



#重寫第四次, time complexity O(n), space complexity O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        while nums:
            l1 = l2 = 0
            n = nums.pop()
            i = n + 1
            while i in nums:
                l1 += 1
                nums.remove(i)
                i += 1
            i = n - 1
            while i in nums:
                l2 += 1
                nums.remove(i)
                i -= 1
            max_len = max(max_len, l1 + l2 + 1)
        return max_len


# 重寫第五次, time complexity O(n), space complexity O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        nums = set(nums)
        while nums:
            l1, l2 = 0, 0
            num = nums.pop()
            n = num + 1
            while n in nums:
                nums.remove(n)
                l1 += 1
                n += 1
            n = num - 1
            while n in nums:
                nums.remove(n)
                l2 += 1
                n -= 1
            max_len = max(max_len, l1 + l2 + 1)
        return max_len



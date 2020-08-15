'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
 

Constraints:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''
#暴力解 2 pointer, O(N^3) TLE
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i+1):
                if sum(nums[j:i+1]) == k:
                    count += 1
        return count

# Python clear explanation with code and exampl  

# Just wanted to share a clear explanation that helped me.

# First of all, the basic idea behind this code is that, whenever the sums has increased by a value of k, we've found a subarray of sums=k.
# I'll also explain why we need to initialise a 0 in the hashmap.
# Example: Let's say our elements are [1,2,1,3] and k = 3.
# and our corresponding running sums = [1,3,4,7]
# Now, if you notice the running sums array, from 1->4, there is increase of k and from 4->7, there is an increase of k. 
# So, we've found 2 subarrays of sums=k.

# But, if you look at the original array, there are 3 subarrays of sums==k. Now, you'll understand why 0 comes in the picture.

# In the above example, 4-1=k and 7-4=k. Hence, we concluded that there are 2 subarrays.
# However, if sums==k, it should've been 3-0=k. But 0 is not present in the array. To account for this case, we include the 0.
# Now the modified sums array will look like [0,1,3,4,7]. Now, try to see for the increase of k.

# 0->3
# 1->4
# 4->7
# Hence, 3 sub arrays of sums=k
# This clarified some confusions I had while doing this proble

# time complexity O(N)
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sums = 0
        d = dict()
        d[0] = 1
        
        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums-k,0) #若(sums - k) 這個key 存在, 代表有subarray sum == k, 因為sum指針是連續往右走所以subarray 不會斷掉
            d[sums] = d.get(sums,0) + 1
        
        return(count)

# ex: [1,3,5,-3,3,5] k = 5
# [0,1,!4,!9,6,!9,14] ans = 3

#思路: 這題包含負數, time complexity O(N), 利用dic 來查找有無目前sum - k 的key, 若有則代表有sum = k 的subarray 
class Solution(object):
    def subarraySum(self, nums, k):
        d = collections.Counter() #預設key value = 0, 也可用 collections.defaultdict(int)
        d[0] = 1 #記得初始條件 for sum = 0
        count = 0
        sums = 0
        for i in nums:
            sums += i
            count += d[sums-k] # 代表以目前sum的位置做為end, 開頭為sum-k的位置都能成為subarray 其sum = k
            d[sums] += 1
        return count


# import collections
# a = collections.Counter()
# a[1]
# 0

#與defailtdict, 最大差別就是有.elements 這個method
from collections import Counter 
  
# Creation of a Counter Class object using  
# string as an iterable data container 
x = Counter("geeksforgeeks") 
  
# printing the elements of counter object 
for i in x.elements(): 
    print ( i, end = " ") 
Output:

g g e e e e k k s s f o r 
















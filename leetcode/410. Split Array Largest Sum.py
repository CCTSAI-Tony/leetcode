'''
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. 
Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
'''

# 不錯的思路 !
# Binary Search Based Solution

# Imagine we split an array into m different sub-arrays. There can be several ways to do this split. Let us assume we take one possible split.
# In this particular split, we take the sum of each subarray j and call it S(j) where j is from 1 to m. 
# Then we figure out the sub-array which has the maximum sum from all of these m different sums and call it max_sum(array, m).
# What is the least possible value of max_sum(array, m)? Answer will be max(array) - this must be obvious. The max(array) value must be in one of the m sub-arrays. 
# The least possible amongst all possible m different sub-arrays would be a sub-array with a single element as the max(array).
# What is the maximum possible value of max_sum(array, m)? Answer will be sum(array) - a subarray with all elements.
# So the range of max_sum(array, m) is max(array) to sum(array).
# We now have a search problem - we need to search within the range max(array) to sum(array) 
# such that we find the minimum value in this range with which we can form at-most m sub-arrays such no sub-array has sum more than this value. 
# To efficiently search a sorted range we use binary search.
# Imagine we pick a value mid and find that we could make more sub-arrays than m. This means we picked too small value (check the code to understand this). 
# We should set low = mid + 1.
# Imagine we pick a value mid and find we could make less sub-arrays than m. 
# Now we can easily split those sub-arrays to increase the count and 
# still make sure that the maximum sum of those sub-arrays is less than mid (splitting will only decrease mid). 
# In this case, we record a potential solution and make high = mid-1, hoping to get an even better solution later.

# Lets use an example: [7,2,5,10,8] and 2
# max_sum([7,2,5,10,8], 2) will be in the range [10, 32] - i.e. any split of the array into 2 sub-array will have sum of the sub-array between [10, 32].
# Now we want to find the minimum value in this range with which we can form 2 sub-arrays. Lets do this linearly. 
# Can we use 10? Using 10, we can form [7, 2]; [5]; [10]; [8] - 4 subarrays. 
# We clearly need to increase the minimum value so that we can reduce from 4 subarrays.
# What if we used binary search and started with mid = (10+32)/2 = 21. This gives us [7,2,5]; [10,8] - This is valid solution. 
# Can we do better? We record 21 and reduce our range to [10, 20].
# This gives us mid as 15. [7,2,5]; [10]; [8] - Invalid! we got more than 2 sub-arrays. We need to increase low to mid+1 and search in the range [16, 20].
# [16, 20] gives us 18. [7,2,5]; [10,8] - This is a valid solution. Can we do better than 18? Let us search in the range [16,17]
# [16,17] gives mid as 16. [7,2,5]; [10]; [8]. This is invalid and we need to increase range. 
# New range is [17,17]. This again gives [7,2,5]; [10]; [8] and we get the new range as [18,17].
# [18,17] breaks the while loop! We have recorded 18 as the last answer and return it.



#模板2
#刷題用這個, time complexity O(nlog(sum(array)), space complexity O(1), 若包含input size => space complexity O(n)
#思路: 這題使用binary search, low = max(nums) 因為最小可能的最大subarray sum 就是max(array) 自己, high = sum(array)
#使用helper 來確認substring sum 的cap值 能否形成 > m個 substring, 若行則low = mid 代表值太小 形成超過m個subarray, else high = mid
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        low, high = max(nums), sum(nums)
        while low + 1 < high:
            mid = (low + high) // 2
            if self.valid(nums, m, mid):
                high = mid 
            else:
                low = mid 
        if self.valid(nums, m, low):
            return low
        else:
            return high
        
    def valid(self, nums, m, mid):
        cuts, curr_sum = 0, 0
        for x in nums:
            curr_sum += x
            if curr_sum > mid:
                cuts += 1
                curr_sum  = x
        subs = cuts + 1
        return subs <= m  #這裡是關鍵! subs <= m 時, high = mid => 找尋符合條件的最小值

#重寫第二次, time complexity O(nlog(sum(nums))), space complexity O(1)
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l, r = max(nums), sum(nums)
        while l + 1 < r:
            mid = l + (r- l) // 2
            if self.helper(mid, m, nums):
                r = mid
            else:
                l = mid
        if self.helper(l, m, nums):
            return l
        return r
        
    def helper(self, k, m, nums):
        count = 1
        temp = 0
        for num in nums:
            if temp + num > k:
                count += 1
                temp = 0
            temp += num
        return count <= m



#重寫第三次, time complexity O(nlog(sum(nums))), space complexity O(1)
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l, r = max(nums), sum(nums)
        while l + 1 < r:
            mid = l + (r - l) // 2
            if self.check(mid, nums, m):
                r = mid
            else:
                l = mid
        if self.check(l, nums, m):
            return l
        else:
            return r
                
    def check(self, k, nums, m):
        cut, cur = 0, 0
        for num in nums:
            cur += num
            if cur > k:
                cut += 1
                cur = num
        return cut + 1 <= m

# 重寫第四次, time complexity O(nlog(sum(nums))), space complexity O(1)
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        low, high = max(nums), sum(nums)
        def verify(cap):
            current_sum, cuts = 0, 0
            for num in nums:
                current_sum += num
                if current_sum > cap:
                    cuts += 1
                    current_sum = num
            return cuts + 1 <= m
        
        while low + 1 < high:
            mid = low + (high - low) // 2
            if verify(mid):
                high = mid
            else:
                low = mid
        
        if verify(low):
            return low
        else:
            return high


# 重寫第五次, time complexity O(nlog(sum(nums))), space complexity O(1)
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def helper(val):
            cut = 0
            cur_sum = 0
            for num in nums:
                if cur_sum + num > val:
                    cut += 1
                    cur_sum = num
                else:
                    cur_sum += num
            return cut + 1 <= m
        
        l, r = max(nums), sum(nums)
        while l + 1 < r:
            mid = l + (r - l) // 2
            if helper(mid):
                r = mid
            else:
                l = mid
        if helper(l):
            return l
        else:
            return r





#刷題用這個
#binary search 變異題型
#模板1 這個解法太厲害了
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        low, high, ans = max(nums), sum(nums), -1
        while low <= high:
            mid = (low+high)//2
            if self.is_valid(nums, m, mid): # can you make at-most m sub-arrays with maximum sum atmost mid 
                ans = mid
                high = mid-1
            else:
                low = mid + 1
        return ans

        
    def is_valid(self, nums, m, mid):
        # assume mid is < max(nums)
        cuts, curr_sum  = 0, 0
        for x in nums:
            curr_sum += x
            if curr_sum > mid:
                cuts, curr_sum = cuts+1, x  #x 放在新的subarray, 不然會超過mid, 這裡cut 就是切割
        subs = cuts + 1
        return (subs <= m)  #why <= m, cause we can easily split those sub-arrays to increase the count
    
    



#模板1, 這題不會越界, 因為答案一定在low, high included 區間內
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        low, high, ans = max(nums), sum(nums), -1
        while low <= high:
            mid = (low + high) // 2
            if self.valid(nums, m, mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
    def valid(self, nums, m, mid):
        cuts, curr_sum = 0, 0
        for x in nums:
            curr_sum += x
            if curr_sum > mid:
                cuts += 1
                curr_sum  = x
        subs = cuts + 1
        return subs <= m




# BruteForce
class Solution(object):
    def helper(self, nums, m):
        if nums == []:
            return 0
        elif m == 1:
            return sum(nums)
        else:
            min_result = float('inf')
            for j in range(1,len(nums)+1):  #這裡j 代表分界點 left: nums[:1] => nums[:len(nums)]
                left, right = sum(nums[:j]), self.helper(nums[j:], m-1)
                min_result = min(min_result, max(left, right))
            return min_result
    
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        return self.helper(nums, m)

a = [1,2,3]
a[6:]
[]
nums = []
sum(nums)
0
nums[:5]
[]


Memoization

#有點難懂
from collections import defaultdict    
class Solution(object):
    def helper(self, i, nums, m, cache):
        if i == len(nums):
            return 0
        elif m == 1:
            return sum(nums[i:])
        else:
            if i in cache and m in cache[i]:  #因為用到 defaultdict(dict), 要確認是否有m key
                return cache[i][m]
            cache[i][m] = float('inf')
            for j in range(1,len(nums)+1):  #切點
                left, right = sum(nums[i:i+j]), self.helper(i+j, nums, m-1, cache)
                cache[i][m] = min(cache[i][m], max(left, right))
                if left > right:  #最小值出現在中間點, 還有當self.helper(i+j), i+j = len(nums), return 0, left > right, break for loop
                    break
            return cache[i][m]
    
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        cache = defaultdict(dict)
        return self.helper(0, nums, m, cache)

Memoization + Cumulative Sum

from collections import defaultdict            
class Solution(object):
    def helper(self, i, nums, m, cache, cums):
        if i == len(nums):
            return 0
        elif m == 1:
            return sum(nums[i:])
        else:
            if i in cache and m in cache[i]:
                return cache[i][m]
            cache[i][m] = float('inf')
            for j in range(1,len(nums)+1):
                left, right = cums[i+j] - cums[i], self.helper(i+j, nums, m-1, cache, cums)
                cache[i][m] = min(cache[i][m], max(left, right))
                if left > right:
                    break
            return cache[i][m]
    
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        cums = [0]
        for x in nums:
            cums.append(cums[-1]+x)
        cache = defaultdict(dict)            
        return self.helper(0, nums, m, cache, cums)





















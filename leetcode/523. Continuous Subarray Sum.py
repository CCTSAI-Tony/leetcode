'''
Given a list of non-negative numbers and a target integer k, 
write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, 
that is, sums up to n*k where n is also an integer.

 

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
 

Note:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
'''

# Idea: if sum(nums[i:j]) % k == 0 for some i < j, then sum(nums[:j]) % k == sum(nums[:i]) % k. ex: k =5, nums[:j] = 7, sum(nums[:i] = 37
# So we just need to use a dictionary to keep track of sum(nums[:i]) % k and the corresponding index i. 
# Once some later sum(nums[:i']) % k == sum(nums[:i]) % k and i' - i > 1, we return True.

Time complexity: O(n), 
space complexity: O(min(k, n)) if k != 0, else O(n). 因為if k != 0, sum % k 共有k種key, 但 k == 0, 

# 這也算hash table
# 思路: if k != 0, 利用 sum % k 的值來紀錄, 若之前有遇到一樣%k值, 則sum(nums[i:j]) % k == 0, 我們可以利用hash table紀錄每個index 的 sum % k 值
# 此題陷阱很多, 注意此題k為任何整數, 負數,正數, 0都有可能, nums 只有可能為正整數與0, => 0可以是所有非0整數數的倍數, 但0的倍數只能是自己
class Solution():
    def checkSubarraySum(self, nums, k):
        dic = {0:-1}  #這個初始條件代表 sum % k == 0, index = -1(無元素), ex: k =5, nums[:1] = 10, 10 % 5 == 0, return false, 0-(-1) =1 < 2
        summ = 0
        for i, n in enumerate(nums):
            if k != 0:
                summ = (summ + n) % k
            else:  #k == 0 時
                summ += n  #因為不能被0整除所以直接加, ex: index 3: sum = 5 => i = 7, sum = 5, sum(nums[4:8]) = 0
            if summ not in dic:
                dic[summ] = i
            else:
                if i - dic[summ] >= 2:  #subarray of size at least 2
                    return True
        return False

#  ex: k =5, nums[:j] = 7, sum(nums[:i] = 37
#  k =5, nums[:j] = 10, sum(nums[:i] = 25

# dic = {0:-1} zero base index issue, 當 sum % k == 0, 此時整段subarray sums up to a multiple of k, 但i + 1 才是整段長度
# 任何整數都是0的因數。
# 另外，因為0不能作為任何數的因數，所以0沒有倍數。 5 % 0 => integer division or modulo by zero, 任何數不能被0整除
# 此題 0 可以sum up to 0 自己

Given a list of non-negative numbers 說明不是負數都有可能, 代表0 也有可能, 還有k 有可能為負數
ex: [-7, -4, -11] k =3, => -7 % 3 = 2, -22 % 3 = 2 => return True
a = Solution()
a.checkSubarraySum([0,0], 0)
True

# i.e.
# [4, 1, 2, 3] and 6

# if we get the accumulated sum, it looks like this [4, 5, 7, 10]
# if we make it accumulated sum % k, it looks like this [4, 5, 1, 4]
# notice that there is duplicated 4's. The diffference between these two sums in theory must be a multiple of 6 since we've only been storing the num%k.
# Just wanted to write this out cz I thought it was pretty awesome and really couldn't figure it out for a while. 說明有些觀點很難想

Need to pay attention to a lot of corner cases...

Some damn it! test cases:

[0], 0 -> false;
[5, 2, 4], 5 -> false;
[0, 0], 100 -> true;  任何整數都是0的因數
[1,5], -6 -> true;
[5,8,0,0], 0 -> true;
etc...



#另一種解法補充觀點用的, 用到pigeonhole principle, 太難證明背起來吧
# if k == 0
# If there are two continuous zeros in nums, return True
# Time O(n).
# if n >= 2k and k > 0, pigeonhole principle!!
# There will be at least three numbers in sum with the same remainder divided by k. So I can return True without any extra calculation.
# Time O(1).
# if n < 2k and k > 0
# If I can find two numbers in sum with the same remainder divided by k and the distance of them is greater than or equal to 2， return True.
# Time O(n) <= O(k).
# k < 0
# same as k > 0.
class Solution(object):
    def checkSubarraySum(self, nums, k):

        
        if k == 0:
            # if two continuous zeros in nums, return True
            # time O(n)
            for i in range(0, len(nums) - 1):
                if nums[i] == 0 and nums[i+1] == 0:
                    return True
            return False
        
        k = abs(k)
        if len(nums) >= k * 2:
            return True
        
        #if n >= 2k: return True
        #if n < 2k:  time O(n) is O(k)  

        sum = [0]
        for x in nums:
            sum.append((sum[-1] + x) % k)
        
        Dict = {}
        for i in range(0, len(sum)):
            if Dict.has_key(sum[i]):
                if i - Dict[sum[i]] > 1:
                    return True
            else:
                Dict[sum[i]] = i
        
        return False















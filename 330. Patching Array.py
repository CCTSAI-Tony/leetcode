'''
Given a sorted positive integer array nums and an integer n, add/patch elements to the array 
such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. 
Return the minimum number of patches required.

Example 1:

Input: nums = [1,3], n = 6
Output: 1 
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.
Example 2:

Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].
Example 3:

Input: nums = [1,2,2], n = 5
Output: 0
'''

# [1,2,3,5,10,50,70], n=100

# 看到第一个数1，我们知道[1,1]可以被覆盖
# 看到第二个数2，我们知道[1,3]可以被覆盖
# 3同理，[1,6]可以被覆盖
# 5同理，[1,11]可以被覆盖
# 10同理，[1,21]可以被覆盖
# 现在到50，发现不得不打补丁了，如果打补丁1，可以扩展为[1,22]，如果打补丁2，可以扩展为[1,23]...可见，要得到最大的范围，应该打的补丁是22，这样能得到[1,43]，
# 为什么不能打补丁23呢？因为[1,2,3,5,10,23]得不到22！
# [1,43]还是没有覆盖50，按照类似的逻辑，这次应该打的补丁是44，将范围扩充到[1,87]
# 最后到70，在[1,87]内，范围被扩充到[1,157]
# 157 > 100，结束
# 综上，一共要2个补丁，即22和44
# 所以，题目的要点在于，如果当前的范围是[1,m]，且当前的数字num > m，我们应该打补丁m+1，使得范围扩充到[1，2m+1]。

# 代码（Code）

#貪婪演算法(Greedy algorithm)是指在對問題求解時總是做出在當前看來是最好的選擇, Greedy algorithm have a local choice of the sub-problems
#使用greedy的時機在於若local最佳解就是整體最佳解就可用greedy, top-down: 直接從n與整段nums區間為切入點
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        cnt = 0
        patch = 0
        tot = len(nums)
        i = 0
        while patch < n:  #still can't cover [1,n]
            if i < tot and patch + 1 >= nums[i]:  #patch + 1 這邊很重要, 不能patch + 2,3,4,,, 因為就是要補足差一的那個坑, 若當前的數不能補坑就要打補丁了
                patch += nums[i]
                i += 1
            else:
                cnt += 1
                #print(patch+1)
                patch += patch + 1  # patch + 1 is the new patch to be added
        return cnt



#Why does a greedy solution work for this problem?

# I see in many solutions posted here, the strategy is to patch the next missing number itself:

# For example, with [1, 2, 3] and N=20, I get 1-6 covered, and I patch 7.

# Yes, 7 would push the frontier the furthest (to 13), but if I choose to patch 4 instead, maybe a 4 may come in 
# handy when I need to make other numbers down the road?

# Why is this choice 7 optimal? Can any provide a solid proof?



# because we are minimizing the number of patch, not the sum of the patch, whatever 4 can reach, 7 can reach , but not vice versa.


# Now “top down” approach is nothing but resolving the problem from high level to low level.Basically you start from the whole problem.

# In "bottom up" approach, you identify lower-level tools that you can compose to become a bigger program.Basically you focus on parts of the problem to solve it.









'''
You have a number of envelopes with widths and heights given as a pair of integers (w, h).
One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
'''


# Dynamic Programming: DP(N^2) in this problem TLE!!
# Sort envelopes first, then it's easy to derive that:
# dp[i]: maximum number of envelopes ends with envelopes[i]
# dp[i] = max{dp[j]}(0<=j<i) + 1


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        if n < 2:
            return n
        envelopes.sort()
        ans = 1
        dp = [1 for i in range(n)]
        for i in range(1, n):
            for j in range(i):  # 不包含i
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
            ans = max(ans, dp[i])
        return ans



# Sort envelopes first, then use LIS solution to find maximum length of subsequence of the 2nd dimension. (Longest Increasing Subsequence (LIS))
# Note that when we sort the original envelopes list, we need to increasing 1st dimension and decreasing 2nd dimension.
# Think about case [[1, 3], [1, 4], [1,5], [1, 3]]. Decreasing 2nd dimension can help us to avoid the equavalent 1st dimension cases.

# 刷題用這個
# Binary Search:  BS(NlogN), 刷題用這個, 搭配300題服用
# 若只按照1st dimension, 依照code 會算進相同1st dimension cases, ex:[1,1], [1,2], [1,3]...
# after sort => [[1, 5], [1, 4], [1,3], [1, 3]]
# 思路: 先sord 1d小到大 在相同1d下sort 2d大到小
# 若遇到比自己小或一樣大的, 找出在ans的適合位置, 替換該位置的值
# 替換後有可能不再是連續可封裝,(只能封裝2d比它小的), 但這麼做是為了未來 較大1d但偏小的2d 有機會變可封裝(新LIS), 但此替換不影響當下LIS長度
# 因為1D的數值已經先從小到大排好序了, 再來依2D大到小排序, 因此若2D遇到比自己大的則代表1,2D都比自己大, append!! 重要
# 300題是,遇到後面num比較小的=>插入前面位置, 因為index 比較後面所以, 其他元素比它小的依舊可以成為新的LIS
# 然而354題也有一樣想法, 遇到後面2d比較小的=>插入前面位置, 因為1d 比較大所以, 其他元素2d比它小的依舊可以成為新的LIS
class Solution(object):

    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        if n < 2:
            return n
        envelopes.sort(key=lambda x: (x[0], -x[1]))  # 先按照x[0]排序 再細部按照-x[1]排序, 這個想法最重要
        ans = [envelopes[0][1]]  # list 化
        for i in range(1, n):
            if envelopes[i][1] > ans[-1]:
                ans.append(envelopes[i][1])
            else:
                pos = self.bs(ans, envelopes[i][1])  
                ans[pos] = envelopes[i][1]
        return len(ans)

    # 模板1
    def bs(self, nums, h):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < h:
                left = mid + 1
            else:  # if nums[mid] >= h
                right = mid - 1
        return left

# 必看 envelops = [[1, 4], [1, 2], [2, 8], [2, 7], [3, 9], [4, 4], [5, 5], [6, 6]] =>[[1,4]]=>[[1,2]]=>[[1,2],[2,8]] => [[1,2],[2,7]] 
# => [[1,2],[2,7],[3,9]]=> [[1,2],[4,4],[3,9]]=>[[1,2],[4,4],[5,5]]=> [[1,2],[4,4],[5,5],[6,6]]
# 300題是,遇到後面num比較小的=>插入前面位置, 因為index 比較後面所以, 其他元素比它小的依舊可以成為新的LIS
# 然而354題也有一樣想法, 遇到後面2d比較小的=>插入前面位置, 因為1d 比較大所以, 其他元素2d比它小的依舊可以成為新的LIS
 
# envelopes = [[1, 5], [1, 4], [1, 3], [1, 3], [2, 6], [2, 3], [3, 9], [3, 7], [4, 8], [4, 2]] 請用這個例子想 ans = [2, 6, 7, 8] 答案4


# envelopes = [[1, 3], [1, 4], [1,5], [1, 3],[2,3],[2,6]]
# envelopes.sort(key=lambda x:(x[0], -x[1]))
# envelopes
# [[1, 5], [1, 4], [1, 3], [1, 3], [2, 6], [2, 3]]

# ans = [envelopes[0][1]]
# ans
# [5]

# envelopes[0][1]
# 5

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        if n < 2:
            return n
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        ans = [envelopes[0][1]]  # list 化
        for i in range(1, n):
            if envelopes[i][1] > ans[-1]:
                ans.append(envelopes[i][1])
            else:
                pos = self.bs(ans, envelopes[i][1])
                ans[pos] = envelopes[i][1]
        return len(ans)

    # 模板2
    def bs(self, nums, h):
        left, right = 0, len(nums)-1
        while left + 1 < right:
            mid = (left+right)//2
            if nums[mid] < h:
                left = mid
            else:
                right = mid
        if nums[left] >= h:
            return left
        return right

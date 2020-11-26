'''
In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). 
If there are multiple answers, return the lexicographically smallest one.

Example:

Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
 

Note:

nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
'''

# A greedy solution using three sliding windows where you keep track of the best indexes/sums as you go.

# O(n) time: Since we're only going through the list once and using no complex operations, this is O(n).
# O(1) space: Just a fixed set of temp vars. We don't need the extra arrays that the DP solutions have.

#刷題用這個 time complexity O(n), space complexity O(1)
#思路: three pointers, 利用三指針遍歷array, 初始指針的位置要間隔, 例如sequence1 的有效起始指針遍歷位置[0, n-3k+1], sequence2 [k, n-2k+1], sequence3 [2k, n-k+1] 左閉右開
#再遍歷的途中, 更新區間sum, 若大於bestsum, 則更新區間起始指針, while loop 終止條件: 當sequence3 起始指針 > n-k 時終止
#最後return bestThreeSeq
#核心, 利用sliding window 來不斷更新每個區間sum, 也因為此遍歷關係, 得到的maximum index 也是 lexicographically smaller
#注意: seqSum, seqTwoSum, seqThreeSum 要合在一起才能比較, 不能獨立windowSum比較, 不然會重疊
class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        # Best single, double, and triple sequence found so far
        bestSeq = 0
        bestTwoSeq = [0, k]
        bestThreeSeq = [0, k, k*2]

        # Sums of each window
        seqSum = sum(nums[0:k])
        seqTwoSum = sum(nums[k:k*2])
        seqThreeSum = sum(nums[k*2:k*3])

        # Sums of combined best windows
        bestSeqSum = seqSum
        bestTwoSum = seqSum + seqTwoSum
        bestThreeSum = seqSum + seqTwoSum + seqThreeSum

        # Current window positions => 起始位置
        seqIndex = 1
        twoSeqIndex = k + 1
        threeSeqIndex = k*2 + 1
        while threeSeqIndex <= len(nums) - k:
            # Update the three sliding windows
            seqSum = seqSum - nums[seqIndex - 1] + nums[seqIndex + k - 1]
            seqTwoSum = seqTwoSum - nums[twoSeqIndex - 1] + nums[twoSeqIndex + k - 1]
            seqThreeSum = seqThreeSum - nums[threeSeqIndex - 1] + nums[threeSeqIndex + k - 1]
            
            # Update best single window
            if seqSum > bestSeqSum:
                bestSeq = seqIndex
                bestSeqSum = seqSum

            # Update best two windows
            if seqTwoSum + bestSeqSum > bestTwoSum:
                bestTwoSeq = [bestSeq, twoSeqIndex]
                bestTwoSum = seqTwoSum + bestSeqSum

            # Update best three windows
            if seqThreeSum + bestTwoSum > bestThreeSum:
                bestThreeSeq = bestTwoSeq + [threeSeqIndex]
                bestThreeSum = seqThreeSum + bestTwoSum

            # Update the current positions
            seqIndex += 1
            twoSeqIndex += 1
            threeSeqIndex += 1

        return bestThreeSeq

#刷題用這個, time complexity O(n)
#思路: three pointers, 利用三指針遍歷array, 初始指針的位置要間隔, 例如sequence1 的有效起始指針遍歷位置[0, n-3k+1], sequence2 [k, n-2k+1], sequence3 [2k, n-k+1] 左閉右開
#再遍歷的途中, 更新區間sum, 若大於bestsum, 則更新區間起始指針, for loop 終止條件: 當sequence1 起始指針 > n-3k 時終止
#最後return mw3index
#核心, 利用sliding window 來不斷更新每個區間sum, 也因為此遍歷關係, 得到的maximum index 也是 lexicographically smaller
#注意: seqSum, seqTwoSum, seqThreeSum 要合在一起才能比較, 不能獨立windowSum比較, 不然會重疊
class Solution(object):
    def maxSumOfThreeSubarrays(self,nums, k):
        w1,w2,w3=sum(nums[:k]),sum(nums[k:2*k]),sum(nums[2*k:3*k])
        mw1,mw2,mw3=w1,w1+w2,w1+w2+w3
        mw1index,mw2index,mw3index=[0],[0,k],[0,k,2*k]#mw1,mw2,mw3's index.
        for i in range(1,len(nums)-3*k+1):#last index for w1 window will be n-3k
            w1+=nums[i-1+k]-nums[i-1]
            w2+=nums[i-1+2*k]-nums[i-1+k]
            w3+=nums[i-1+3*k]-nums[i-1+2*k]
            if w1>mw1:
                mw1,mw1index=w1,[i]
            if mw1+w2>mw2:
                mw2,mw2index=mw1+w2,mw1index+[i+k]
            if mw2+w3>mw3:
                mw3,mw3index=mw2+w3,mw2index+[i+2*k]
        return mw3index














#自己重寫, 刷題用這個
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        bestIndex1 = [0]
        bestIndex2 = [0, k]
        bestIndex3 = [0, k, k*2]
        windowSum1 = sum(nums[0:k])
        windowSum2 = sum(nums[k:k*2])
        windowSum3 = sum(nums[k*2:k*3])
        bestSum1 = windowSum1
        bestSum2 = windowSum1 + windowSum2
        bestSum3 = windowSum1 + windowSum2 + windowSum3
        currIndex1 = 1
        currIndex2 = k+1
        currIndex3 = k*2 + 1
        while currIndex3 <= n-k:
            windowSum1 = windowSum1 - nums[currIndex1 -1] + nums[currIndex1 + k -1]
            windowSum2 = windowSum2 - nums[currIndex2 -1] + nums[currIndex2 + k -1]
            windowSum3 = windowSum3 - nums[currIndex3 -1] + nums[currIndex3 + k -1]
            
            if windowSum1 > bestSum1:
                bestIndex1 = [currIndex1]
                bestSum1 = windowSum1
                
            if bestSum1 + windowSum2 > bestSum2:
                bestIndex2 = bestIndex1 + [currIndex2]
                bestSum2 = bestSum1 + windowSum2
                
            if bestSum2 + windowSum3 > bestSum3:
                bestIndex3 = bestIndex2 + [currIndex3]
                bestSum3 = bestSum2 + windowSum3
                
            currIndex1 += 1
            currIndex2 += 1
            currIndex3 += 1
            
        return bestIndex3

'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
'''

# Python O(N) time O(1) Space Explanation in Comments
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # there can be at most two majority elements
        # think of 3 segments: m, n, l
        # m & n is some candidate number
        # l is anything else
        # if l is longer than m, m stops being majority (majority becomes n and l)
        # elif l is longer than n, n stops being majority (majority becomes m and l)
        # elif l is same length as m & n, there's no majority
        
        # a number isn't necessarily a majority just because it survives the pair off 
        # @@ but if a number doesn't survive pair off, it definitely can't be a majority
        
        # if a number is a majority, it will always survive the pair off or come back later
        
        # key idea is that if a number is over n/3, the ratio of it versus the rest is at least 1:2 and it always comes back as a candidate
        
        m, m_count, n, n_count = 0, 0, 1, 0
        for num in nums: 
            # adds to lead of m
            if num == m:
                m_count += 1
            # adds to lead of n
            elif num == n:
                n_count += 1
            
            # l is the same length as m, because m_count == 0, so m is not a majority number now
            elif m_count == 0:
                # set a new candidate (previous candidate can always come back)
                m = num
                m_count = 1
                
            # l is the same length as n
            elif n_count == 0:
                # set a new candidate
                n = num
                n_count = 1
                
            # close the gap between l and m/n
            else:
                m_count -= 1
                n_count -= 1
        third = len(nums)/3
        res = []
        
        if m_count > 0:
            if nums.count(m) > third:
                res.append(m)
        if n_count > 0:
            if nums.count(n) > third:
                res.append(n)
        return res






        
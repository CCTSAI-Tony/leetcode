'''
An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, 
and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. 
The elements in original may be returned in any order.

 

Example 1:

Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].
Example 2:

Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.
Example 3:

Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.
 

Constraints:

1 <= changed.length <= 105
0 <= changed[i] <= 105
'''

# This problem is very similar to problem 0954. Array of Doubled Pairs. 
# The idea is that for the smallest number there is unique way to find its pair. 
# So, we sort numbers and then start from the smallest numbers, each time looking for pairs. 
# If we can not find pair, return []. The only difference, which costs me 5 minutes fine was that we need to deal with 0 as well.

# Complexity
# It is O(n log n) for time and O(n) for space.

class Solution:
    def findOriginalArray(self, arr):
        cnt, ans = Counter(arr), []
        for num in sorted(arr, key = lambda x: abs(x)):
            if cnt[num] == 0: 
            	continue
            if cnt[2*num] == 0: 
            	return []
            ans += [num]
            if num == 0 and cnt[num] <= 1: 
            	return []
            cnt[num] -= 1
            cnt[2*num] -= 1
        return ans

# 刷題用這個, time complexity O(nlogn), space complexity O(n)
# 思路: 使用 Counter 做題, 小心 num = 0 的edge case
from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        cnt, ans = Counter(changed), []
        changed.sort()
        for num in changed:
            if cnt[num] == 0:
                continue
            if cnt[2 * num] == 0:
                return []
            ans.append(num)
            if num == 0 and cnt[num] <= 1:
                return []
            cnt[num] -= 1
            cnt[2 * num] -= 1
        return ans


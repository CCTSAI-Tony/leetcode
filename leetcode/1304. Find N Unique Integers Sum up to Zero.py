'''
Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]
 

Constraints:

1 <= n <= 1000
'''

'''
Explanation:
First, take a look at a few examples:

n = 1: ans = [0]
n = 2: ans = [-1,1]
n = 3: ans = [-1,0,1]
n = 4: ans = [-2,-1,1,2]
n = 5: ans = [-2,-1,0,1,2]
So, we should return an array where the values are symmetric.
If n%2 is not equal to zero (n is odd), we append 0 to the answer list.
The maximum value is equal to n//2; and the minimum value is equal to -n//2.
So, we use a for loop; and each time we add -i and i to the answer list.
'''

# 刷題用這個, time complexity O(n), space complexity O(n)
# 思路: greedy, n = 1: ans = [0], n = 2: ans = [-1,1], n = 3: ans = [-1,0,1]
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        l = n // 2
        if n % 2:
            ans.append(0)
        for i in range(1, l+1):
            ans.append(i)
            ans.append(-i)
        return ans




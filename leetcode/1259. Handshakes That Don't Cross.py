'''
You are given an even number of people num_people that stand around a circle and each person shakes hands with someone else, 
so that there are num_people / 2 handshakes total.

Return the number of ways these handshakes could occur such that none of the handshakes cross.

Since this number could be very big, return the answer mod 10^9 + 7

 

Example 1:

Input: num_people = 2
Output: 1
Example 2:



Input: num_people = 4
Output: 2
Explanation: There are two ways to do it, the first way is [(1,2),(3,4)] and the second one is [(2,3),(4,1)].
Example 3:



Input: num_people = 6
Output: 5
Example 4:

Input: num_people = 8
Output: 14
 

Constraints:

2 <= num_people <= 1000
num_people % 2 == 0
'''


# let's take num_people = 6 for example.
# 6 people stand around a circle, they are numbered as 1,2,3,4,5,6.
# We can take any of them to launch hands shaking, let's take NO.1.
# i. 1 shakes hands with 2, left left 0 people, right left 4 people. Then we get 2 ways of hands shaking.
# ii. 1 shakes hands with 4, left left 2 people, right left 2 people. Then we get 1 way of hands shaking.
# iii. 1 shakes hands with 6, left left 4 people, right left 0 people. Then we get 2 ways of hands shaking.
# (2, 4), (4, 2), (2, 2, 2)
# With each left and right, the procedure will be applied repeatly.

# 刷題用這個, time complexity O(n^2), space complexity O(n)
# 思路: dp top down, 拆解大問題 to 小問題, 左邊握手組 當下2人握手組 右邊握手組
class Solution(object):
    def numberOfWays(self, num_people):
        """
        :type num_people: int
        :rtype: int
        """
        d = {0: 1, 2: 1, 4: 2}  # 0: 1 => 代表初始兩個握手, 只剩右邊, 要初始值 1
        for i in range(6, num_people + 1, 2):
            s = 0
            for j in range(i / 2): # 一開始1,2 握手, 求左右, 3, 4握手, 求左右, 5, 6 握手, 求左右
                left = j * 2
                right = i - left - 2
                s += d[left] * d[right]
            d[i] = s    
        return d[num_people] % (10 ** 9 + 7)




# 重寫第二次, time complexity O(n^2), space complexity O(n)
class Solution:
    def numberOfWays(self, num_people: int) -> int:
        mod = 10 ** 9 + 7
        dp = {0: 1, 2: 1, 4: 2}
        for i in range(6, num_people + 1, 2):
            s = 0
            for j in range(i // 2):
                left = j * 2
                right = i - left - 2
                s += dp[left] * dp[right]
            dp[i] = s
        return dp[num_people] % mod












'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''

# First solution is to use DP.
# Suppose dp[i] records to least number of perfect square numbers that sum up to i. And there are multiple ways for perfect square numbers to sum up to i.
# The candidate way is to add a perfect square number j*j to a sum of perfect square numbers that equals to i. 
# And it can be generized as i-j*j + j*j. So the least number of perfect square numbers that sum up to i-j*j is dp[i-j*j]. 
# So candidate answer is dp[i-j*j]+1(add one more number j*j).
# So for dp[i], we just pick the minimum of all candidates:

# dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1
# Time complexity is O(n√n). Actually running time is 2500ms.

class Solution(object):
    def numSquares(n):
        dp = [0] + [float('inf')]*n #dp[0] = 0, 其實這題可以dp = [0]*(n+1) 不影響結果
        for i in range(1, n+1):
            dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1 #ex: n = 25 output=1
        return dp[n]

#  刷題用這個 bfs
#  自己重寫 time complexity O(n√n), 192 ms
#  思路:  利用 到n有幾個perfect squre i**2, i最大為 int(n**0.5), 使用bfs, 每隔一層, n - square, 最終得到least number of perfect square numbers
#  此題bfs 可以不用visited, 因為篤定能找到答案
#  因為queue 本身就是set 可以消除當層重複, ex: 12-1-4 or 12-4-1, 若不消除會tle
#  比較trick的地方在於for node in q: 代表同一層items, 並使用另外一個nq set來收集這些q擴散的值, 當作下一層items
#  若不使用新的nq set, 那每一輪新加的物件會與舊的一層物件順序錯亂, 也就是 set.pop() pop出來的有可能是下一輪的
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        queue = set()
        queue.add(n)
        step = -1 #為了初始化=0
        while queue:
            new_queue = set()
            step += 1
            for value in queue: #當層value
                for square in squares:
                    if value < square:  #提高性能關鍵, 提早結束不適合的square, 因為square依小到大排序
                        break
                    if value == square: #最早消化完value
                        return step + 1  #提早回報所以+1    
                    new_queue.add(value-square)
            queue = new_queue


# 重寫第二次, time complexity O(n√n), space complexity O(n)
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1, int(n**0.5) + 1)]
        queue = set([n])
        steps = 0
        while queue:
            new_queue = set()
            for val in queue:
                if val == 0:
                    return steps
                for square in squares:
                    new_queue.add(val - square)
            if new_queue:
                queue = new_queue
                steps += 1
        return 0

# 刷題用這個 time complexity O(n√n), space complexity O(n)
# 思路: dp 解法, 
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
        
        dp = [float('inf')] * (n+1)
        # bottom case
        dp[0] = 0
        
        for i in range(1, n+1):
            for square in square_nums:
                if i < square:  # 優化
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)
        
        return dp[-1]


# 重寫第二次, time complexity O(n√n), space complexity O(n)
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1, int(n**0.5) + 1)]
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for square in squares:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)
        return dp[-1]


# time complexity O(n√n)
# Another solution is to use BFS.
# The root node is n, and we are trying to keep reduce a perfect square number from it each layer. 
# So the next layer nodes are {n - i**2 for i in range(1, int(n**0.5)+1)}. And target leaf node is 0, 
# indicates n is made up of a number of perfect square numbers and depth is the least number of perfect square numbers.

#  思路,這個解法不需要visited, bfs若確定一定能找到目標, 則可以不用設visited, 此題設visited會佔據很大資源
#  因為queue 本身就是set 可以消除當層重複, ex: 12-1-4 or 12-4-1
#  比較trick的地方在於for node in q: 代表同一層items, 並使用另外一個nq set來收集這些q擴散的值, 當作下一層items
#  若不使用新的nq set, 那每一輪新加的物件會與舊的一層物件順序錯亂, 也就是 set.pop() pop出來的有可能是下一輪的
                
class Solution(object):
    def numSquares(self, n):
        squares = [i**2 for i in range(1, int(n**0.5)+1)] #within the square root, why int(n**0.5)+1), zero based index issue
        d, q, nq = 1, {n}, set() #q = {n} type: set, nq也可以[]但會變慢
        while q:
            for node in q: #一輪for loop 代表一層 (node-square)
                for square in squares:
                    if node == square: 
                        return d
                    if node < square: 
                        break  #break for square in squares 這個迴圈, 提高性能關鍵, 提早結束不適合的square, 因為square依小到大排序
                    nq.add(node-square)
            q, nq, d = nq, set(), d+1

# Each while loop takes Si, which is the number of the values that is within range {1, n} whose least number of perfect squares is i. E.g. S1 = √n.
# So total time cost should be c∑Si = cS1+cS2+...+cSd. Since I used a set for queue here, 
# ∑Si ≤ n, and time complexity is O(n). The worst case would be n happen to have a larger least number of perfect square than any number from {1, n-1}. 
# Actually running time is 220ms.

#可以這麼理解 Si 就是一個數至少有幾個perfect square numbers

#S1 = 1,4,9...
#S2 = 2,3,5....

#  python Set | pop()                  
#  This method removes a random element from the set   






# 自己重寫, NAIVE BFS, time complexity O(n√n) 2612ms
# 思路:  利用 到n有幾個perfect squre i**2, i最大為 int(n**0.5), 使用bfs, 每隔一層, n - square, 最終得到least number of perfect square numbers
# 使用到visited 佔據相當大資源
from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        queue = deque()
        visited = set()
        queue.append((n, 0))
        while queue:
            for _ in range(len(queue)):
                value, step = queue.popleft()
                if value not in visited and value >= 0:
                    visited.add(value)
                    if value == 0:
                        return step
                    for square in squares:
                        queue.append((value-square, step + 1))

















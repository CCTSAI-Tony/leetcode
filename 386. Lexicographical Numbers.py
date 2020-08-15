'''
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
'''

# O(n) space complexity.
# I think a better way to calculate the complexity is that every number needs be called exactly one time. Therefore the total cost is O(n).
# Accepted python code with DFS:

    def lexicalOrder(self, n):
        def dfs(k, res):
            if k <= n:
                res.append(k)
                t = 10*k
                if t <= n:
                    for i in range(10):
                        dfs(t + i, res)
        res = []
        for i in range(1, 10):
            dfs(i, res)
        return res

# Interestingly, with only one modification to the above code, the following code gets Memory Limit Exceeded.

    def lexicalOrder(self, n):
        def dfs(k):
            if k <= n:
                res.append(k)
                t = 10*k
                if t <= n:
                    for i in range(10):
                        dfs(t + i)
        res = []
        for i in range(1, 10):
            dfs(i)
        return res


# The only difference between these two is that, in the latter one, 
# we do not pass the list res as an argument to the function dfs. Can anybody explain this phenomenon? Thanks!


# So apparently the dfs function in the second version is somewhat harder to delete and thus might stick around longer. 
# Since it references the res entry in the outer scope, I guess the list then has to stick around longer as well. 
# The first version on the other hand doesn't access the outer scope but accesses res via a local variable, which dies when dfs returns. 
# So that might be the crucial difference.

# 10 liner. iterative. O(n) time, O(1) space.

# Simple. easy to understand. No fking weird, rarely used built-int functions.


class Solution(object):
    def lexicalOrder(self, n):
        ans = [1]
        while len(ans) < n:
            new = ans[-1] * 10
            while new > n:
                new /= 10
                new += 1
                while new % 10 == 0:    # deal with case like 199+1=200 when we need to restart from 2.
                    new /= 10
            ans.append(new)    
        return ans




















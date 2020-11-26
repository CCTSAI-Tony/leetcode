'''
In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example

Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
'''

# Top Down DFS with Memoization: Time: O(N * 2^N). Space: O(2^N)

# We create an array allowed which has all the integers from 1 to maxChoosableInteger.
# We test if the input is valid or not i.e. sum(allowed) >= desiredTotal.
# How do we define the state of the game? This answer determines how we will do memoization as well. 
# Clearly list of current allowed numbers are needed to define the state. It might also look that so_far is also required to define the state. 
# However, given all allowed values and the current set of allowed values, so_far is really the difference of the sum of the two. 
# Therefore only allowed values uniquely determine the state.
# How many allowed values sets are possible? The length of the allowed value set can range 1 to maxChoosableInteger(N). 
# So the answer is (N,1) + (N,2) + ..(N,N) where (N,K) means choose K from N. This is equal to 2^N.

# Now at my turn, if the max(allowed) + so_far >= target, then I will win. Otherwise, 
# I choose from the allowed values one by one and recursively call for the other player. 
# If with any choice the opponent fails for sure, then also I can win for sure from this state.
# What is the time complexity? For a brute force solution, the game tree has 10 choices at first level, each of these choices has 9 choices at second level, 
# and so on. So the complexity is N!. But with memoization, we only compute 2^N sub-problems, and in each problem we do O(N) work. So total time complexity is O(N2^N).

#dfs backtracking + memo, time complexity O(n*2^n)
#思路: 此題的核心在於allowed array,與 so_far 選過的值的sum, 若到我的turn, max(allowed) + so_far >= target 就是這局我可以force win
#若上面條件不符合, 就dfs allowed 裡面的值, 看出什麼值, 對方不能force win, 若對方不能force win 就代表我方可以force win
#其實每局的state都是allowd裡面數字的組合, 有2^n種, 算上排列就是n!, 但不同順序出牌結果都是一樣的, 所以只要compute 2^n個 sunproblem
#此題出牌順序不同, 排列順序一樣, 因為我們是從allowed 挑牌出來不影響原本的排列
class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        allowed = [x for x in range(1, maxChoosableInteger+1)]
        if sum(allowed) < desiredTotal:
            return False
        cache = {}
        return self.helper(allowed, desiredTotal, 0, cache)


    def helper(self, allowed, target, so_far, cache):
        state = tuple(allowed)
        if state in cache:
            return cache[state]
        
        cache[state] = False #預設
        if max(allowed) + so_far >= target:
            cache[state] = True
        else:
            for x in allowed:
                new_allowed = [y for y in allowed if x!=y] #排除x, 此trun 我方選x
                if not self.helper(new_allowed, target, so_far+x, cache): #換對方的turn
                    cache[state] = True
                    break
        return cache[state]
    
    
#自己重寫, time complexity O(n*2^n), 刷題用這個 680ms 
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        allowed = [i for i in range(1, maxChoosableInteger+1)]
        if sum(allowed) < desiredTotal:
            return False
        memo = {}
        return self.dfs(allowed, 0, desiredTotal, memo)
        
    
    
    def dfs(self, allowed, so_far, desiredTotal, memo):
        if tuple(allowed) not in memo:
            memo[tuple(allowed)] = False
            if max(allowed) + so_far >= desiredTotal:
                memo[tuple(allowed)] = True
            else:
                for i in range(len(allowed)):
                    new_allowed = allowed[:i] + allowed[i+1:]
                    if not self.dfs(new_allowed, so_far + allowed[i], desiredTotal, memo):
                        memo[tuple(allowed)] = True
                        break
        return memo[tuple(allowed)]









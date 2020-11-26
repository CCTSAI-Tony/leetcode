'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.
'''

# MinMax，游戏策略，在人工智能课里讲过，还考过，然而当时真的学得太渣了，一点不会。

# 看了题解，再看了维基百科，强行解释一下吧。

# minMax对应的每次选择就是完整的一轮博弈过程：

# 我走一步，然后你走一步

# 然后我假设我走A，然后在A下我猜测你所有可能的应对方法，设这些方法中每个方法对我的伤害构成的集合B_A，我应该相信你的智商，所以我得去 B_A中最大的，即我走A后，带来的伤害是 max B_A 。 
# 然后我考虑每种走法，A_I， 其对应的伤害为max B_A_I , 因此我最后应该选择的走法是 min_{I} max B_A_I 。 这样一解释就算是清楚了。

# 再总结一下，我有K种走法，每种走法你又会有M_i种对应的手段。我非常尊重对手，认为我选择K_i方法，你就会选择对我又最大伤害的对应手段（即MAX），然后我就应该在这K中走法中选择最大伤害最小的（MIN）。

# OK，上面就是MinMax过程了。我知道下象棋是可以这么做的。然而换到这个猜数该怎么做呢？

# 看了题解，是这么一个递推：

# R[i][j] = min_{k} { k + max(R[i][k-1] , R[k+1][j]) } , i <= k <= j
# R[x][x] = 0
# 解释一下，R[i][j]就表示i到j中猜数的minMax代价。我有 j - i + 1中可能的猜法，对每个猜测k，首先付出代价k（这是题设），
# 然后轮到你说这个K对不对。你有三种对应，一种是小了，一种是大了，一种是等于。我们做最坏打算，取三种最大的代价，等于的代价是0，故直接在公式中忽略了。初始条件，对只含一个数的区间，代价为0。因为我必然猜对。

# It is actually confusing that the example shown in the problem description is not the best stragety to guess the final target number, 
# and the problem itself is asking for the lowest cost achieved by best guessing strategy.
# The example description should be updated.

# ---POSSIBLY, it can also add some example about the BEST Strategy---
# The example description should be:

# first introducebest strategyto guess:

# for one number, like 1, best strategy is 0$
# for two number, like 3,4, best strategy is 3$, which can be understood in this way: you have two way to guess: a) start by guess 4 is the target, 
# (the worst case is) if wrong, you get charged $4, then immediately you know 3 is the target number, get get charged $0 by guessing that, 
# and finally you get charged $4. b) similarly, if you start by 3, (the worst case is) if wrong, you get charged $3, 
# then you immediately know that 4 is the target number, and get charged $0 for guessing this, and finally you get charged $3. In summary:
# range ---------> best strategy cost
# 3, 4 ---------> $3
# 5, 6 ---------> $5
# ...
# for three number, the best strategy is guess the middle number first, and (worst case is) if wrong, you get charged that middle number money, 
# and then you immediately know what target number is by using "lower" or "higher" response, so in summary:
# range ---------> best strategy cost
# 3, 4, 5 ---------> $4
# 7, 8, 9 ---------> $8
# ...
# for more numbers, it can simply be reduced them into smaller ranges, and here is why DP solution make more sense in solving this.
# suppose the range is [start, end]
# the strategy here is to iterate through all number possible and select it as the starting point, say for any k between start and end, 
# the worst cost for this is: k+ max(DP( start, k-1 ), DP(k+1, end )), and the goal is minimize the cost, 
# so you need the minimum one among all those k between start and end



# I feel like this is one of the classical kind of DP problem, so here I decided wrote down the thinking process for this problem for futuer record.

# First we have following observation:

# dp[i][j]: min money we need to guarantee a win for numbers from i ->j includisve
# Following definition we can complete other typical DP components:

# init: dp = [[0 for _ in  range(n+1)] for _  in range(n + 1)], dp[i][i] = 0 for i from 0->n, @@range(n+1) 確保index n 包含在內
# transition: dp[i][j] = k + max(dp[i][k-1], dp[k+1][j]), for k = i -> j inclusive
# return: dp[1][n]
# One thing I always felt tricky is the way to iterative over dp matrix becuase for this kind of problem we need to iterative over the diag(diagonal). 
# I personally like following template:

# for start in range(1, n+1):
#     for j in range(start, n+1):
#         i = j - start
#         update dp[i][j]
# So basically we iterative over column j, and compute i from j. With above components it is trivial to write following code:




#dp[i][j] = min(i + max(dp[i+1][j],dp[i][i-1]), j + max(dp[i][j-1],dp[j+1][j])

#其中dp[i][i-1], dp[j+1][j] 均已超出i to j 的 range, 故不算進去

#接下來for k in range(i+1, j) 保證不會超出 i to j 的 range

#Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.,

#可以這樣理解, 一開始選哪個數就算之後都沒猜準總體損失最小, dp法暗示這個問題有其最佳解

# 經典 min-max, 刷題用這個
# 自己重寫, time complexity O(n^2), 修改一下space 與 j, space最多差n-1, j至少=2
# 思路: 對整段區間切分, 區間內任選一個值k, 之後依k分隔出來的兩個區間選需要花的錢比較多的, 因為目的是保證要贏=> 眾多k中選一個整體花費最少的
# dp[i][j]: min money we need to guarantee a win for numbers from i ->j inclusive
# init: dp = [[0 for _ in  range(n+1)] for _  in range(n + 1)], dp[i][i] = 0 for i from 0->n, @@range(n+1) 確保index n 包含在內
# transition: dp[i][j] = k + max(dp[i][k-1], dp[k+1][j]), for k = i -> j inclusive
# return: dp[1][n]
# 這邊start 代表差值 例如dp[1][2], dp[1][3]....為啥從1開始, 因為dp[x][x] = 0
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0 for i in range(n+1)] for j in range(n+1)] #non-zero based index 比較方便理解
        for space in range(1, n):
            for j in range(space+1, n+1):
                i = j - space
                dp[i][j] = min(i + dp[i+1][j], j + dp[i][j-1])
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], k + max(dp[i][k-1], dp[k+1][j]))
        return dp[1][n]



# 經典 min-max
# 思路: 對整段區間切分, 區間內任選一個值k, 之後依k分隔出來的兩個區間選需要花的錢比較多的, 因為目的是保證要贏=> 眾多k中選一個整體花費最少的
# dp[i][j]: min money we need to guarantee a win for numbers from i ->j inclusive
# init: dp = [[0 for _ in  range(n+1)] for _  in range(n + 1)], dp[i][i] = 0 for i from 0->n, @@range(n+1) 確保index n 包含在內
# transition: dp[i][j] = k + max(dp[i][k-1], dp[k+1][j]), for k = i -> j inclusive
# return: dp[1][n]
# 這邊start 代表差值 例如dp[1][2], dp[1][3]....為啥從1開始, 因為dp[x][x] = 0
class Solution(object):
    def getMoneyAmount(self, n):
            """
            :type n: int
            :rtype: int
            """
            dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
            for start in range(1, n+1):  #這邊start 代表差值 例如dp[1][2], dp[1][3]....為啥從1開始, 因為dp[x][x] = 0
                for j in range(start, n+1): 
                    i = j - start
                    dp[i][j] = min(i + dp[i+1][j], j + dp[i][j-1]) #邊界情況, 先猜頭尾, 避免之後 list index out of range
                    for k in range(i+1, j): #扣掉首尾的部分
                        dp[i][j] = min(dp[i][j], k + max(dp[i][k-1], dp[k+1][j])) #
            return dp[1][n]
















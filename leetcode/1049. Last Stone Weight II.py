'''
We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose any two rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the smallest possible weight of this stone (the weight is 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0 so the array converts to [1] then that's the optimal value.
 

Note:

1 <= stones.length <= 30
1 <= stones[i] <= 100
'''

@@
# Explaining why this problem is equals to finding the difference between the sum of two groups

# Suppose you have rock a, b, c and d.
# If you subtract them in the following order: b-c, then d-b-c. Then it is the same as doing d-(b+c).
# Then doing [d-(b+c)]-a is the same as -a+d-(b+c), which is d-a-(b+c), which is d-[a+(b+c)], which is d-(a+b+c). (So doing things in that order will lead to this shortcut).

# Lets try another order.
# Suppose you have rock a, b, c and d.
# If you do a-d, then b-c, then (a-d)-(b-c).
# Then (a-d)-(b-c) is the same as a-d-b+c, which is the same as -d-b+a+c, which is -(d+b)+(a+c), which is (a+c)-(d+b). Another shortcut.

# Then you can see that depending on the order of the subtractions, we get a different setting of difference between two groups.


# we could split the stones into two piles A and B, so that abs( A - B ) has a minimum value. Thus each stone is either in pile A or pile B. 
# now we simply need to figure out how to spilt the stones.
# as metioned above, each stone is only in one of the two piles, let's denote dp[i] as whether to put the i-th(starting from 0) stone in to A or B.

# if we put it into A, then for all the results that before the i-th stone, we add the weight of i-th stone to them.
# if we put it into B, then for all the results that before the i-th stone, we subtract the weight of i-th stone from them.
# keep doing this until we put the last stone into calculation. at this point, 
# we simply take a look at final results and the minimum abs value is the answer. below is the code:
# actually, we don't need to keep track of dp arrays of all the stones, only the dp array of previous stone that matters.

#刷題用這個 time complexity O(n log n)
#思路: 此題有點數學, ex: d-(a+b+c), 題目簡化成把stone 分成兩group, 並計算此兩group的差值, 不同相減順序會導致不同最終結果 => 使用dp
#若決定把該石頭放入pile a => 放入i-1 stone的相減組合都加上該i-th石頭值, 若放入pile b => 之前 i-1 stone的相減組合都減上該i-th石頭值 => 對每個相減組合結果取絕對值排序 => 最小的就是ans
class Solution:
    def lastStoneWeightII(self, stones) -> int:
        dp = [[]] #why dp = [[]] cause dp[0] need something to fill in 
        dp[0] = [stones[0],stones[0] * (-1)]  #put it into pile A or pile B
        for i in range(1,len(stones)):
            dp.append([e + stones[i] for e in dp[i - 1]] + [e - stones[i] for e in dp[i - 1]])  #注意這邊是dp.append 新增dp[i]
            dp[i] = list(set(dp[i]))  #先set化後 記得list化回來
        total = list(set(abs(e) for e in dp[-1]))  #最後把dp[-1] 每個元素取絕對值
        total.sort()  #sort() ascending order
        return total[0]



set([1,1,1,1])
{1}

#重寫第二次, time complexity O(nlogn), space complexity O(2^n)
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = []
        dp.append([stones[0], -stones[0]])
        for i in range(1, len(stones)):
            dp.append(list(set([e + stones[i] for e in dp[i - 1]] + [e - stones[i] for e in dp[i - 1]])))
        temp = [abs(e) for e in dp[-1]]
        temp.sort()
        return temp[0]





















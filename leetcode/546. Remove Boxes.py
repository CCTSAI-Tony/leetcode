'''
You are given several boxes with different colors represented by different positive numbers.

You may experience several rounds to remove boxes until there is no box left. 
Each time you can choose some continuous boxes with the same color (i.e., composed of k boxes, k >= 1), remove them and get k * k points.

Return the maximum points you can get.

 

Example 1:

Input: boxes = [1,3,2,2,2,3,4,3,1]
Output: 23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
----> [1, 3, 3, 3, 1] (1*1=1 points) 
----> [1, 1] (3*3=9 points) 
----> [] (2*2=4 points)
Example 2:

Input: boxes = [1,1,1]
Output: 9
Example 3:

Input: boxes = [1]
Output: 1
 

Constraints:

1 <= boxes.length <= 100
1 <= boxes[i] <= 100
'''

'''
dp(i,j,k) means the max points you can earn between boxes "i" and "j", with "k" boxes before i that has the same color as "i".

But there are a few important facts that are not clearly mentioned in other posts:

At the point of "dp(i,j,k)", all boxes before "i" are already removed. 
"ALL" removed, except for the "k" boxes that has same color as "i". 
So, literally, at "dp(i,j,k)" you are seeing "k+1" continuous boxes of "i" in the front.
For dp(i,j,k), we can have 2 choices, either remove box "i", or not.
If we remove box "i", then we earn the points of "i" together with "k" boxes before it. 
And the rest dp becomes "dp(i+1,j,0)". "k" becomes zero for the rest becase there are not a single box ahead anymore after removing "i".
If we don't remove box "i", then k becomes "k+1". In order to use this "k+1", 
we have to find another box that has the same color as these "k+1" boxes. 
If there is no such box, then there is no point keeping box "i". 
If there is such box, then we remove all boxes along the way until this box of same color, 
so that this box can join "k+1" and makes a pattern in #1
'''


# 刷題用這個, time complexity O(n^4), space complexity O(n^3)
# 思路: dp(i,j,k) means the max points you can earn between boxes "i" and "j", with "k" boxes before i that has the same color as "i".
# literally, at "dp(i,j,k)" you are seeing "k+1" continuous boxes of same color as "i" in the front.
# For dp(i,j,k), we can have 2 choices, either remove box "i", or not.
# If we remove box "i", then we earn the points of "i" together with "k" boxes before it. 
# And the rest dp becomes "dp(i+1,j,0)". "k" becomes zero for the rest becase there are not a single box ahead anymore after removing "i".
# If we don't remove box "i", then k becomes "k+1". 
# In order to use this "k+1", we have to find another box that has the same color as these "k+1" boxes. 
# If there is no such box, then there is no point keeping box "i". 
# If there is such box, then we remove all boxes along the way until this box of same color can rejoin to the "k + 1" previous box
# top down dp 好題!
import functools
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @functools.lru_cache(None)
        def dfs(i,j,k):
            if i>j: 
                return 0
            cnt=0
            while (i+cnt)<=j and boxes[i]==boxes[i+cnt]:
                cnt+=1
            i2=i+cnt
            res=dfs(i2,j,0)+(k+cnt)**2
            for m in range(i2+1,j+1):
                if boxes[m]==boxes[i]:
                    res=max(res, dfs(i2,m-1,0)+dfs(m,j,k+cnt)) # 先不remove i box, 因為知道後面有相同顏色的box, 想先刪除中間不同色的, 再rejoin回去
            return res
        return dfs(0,len(boxes)-1,0)


# 重寫第二次, time complexity O(n^4), space complexity O(n^3)
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        memo = {}
        def dfs(i, j, k):
            if i > j:
                return 0
            if (i, j, k) in memo:
                return memo[(i, j, k)]
            cnt = 0
            while i + cnt <= j and boxes[i + cnt] == boxes[i]:
                cnt += 1
            i2 = i + cnt
            memo[(i, j, k)] = dfs(i2, j, 0) + (k + cnt) ** 2
            for m in range(i2+1, j+1):
                if boxes[m] == boxes[i]:
                    memo[(i, j, k)] = max(memo[(i, j, k)], dfs(i2, m-1, 0) + dfs(m, j, k + cnt))
            return memo[(i, j, k)]
        return dfs(0, len(boxes) - 1, 0)

















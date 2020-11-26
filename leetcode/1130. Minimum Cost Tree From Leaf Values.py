'''
Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.  (Recall that a node is a leaf if and only if it has 0 children.)
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit integer.

 

Example 1:

Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4
 

Constraints:

2 <= arr.length <= 40
1 <= arr[i] <= 15
It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is less than 2^31).
'''

# When we check root, we find that the value of root only depends on how we divide the left arr and right arr. Thus dp(i,j) = dp(i,k) + dp(k+1,j) + value of root.
# Use the relation, and we have this dp solution.

# Python Easy DP, O(n^3) time, memorization, top down

#思路: 利用不同斷點 不斷改變結果, 計算當前節點還需要左右兩邊的dp值
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        self.memo = {}  #其實這邊不宣告全域變數一樣work, memo= {} 因為mutable
        def dp(i,j):
            if j==i:  #當j == i, dp(i,i) 不會有none-leaf 的 node, 所以return 0
                return 0
            if (i,j) not in self.memo:
                res = float('inf')
                for k in range(i+1,j+1): #不同斷點, 會得出不同的sum
                    res = min(dp(i,k-1)+dp(k,j)+max(arr[i:k])*max(arr[k:j+1]),res)  #當k = j, max(arr[i:j])*max(arr[j:j+1]),res
                self.memo[(i,j)] = res
            return self.memo[(i,j)]
        return dp(0,len(arr)-1)



# Bottom up python DP solution N^2 time, N^2 space

# Starting from the end of the array and building the tree up by increasing the interval size by decrementing L. 
# Then start R at L + 1 to build references of that side of the subtree, that will be used later as R approaches N - 1.

a = [1,2,3]
a[2:3]
[3]



class Solution:
    def mctFromLeafValues(self, arr):

    # bottom up dp solution

        N = len(arr)
        maxi = [[0 for _ in range(N)] for __ in range(N)]
        dp = [[0 for _ in range(N)] for __ in range(N)]

        # get the max in each interval
        for i in range(N):
            maxi[i][i] = A[i]
            for j in range(i + 1, N):
                maxi[i][j] = max(maxi[i][j-1], arr[j])

        for left in range(N - 2, -1, -1):  #從右邊到左邊
            for right in range(left + 1, N):  #從左邊到右邊
                dp[left][right] = float('inf')
                for i in range(left, right):   # i represents the current interval subproblem
                    dp[left][right] = min(dp[left][right], maxi[left][i] * maxi[i + 1][right] + dp[left][i] + dp[i + 1][right])

        return dp[0][N-1]

#最一開始: dp[N-2][N-1] = min(dp[N-2][N-1], maxi[N-2][N-2] * maxi[N-1][N-1] + dp[N-2][N-2] + dp[N-1][N-1])

#可以從圖想像

#maxi[left][i] * maxi[i + 1][right] 左右兩邊都會有值, 不會出現none, 符合none leaf node has 2 children

#maxi[left][i] * maxi[i + 1][right] 就是此區間新增的none leaf node  


#     24            24
#    /  \          /  \
#   12   4        6    8
#  /  \               / \
# 6    2             2   4
 

















































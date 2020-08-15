'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \\       /     /      / \\      \
     3     2     1      1   3      2
    /     /       \\                 \
   2     1         2                 3

'''

# time complexity O(n)
# 思路: dp法, dp[i] = dp[左] * dp[右], res[0] => none node, res[1] => root 
class Solution(object):
    def numTrees1(self, n):
        res = [0] * (n+1)
        res[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                res[i] += res[j] * res[i-(1+j)] #分左邊 分右邊
        return res[n]
    '''
DP bottom up

    '''
# * Okay so Approach...... we know 2 things for sure when we have 0 nodes, how many unique BST we can make
#          * just 1. right (it will be EMPTY BST)
#          * Okay so now similarly when we have 1 node how many unique BST can we make .... just 1 node sitting at Root.
#          *
#          * Now interesting thing starts at when 2 nodes are there [1,2]
#          * we can either put 2 as Root or 1 as root.... in both the cases we have 1 side empty.
#          *    2          or        1
#          *   /                      \
#          *  /                        \
#          * 1                          2
#          *
#          * Let's check [1,2,3]
#          * Keep 1 as root.                     keeping 2 as root.               keeping 3 as root.
#          *
#          *      1                   1                       2                      3        or     3
#          *       \                   \                     / \                    /               /
#          *        \                  3                    1   3                  1               2
#          *        2                 /                                             \             /
#          *         \               /                                               \           1
#          *          \             2                                                 2
#          *           3
#          *
#          *  So to get NumTrees At (N) it's a combination of Number of Combination by putting [1..........N] numbers as root.
#          *  NumTrees or G[3] = F[1, 3] + F[2, 3] + F[3,3]    where F is a function F(i=currentRoot, N=TotalNodes)
#          *
#          *                                        N u m T r e e s [3]
#          *                                      /         |          \
#          *                                   F[1,3]      F[2,3]     F[3,3]
#          *                                   /  \        /  \       /  \
#          *                                  /    \      /    \     /    \
#          *                                 G(0) G(2)  G(1)   G(1) G(2)  G(0)
#          *  General Formula:
#          *  F(i, n) = G(i-1) * G(n-i).
#          */
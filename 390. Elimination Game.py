'''
There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
$1 2 $3 4 $5 6 $7 8 $9
2 $4 6 $8
2 6
6

Output:
6
'''

#這個滿難想的, 從右往左有兩種情況, 一種會碰到head(第一個元素) remove odd, 另一種則不是 remode even
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(n, isLeft):
            if(n==1): return 1  #這個重要
            if(isLeft):  #isLeft 當作往左往右開關
                return 2*helper(n//2, 0)
    # if started from left side the odd elements will be removed, the only remaining ones will the the even i.e.
    #       [1 2 3 4 5 6 7 8 9]==   [2 4 6 8]==     2*[1 2 3 4]
            elif(n%2==1):  #touch head, the odd elements will be removed
                return 2*helper(n//2, 1)
    # same as left side the odd elements will be removed
            else:
                return 2*helper(n//2, 1) - 1
    #[1,2,3,4] == [1,3]  == 2*[1, 2] - 1
    # even elements will be removed and the only left ones will be [1 2 3 4 5 6 ]== [1 3 5]== 2*[1 2 3] - 1
            
        return helper(n, 1)


#刷題用這個
 class Solution:
    def lastRemaining(self, n: int) -> int:
        return self.helper(n,1)
    
    def helper(self, n, isLeft):
        if n == 1:
            return 1
        if isLeft:
            return 2 * self.helper(n//2, 0)
        elif n % 2 == 1:
            return 2 * self.helper(n//2, 1)
        else:
            return 2 * self.helper(n//2, 1) - 1


[1 2 3 4 5 6 7 8 9 10]==   [2 4 6 8 10]==     2*[1 2 3 4 5]

[2 4 6 8 10] == [4,8] == 4*[1 2 ]

[4,8] == [8] == 8*[1] 

[1 2 3 4 5 6 7 8 9 ]==   [2 4 6 8 ]==     2*[1 2 3 4 ]

[2 4 6 8 ] == [2,6] == 2 *(2*[1 2 ] -1) = 2([1,3])

[2,6] == [6] == 2 *(2*[2]-1)









# https://leetcode.com/problems/elimination-game/discuss/87119/JAVA%3A-Easiest-solution-O(logN)-with-explanation
# example:
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24

# Let us start with head = 1, left = true, step = 1 (times 2 each turn), remaining = n(24)

# we first move from left, we definitely need to move head to next position. (head = head + step)
# So after first loop we will have:
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 - > 2 4 6 8 10 12 14 16 18 20 22 24
# head = 2, left = false, step = 1 * 2 = 2, remaining = remaining / 2 = 12

# second loop, we move from right, in what situation we need to move head?
# only if the remaining % 2 == 1, in this case we have 12 % 2 == 0, we don't touch head.
# so after this second loop we will have:
# 2 4 6 8 10 12 14 16 18 20 22 24 - > 2 6 10 14 18 22
# head = 2, left = true, step = 2 * 2 = 4, remaining = remaining / 2 = 6

# third loop, we move from left, move head to next position
# after third loop we will have:
# 2 6 10 14 18 22 - > 6 14 22
# head = 6, left = false, step = 4 * 2 = 8, remaining = remaining / 2 = 3

# fourth loop, we move from right, NOTICE HERE:
# we have remaining(3) % 2 == 1, so we know we need to move head to next position
# after this loop, we will have
# 6 14 22 - > 14
# head = 14, left = true, step = 8 * 2 = 16, remaining = remaining / 2 = 1

# while loop end, return head











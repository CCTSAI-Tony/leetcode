'''
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. 
The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to 
determine whether you can win the game given the number of stones in the heap.

Example:

Input: 4
Output: false 
Explanation: If there are 4 stones in the heap, then you will never win the game;
             No matter 1, 2, or 3 stones you remove, the last stone will always be 
             removed by your friend.
'''

# think this thinking way can help us to solve and understand this problem quickly.

# First,Let's begin with some tries.
# when the rock is 1(win) 2(win) 3(win) 4(lose) I think everyone can do this,then we stop and think.

# After you take rock and your friend becomes "you" think it carefully
# for example. when there are 4 rocks,after your taking ,there are three situations.so your friend begin with
# 1,2,or 3
# you lose(when there are 4 rocks) = your friend win = start with(4-1),(4-2),(4-3) win

# so there must be 3 win before 1 lose

# so 4 is a group.

# in c language we just return n%

# Dynamic Programming Solution

# Just maintain the last three outcomes.

# dp[i] stores the result of the game (win or lose) when there are i stones left for the player whoever asks for it.
# So if we build from the bottom, we can always check the last 3 positions to see 
# if we can turn current number into any number from the last 3 positions that gurantees a win for us. ex: leave the other a dead-end

#這題相當不錯 dp思路看不懂請看解釋 此題dp TLE
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 3:
            return True
        win = [True]*3
        i = 4
        while i <= n:
            next_outcome = (not win[0]) or (not win[1]) or (not win[2]) # Just maintain the last three outcomes. so there must be 3 win before 1 lose
            win[0] = win[1] #i =4 往下一個outcome了
            win[1] = win[2]
            win[2] = next_outcome
            i = i + 1
        return win[-1]

# // Then, think about the question in this way: 
#     // after choosing 1 ~ 3 stones in the first round, 
#     // can we left AT LEAST ONE dead-end to another player?

#     // For 4 stones, if we choose 1 stone, there are 3 stones left;
#     // choose 2 stones, 2 stones left;
#     // choose 3 stones, 1 stone left. 
#     // This is a bad situation for us, but a good news for another player,
#     // because 1, 2, 3 stones are all not dead-ends for him.

#     // So to determine if we can win the game, we only need to care about if we can left AT LEAST ONE dead-end at first round.

#     // For example:
#     //    5 stones: choose 1 stone, left 4 stones, 4 stones is a dead-end so we win;
#     //    6 stones: choose 2 stones, left 4 stones, win again.
#     //    7 stones: choose 3 stones, left 4 stones, win again.
#     //    8 stones: after choosing 1, 2, 3 stones, we left either 5, 6, or 7 stones, and none of them are dead-ends, so we cannot win the game.
#     //    9 stones: we choose 1 stone, left 8 stones, 8 stones is a dead-end so we win...
#     //    and so on...

# d = True or False or False
# d
# True

# d = False or False or False
# d
# False

# Mathematical Answer

# Multiple of 4 will always result in loss.

#best anser
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 4 == 0:
            return False
        else:
            return True


















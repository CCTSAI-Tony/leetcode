'''
There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. 
On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the i-th round, you toggle every i bulb. 
For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Input: 3
Output: 1 
Explanation: 
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.
'''

# 思路：
# 根据题意，按全亮，2x, 3x, 4x…n轮的方式开关灯；
#   一盏灯，当且仅当其乘数轮被开关时，它会随之被开关；（举例：6=1X6或2X3，6只会随着第1,2,3,6轮开关，并且轮数大于灯位置后对灯不再有任何影响）
#   因此，一盏灯在若干轮后，它的开关状态只与其乘数的个数有关，并且，由于灯初始为关闭状态，乘数个数和为奇数的灯会被开启，乘数个数和为偶数的灯会保持关闭。
#   由上，本题可以化简成于求一个数乘积个数的问题；

# 其中，数又可分为两类：开方后可取整的数与开方后不可取整的数，设为A,B两类。
# 1.A类：乘数个数为奇数，因为它包含2n个不同数的积与1个相同数的积（如：16=1X16=2X8=4X4，乘数为2X2+1=5个），当轮数大于其位置时，始终开启；
# 2.B类： 乘数为偶数，包含2n个不同数的积，当轮数大于等于其位置时，保持关闭。

# 综上，只需要求取n中可开方数的个数即可，只有这些灯会保持常亮~

#turn off every second bulb 說的是每過兩個關掉第二個燈, 只要是二的倍數的燈都會被關掉

# There is a pattern for it
# for 1th bulb : 1
# 2nd : 1 0
# 3rd : 1 0 0
# 4th : 1 0 0 1
# 5th : 1 0 0 1 0
# 6th : 1 0 0 1 0 0
# 7th : 1 0 0 1 0 0 0
# 8th : 1 0 0 1 0 0 0 0
# 9th : 1 0 0 1 0 0 0 0 1

# Meaning the I-th bulb that is on only on when its on I**2 turn, for example if you want 2 bulb on then you will have to go to 4th round, 3 bulb on -> 9th round.
# so for (n-th round) you can get at most floor(square_root(n)) bulb.

class Solution(object):
    def bulbSwitch(self, n: int) -> int:
        return int(n**(1/2))  #很好想吧
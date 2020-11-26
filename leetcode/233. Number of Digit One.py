'''
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example:

Input: 13
Output: 6 
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
'''

# 思路:
# 最好的方法
# 這邊的weight 代表當前的數字
# 若weight为0，则1出现次数为round*base
# 若weight为1，则1出现次数为round*base+former+1
# 若weight大于1，则1出现次数为round*base+base
#
# 比如：
# 534 = （个位1出现次数）+（十位1出现次数）+（百位1出现次数）=（53*1+1）+（5*10+10）+（0*100+100）= 214
# 530 = （53*1）+（5*10+10）+（0*100+100） = 213
# 504 = （50*1+1）+（5*10）+（0*100+100） = 201
# 514 = （51*1+1）+（5*10+4+1）+（0*100+100） = 207
# 10 = (1*1)+(0*10+0+1) = 2
# 121 = (12*1+0+1) + (1*10+10) + (0*100+21+1) = 55
class Solution:
    def countDigitOne(self, n):
        if (n<1):
            print(0)

        count = 0  # 用于统计1的个数
        base = 1    # 公式里的base
        round = n   #

        while round>0:
            weight = round%10 #remainder, decide digit in ones or tens or hundreds
            round //= 10 
            count += round*base
            if weight == 1:     # 若weight为1，则1出现次数为round*base+former+1
                count += (n%base)+1
            elif weight>1:      # 若weight大于1，则1出现次数为rount*base+base
                count += base
            base *= 10
        return (count)



        
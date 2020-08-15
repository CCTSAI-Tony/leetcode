'''
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. 
Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
'''

# Scan nums only once. The stack maintains a list of disjoint intervals  (except the end point) 
# where the lower and upper bound of each interval denote the minimum and maximum in the '132' pattern respectively. 
# Thus any subsequent number which is strictly contained in any intervals in the stack will form a '132' pattern.
# The order of intervals in the stack are maintained in a way 
# such that if the right end of interval A is less than or equal to the left end of interval B, then A is above B in the stack. 
# The time complexity is O(N), since each number will at most be pushed and popped once.

# 此方法比較直覺, time complexity O(n), 刷題用這個, 找到中間值 third 並確認是否能找到 one < third < two 的關係
# 思路: subsequence 不需連續array index, 設立stack 來紀錄 disjoint intervals, interval的左邊,右邊代表 該區間的 minimum & maximum
# 解題思路: 若之後遇到的num(小於目前最大值 and 目前最小值) 在stack儲存的intervals 區間內, 代表找到132 pattern, 因為最大值, 最小值的順序 比中間值來得早
# stack = [[interval_min, interval_max]], stack[0][1] 代表目前為止的最大值, current_min 代表目前為止的最小值
# 若有num 介於這兩者之間代表有機會在其中一個interval 之間 => 找到132 pattern
# 利用while loop 先確認num 是否大於等於前一個interval 的最小值, 再確認是否小於前一個interval 的最大值, 若是 return True
# 若不是則不斷pop 出前一個interval, 直到小於前一個interval的最小值 (disjoint intervsl) or stack empty, 則新增區間 [current_min, cur]
# ex: stack[[9,15], [3,4], [1,3]], cur = 9 => stack[[9,15], [1,9] => disjoint intervals 除了end端有重疊
# num 超過目前最大值, stack 直接變成一個區間 [current_min, cur], num 小於current_min => 新增區間 [[old interval], [cur, cur]] ex: [[8, 10], [7,7]]
class Solution(object):
    def find132pattern(self, nums):
        if len(set(nums)) < 3: #不會有第三個數, 所以不會有 132 pattern
            return False
        stack = [[nums[0], nums[0]]]
        current_min = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            if curr >= stack[0][1]:  # curr >= max(nums[:i]), 因為curr不可能是中間值
                stack = [[current_min, curr]]
            elif curr < current_min:  # curr < min(nums[:i]), 新增一個interval, 因為curr不可能是中間值
                stack.append([curr, curr])
                current_min = curr
            elif curr == current_min:
                continue
            else:  #cur < stack[0][1] and cur > current_min, 有機會找到132 pattern, 要看是否curr 是否小於前一個interval_max, 若是代表找到132 pattern
                while stack and curr > stack[-1][0]:
                    if curr < stack[-1][1]:
                        return True
                    else: #curr >= stack[-1][1], pop掉前一個interval
                        stack.pop()
                stack.append([current_min, curr])
        return False

#自己重寫
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(set(nums)) < 3:
            return False
        stack = [(nums[0], nums[0])]
        cur_min = nums[0]
        for i in range(1, len(nums)):
            cur = nums[i]
            if cur > stack[0][1]: #改成 > 也可以, 因為就算 cur = stack[0][1], 在else 的 while loop 也會幫忙消除stack至empty
                stack = [(cur_min, cur)]
            elif cur < cur_min:
                stack.append((cur, cur))
                cur_min = cur
            elif cur == stack[-1][1]:
                continue
            else:
                while stack and cur > stack[-1][0]:
                    if cur < stack[-1][1]:
                        return True
                    stack.pop()
                stack.append((cur_min, cur))
        return False






# The num which is larger than the third and before third is stored in the 'stack'

#time complexity O(n), 刷題用這個
#思路: 找到中間值 third 並確認是否能找到 one < third < two 的關係
#倒序把 num 加入stack, 設立third => one < two > third and third > one
#若發現num > stack[-1], 代表發現third candidate => stack[-1] => stack.pop()
#若之後有發現num < third, 代表找到 132 pattern, num 就是one, one < two > third and one < third
#若沒有找到 < third 的 num, 直到再次發現其他third candidate, 才有可能找到 132 pattern
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        stack, third = [], float('-inf')
        for i in range(n-1,-1,-1):  #倒序
            if nums[i] < third: 
                return True
            while stack and nums[i] > stack[-1]:
                third = stack.pop() #換新的third, 一定比舊的third 大或等於, 不然就return True了
            stack.append(nums[i])
        return False

#自己重寫
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        third = float("-inf")
        n = len(nums)
        stack = []
        for i in range(n-1, -1, -1):
            if nums[i] < third:
                return True
            while stack and nums[i] > stack[-1]:
                third = stack.pop()
            stack.append(nums[i])
        return False

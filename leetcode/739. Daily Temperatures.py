'''
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. 
If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
'''

Improved from the stack solution, which iterates backwards.
We itereate forward here so that enumerate() can be used.
Everytime a higher temperature is found, we update answer of the peak one in the stack.
If the day with higher temperature is not found, we leave the ans to be the default 0.

#time complexity o(n)
#思路: 首先建立ans array, 長度為len(T) 值都設為0, 建立stack[], 利用enumerate iterate through T, 並append 該index to stack
#若目前iterate的val > T(stack[-1]), stack[-1] 的那一天需要等cur_index - stack[-1] 的天數才會變暖, 紀錄在ans裡的對應位置, pop stack[-1] 換下一個比原stack[-1]暖的日子
#利用while loop 來消除stack 裡面比你冷的日子, 注意, stack 裡面的日子 溫度都是遞減的, 若不是則前面的日子早已找到比它暖的日子 
#Monotonic stack
class Solution:
  def dailyTemperatures(self, T):
    ans = [0] * len(T)
    stack = []
    for i, t in enumerate(T):
      while stack and T[stack[-1]] < t:
        cur = stack.pop()
        ans[cur] = i - cur
      stack.append(i)

    return ans



#自己重寫, time complexity O(n), 460ms
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(T)
        for i, v in enumerate(T):
            while stack and v > T[stack[-1]]:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)
        return ans

# 重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)
        return ans



# On a single threaded CPU, we execute some functions.  Each function has a unique id between 0 and N-1.

# We store logs in timestamp order that describe when a function is entered or exited.

# Each log is a string with this format: "{function_id}:{"start" | "end"}:{timestamp}".  
# For example, "0:start:3" means the function with id 0 started at the beginning of timestamp 3.  "1:end:2" means the function with id 1 ended at the end of timestamp 2.

# A function's exclusive time is the number of units of time spent in this function.  Note that this does not include any recursive calls to child functions.

# The CPU is single threaded which means that only one function is being executed at a given time unit.

# Return the exclusive time of each function, sorted by their function id.

# Input:
# n = 2
# logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
# Output: [3, 4]
# Explanation:
# Function 0 starts at the beginning of time 0, then it executes 2 units of time and reaches the end of time 1.
# Now function 1 starts at the beginning of time 2, executes 4 units of time and ends at time 5.
# Function 0 is running again at the beginning of time 6, and also ends at the end of time 6, thus executing for 1 unit of time. 
# So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.
 

# Note:

# 1 <= n <= 100
# Two functions won't start or end at the same time.
# Functions will always log when they exit.

# Python, Straightforward with Explanation

# In a more conventional approach, let's look between adjacent events, with duration time - prev_time. 
# If we started a function, and we have a function in the background, then it was running during this time. 
# Otherwise, we ended the function that is most recent in our stack.

# 重要觀念 id較前的fn若end之前有呼叫子程序, 一定是子程序先結束才會輪到母程序結束
# 思路: 利用stack 存放fn指針, 分拆start, end 來做個別計算, 並把計算回應在ans裡, end指針的time 要 + 1
# time complexity O(n), space complexity O(n)
class Solution:
    def exclusiveTime(self, n, logs):
        ans = [0] * n
        stack = []

        for log in logs:
            fn, typ, time = log.split(':') #list unpacking
            fn, time = int(fn), int(time) #int化 fn and time

            if typ == 'start':  #只有typ == 'start', fn才會加入stack
                if stack:
                    ans[stack[-1]] += time - prev_time  #這邊prev_time 代表前一func起始時間點, stack[-1] 當作指針
                stack.append(fn)  #這邊fn_id 題目好心對應成zero based index
                prev_time = time  # 因為single threaded, prev_time可作為臨時變數來紀錄斷點且不衝突
            else:
                ans[stack.pop()] += time - prev_time + 1  #這邊用stack.pop() 因為收尾了,ans已決定, why + 1, 因為end的 time stamp = start + 1
                prev_time = time + 1

        return ans

# Two functions won't start or end at the same time. 題目說的

#自己重寫 time complexity O(n), 額外回憶與發現 python 的變數是function scope, 還有這幾行代碼有動態語言的特性 ex: pre_time 不用先定義, 要用在定義就行了
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0] * n
        for log in logs:
            fn, typ, time = log.split(":")
            if typ == "start":
                if stack:
                    res[stack[-1]] += (int(time) - pre_time)
                stack.append(int(fn))
                pre_time = int(time)
                
            elif typ == "end":
                res[stack.pop()] += (int(time) - pre_time + 1)
                pre_time = int(time) + 1
        return res


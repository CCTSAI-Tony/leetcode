'''
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. 
The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
Example 4:
Input: deadends = ["0000"], target = "8888"
Output: -1
Note:
The length of deadends will be in the range [1, 500].
target will not be in the list deadends.
Every string in deadends and the string target will be a string of 4 digits from the 10,000 possibilities '0000' to '9999'.
'''

# 刷題用這個
# 自己重寫 1060ms, 最大優化來自於 把deadends 加到 visited set 裡, 這樣查找只要O(1)
# time complexity O(10000), space complexity O(10000)
# 思路:  利用0000 每動一格 其中一個數字可以+1, or -1, 但0,9 比較特殊, 所以要特別處裡, 新的數字代表新node, 加進visited, 之後遇到visited or deadends 都要停止
# 利用bfs 來找出最短steps
from collections import deque, defaultdict
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque(["0000"])
        visited = set(deadends)
        if "0000" in visited and target != "0000":
            return -1
        visited.add("0000")
        step = -1   
        while queue:
            step += 1
            for _ in range(len(queue)):
                digits = queue.popleft()
                if digits == target:
                    return step
                for i in range(4):
                    num = digits[i]
                    prev_num = (int(num) + 10 - 1) % 10
                    next_num = (int(num) + 10 + 1) % 10
                    if digits[:i] + str(prev_num) + digits[i+1:] not in visited:
                        queue.append(digits[:i] + str(prev_num) + digits[i+1:])
                        visited.add(digits[:i] + str(prev_num) + digits[i+1:])
                    if digits[:i] + str(next_num) + digits[i+1:] not in visited:
                        queue.append(digits[:i] + str(next_num) + digits[i+1:])
                        visited.add(digits[:i] + str(next_num) + digits[i+1:])     
        return -1





   
#1404ms
#自己想的 time complexity O(10000), space complexity O(10000)
from collections import deque, defaultdict
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque(["0000"])
        visited = set()
        step = -1
        graph = defaultdict(list)
        for i in range(10):
            if i == 9:
                graph[str(i)].append("0")
                graph[str(i)].append("8")
            elif i == 0:
                graph[str(i)].append("1")
                graph[str(i)].append("9")
            else:
                graph[str(i)].append(str(i+1))
                graph[str(i)].append(str(i-1))
            
        while queue:
            step += 1
            for _ in range(len(queue)):
                digits = queue.popleft()
                if digits in deadends:
                    continue
                if digits == target:
                    return step
                for i in graph[digits[0]]:
                    if i + digits[1:] not in visited:
                        visited.add(i + digits[1:])
                        queue.append(i + digits[1:])
                for j in graph[digits[1]]:
                    if digits[0] + j + digits[2:] not in visited:
                        visited.add(digits[0] + j + digits[2:])
                        queue.append(digits[0] + j + digits[2:])
                for k in graph[digits[2]]:
                    if digits[:2] + k + digits[3:] not in visited:
                        visited.add(digits[:2] + k + digits[3:])
                        queue.append(digits[:2] + k + digits[3:])
                for l in graph[digits[3]]:
                    if digits[:3] + l not in visited:
                        visited.add(digits[:3] + l)
                        queue.append(digits[:3] + l)       
        return -1



#680ms
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0
        
        visited = set(deadends)
        
        steps = 0
        queue = deque()
        queue.append("0000")
        
        while queue:
            for _ in range(len(queue)):
                nums = queue.popleft()
                if nums == target:
                    return steps
                
                if nums in visited:
                    continue
                visited.add(nums)
                
                for idx in range(4):  #trick!
                    num = int(nums[idx])
                    next_num = (num + 10 + 1) % 10 
                    prev_num = (num + 10 - 1) % 10
                    
                    queue.append(nums[:idx] + str(prev_num) + nums[idx + 1:])
                    queue.append(nums[:idx] + str(next_num) + nums[idx + 1:])
            steps += 1
            
        return -1







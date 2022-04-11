'''
You are given n tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, 
where tasks[i] = [enqueueTimei, processingTimei] means that the ith task will be available to process at enqueueTimei and will take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains idle.
If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. 
If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
Once a task is started, the CPU will process the entire task without stopping.
The CPU can finish a task then start a new one instantly.
Return the order in which the CPU will process the tasks.

 

Example 1:

Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]
Explanation: The events go as follows: 
- At time = 1, task 0 is available to process. Available tasks = {0}.
- Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
- At time = 2, task 1 is available to process. Available tasks = {1}.
- At time = 3, task 2 is available to process. Available tasks = {1, 2}.
- Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
- At time = 4, task 3 is available to process. Available tasks = {1, 3}.
- At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
- At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
- At time = 10, the CPU finishes task 1 and becomes idle.
Example 2:

Input: tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
Output: [4,3,2,0,1]
Explanation: The events go as follows:
- At time = 7, all the tasks become available. Available tasks = {0,1,2,3,4}.
- Also at time = 7, the idle CPU starts processing task 4. Available tasks = {0,1,2,3}.
- At time = 9, the CPU finishes task 4 and starts processing task 3. Available tasks = {0,1,2}.
- At time = 13, the CPU finishes task 3 and starts processing task 2. Available tasks = {0,1}.
- At time = 18, the CPU finishes task 2 and starts processing task 0. Available tasks = {1}.
- At time = 28, the CPU finishes task 0 and starts processing task 1. Available tasks = {}.
- At time = 40, the CPU finishes task 1 and becomes idle.
 

Constraints:

tasks.length == n
1 <= n <= 105
1 <= enqueueTimei, processingTimei <= 109
'''

# 刷題用這個, time complexity O(nlogn), space complexity O(n)
# 思路: 
# Sort the tasks according to start time, remember to keep a reference to the original task index
# tasks = [[start_time, process_time, original_index], ..., ...]
# Set the current time to the first start time in the task list.
# Push all tasks whose start time is ≤ the current time into heap h.
# heapq.heappush(h, (process_time, original_index))
# Notice we don't care about start time, since we know any item pushed into
# the heap is already past it's start_time.
# Pop the first task to be processed.
# Increase the current time by the processed time.
# Repeat
# Remember to check if the heap is empty before trying to pop from it.
# If it is empty, then let the CPU sit idle.
# This just means increase the time to when the next task can be pushed into the heap.

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        i = 0
        h = []
        time = tasks[0][0]
        while len(res) < len(tasks):
            while (i < len(tasks)) and (tasks[i][0] <= time):
                heapq.heappush(h, (tasks[i][1], tasks[i][2])) # (processing_time, original_index)
                i += 1
            if h:
                t_diff, original_index = heapq.heappop(h)
                time += t_diff
                res.append(original_index)
            elif i < len(tasks):
                time = tasks[i][0]
        return res

# 重寫第二次, time complexity O(nlogn), space complexity O(n)
import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans = []
        sorted_tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        idx = 0
        time = sorted_tasks[0][0]
        heap = []
        while len(ans) < len(sorted_tasks):
            while idx < len(sorted_tasks) and sorted_tasks[idx][0] <= time:
                heapq.heappush(heap, (sorted_tasks[idx][1], sorted_tasks[idx][2]))
                idx += 1
            if heap:
                t_diff, original_idx = heapq.heappop(heap)
                ans.append(original_idx)
                time += t_diff
            elif idx < len(sorted_tasks):
                time = sorted_tasks[idx][0]
        return ans


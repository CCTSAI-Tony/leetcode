'''
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You do not need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
 

Constraints:

1 <= arr.length <= 5 * 104
-108 <= arr[i] <= 108
'''

# 刷題用這個, time complexity O(n), space complexity O(n)
# 思路: 使用bfs 來尋找最少 jumps
# 技巧: 找尋完next childrens, 記得清空graph[cur] 的list => 來減少不必要的搜索 => 不然會TLE
from collections import defaultdict, deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        graph = defaultdict(list)
        for i in range(n):
            graph[arr[i]].append(i)
        
        queue = deque([0])
        visited = set([0])
        steps = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == n-1:
                    return steps
                for nxt in graph[arr[cur]]:
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
                        
                graph[arr[cur]].clear()  # clear the list to prevent redundant search
                
                for nxt in [cur-1, cur+1]:
                    if nxt not in visited and 0 <= nxt < n:
                        visited.add(nxt)
                        queue.append(nxt)
            steps += 1
        return -1


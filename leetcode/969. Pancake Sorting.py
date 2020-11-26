'''
Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length, then reverse the order of the first k elements of A.  
We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.

Return the k-values corresponding to a sequence of pancake flips that sort A.  
Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

 

Example 1:

Input: [3,2,4,1]
Output: [4,2,4,3]
Explanation: 
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 
Example 2:

Input: [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.
 

Note:

1 <= A.length <= 100
A[i] is a permutation of [1, 2, ..., A.length]
'''

#自己想的 naive bfs TLE, time complexity O(n^n)
from collections import deque
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        visited = set()
        sortArray = tuple(sorted(A))
        visited.add(tuple(A))
        queue = deque([(tuple(A), [])])
        while queue:
            for _ in range(len(queue)):
                array, path = queue.popleft()
                if array == sortArray:
                    return path
                for i in range(1, len(array)+1):
                    newArray = array[:i][::-1] + array[i:]
                    if newArray not in visited:
                        queue.append((newArray, path + [i]))
                        visited.add(newArray)

# Detailed Explanation for This Problem

# Find the largest element A[i], reverse A[0:i+1], making the current largest at the head of the array, 
# then reverse the whole array to make A[i] at the bottom.
# Do the above again and again, finally we'll have the whole array sorted.
# eg:

# [3,1,4,2] (input array)
# [4,1,3,2] -> [2,3,1,4] (current maximum 4 is placed at the bottom)
# [3,2,1,4] -> [1,2,3,4] (current maximum 3 is placed at the bottom)
# [2,1,3,4] -> [1,2,3,4] (current maximum 2 is placed at the bottom)
# [1,2,3,4] -> [1,2,3,4] (current maximum 1 is placed at the bottom)
# done!
# Code:

# 題目條件 A[i] is a permutation of [1, 2, ..., A.length], 每個元素都不同
# 自己重寫 time complexity O(n)
# 思路: 先找到序列最大值 並反轉首元素到最大值區間的元素, 使得最大值變成首元素, 再反轉整個序列讓最大值變成最後一個=>最大值排序完成
# 之後找尋次大值一樣反轉到次大值之間的元素使次大值變成首元素, 再反轉len(array)-1 的元素, 使得次大值在倒數第二的位置 => 次大值排序完成
# 直到要排序的值變為0, 代表1-N 的實際元素皆以排序完成
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        res = []
        max_num = max(A)
        toReverse = len(A)
        while True:
            max_index = A.index(max_num)
            A = A[:max_index+1][::-1] + A[max_index+1:]
            res.append(max_index+1)
            A = A[:toReverse][::-1] + A[toReverse:]
            res.append(toReverse)
            max_num -= 1
            toReverse -= 1
            if max_num == 0:  #代表 1-N 的值都sort 完畢
                return res





class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        """
        找到最大的数字，假设它的下标是i
        反转0到i之间的数字，使得A[i]变成第一个数
        反转整个数组，让最大的数到末尾
        """
        n = len(A)
        res = []
        for i in range(n):
            cur_max = max(A[0:n-i])
            j = 0
            while A[j] != cur_max:
                j += 1
            # should reverse j+1 elements
            A[:j+1] = reversed(A[:j+1])
            res.append(j+1)
            # reverse all
            A[:n-i] = reversed(A[:n-i])
            res.append(n-i)
        return res







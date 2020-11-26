'''
In an array A containing only 0s and 1s, a K-bit flip consists of choosing a (contiguous) subarray of length K and simultaneously changing every 0 in the subarray to 1, 
and every 1 in the subarray to 0.

Return the minimum number of K-bit flips required so that there is no 0 in the array.  If it is not possible, return -1.

 

Example 1:

Input: A = [0,1,0], K = 1
Output: 2
Explanation: Flip A[0], then flip A[2].
Example 2:

Input: A = [1,1,0], K = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we can't make the array become [1,1,1].
Example 3:

Input: A = [0,0,0,1,0,1,1,0], K = 3
Output: 3
Explanation:
Flip A[0],A[1],A[2]: A becomes [1,1,1,1,0,1,1,0]
Flip A[4],A[5],A[6]: A becomes [1,1,1,1,1,0,0,0]
Flip A[5],A[6],A[7]: A becomes [1,1,1,1,1,1,1,1]
 

Note:

1 <= A.length <= 30000
1 <= K <= A.length
'''

# It is not necessary to update A every time we flip a bit.
# We do not care that every bit in A is correctly marked as a 1 or a 0 at every step.
# What we do care about is knowing how many times bit i was flipped.
# If i was flipped an even number of times, then A[i] remains the same, but if i was flipped an odd number of times A[i] = 1 - A[i].

# ✔️Optimization: Use a queue to keep track of how many times each bit was flipped.
# Numbers match the annotations in code.
# (#1) Every time a bit is flipped, append i+k-1 to the deque. This tells us that all bits from i to i+k-1 (inclusive) have been flipped.
# (#2) To determine if a bit has been flipped, check if the length of the queue is odd. The length of the queue tells us how many times bit i was flipped.
# (#3) Remove all flips that occurred before i from the queue.
# (#4) It is impossible to flip any bits that occur after len(A) - k cause it will lead to out of index

#time complexity O(n), space complexity O(n), 跟自己解法最大不同就是利用deque 來確認該位置是否翻面過 => 來確認是否要再翻一次
#思路: 利用deque 的長度來判斷該bit 是否翻過面, 若len(deque) & 1 == 1 => 翻過面, == 0 沒翻面, 
#重點思路: 若翻過面但A[i] 沒翻面時就是1 => 需要再翻一次, 若沒翻面但A[i]沒翻面是就是0 => 需要翻一次
#若執行翻面 => deque.append(i+k-1) => 告知i ~ i+k-1 區間的index都加翻一次, 到i位置時檢查deque[0] 是否小於i, 若是popleft() => 因為已與index i 無關
#定義 latest_possible_flip = len(A) - k, 因為該位置以後不能執行flip k bits => 會out of index, 若發現該位置該翻但超過 latest_possible_flip => return -1
class Solution:
    def minKBitFlips(self, A: List[int], k: int) -> int:
        latest_possible_flip = len(A) - k       # 4
        flipped = collections.deque()
        flips = 0
        for i in range(len(A)):
            if flipped and (flipped[0] < i):    # 3
                flipped.popleft()
            if len(flipped) & 1 == A[i]:        # 2 需要flip
                if i <= latest_possible_flip:   # 4
                    flips += 1
                    flipped.append(i+k-1)       # 1
                else:
                    return -1
        return flips

#自己重寫, time complexity O(n), space complexity O(n)
from collections import deque
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        flips = deque()
        latest_flip = len(A) - K
        count = 0
        
        for i in range(len(A)):
            if flips and flips[0] < i:
                flips.popleft()
            if len(flips) & 1 == A[i]:
                if i > latest_flip:
                    return -1
                flips.append(i+K-1)
                count += 1
        return count


#自己想的, tle, time complexity O(k·n) 
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        count = 0
        start = 0
        while start < len(A):
            if A[start] == 0:
                if start + K - 1 >= len(A):
                    return -1
                for j in range(start, start + K):
                    A[j] = -(A[j]-1)
                count += 1  
                
            end = start
            while end  < len(A):
                if A[end] != 1:
                    start = end
                    break
                end += 1
            if end == len(A):
                start = end
        
        return count
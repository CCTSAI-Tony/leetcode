'''
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K. , 重要K 一定是正數

If there is no non-empty subarray with sum at least K, return -1.

 

Example 1:

Input: A = [1], K = 1
Output: 1

Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3
 

Note:

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9
'''

# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/204290/Monotonic-Queue-Summary 建議看

# In general, the following "prototype" problems can be solved by monotonic queue:

# Any DP problem where A[i] = min(A[j:k]) + C where j < k <= i
# This is a sliding max/min window problem.

# The task is to return the max/min elements in some sliding window. For example, we want a running max in the sliding windows, amax = max(A[i:i+width]).

# Key observation: Given input array A, when A[l] < A[r] for l < r, then A[l] should never be retuned as the sliding max amax, once A[r] has entered the sliding window.

# So we maintain a monotonic array with index increasing and value decreasing, because smaller elements like A[l] on the left are useless.

# For example, with sliding window of fixed length 3,

# A = [3, 1, 4, 3, 8] => monotonic queue is like [3], [3, 1], [4], [4, 3], [8]

# when element 4 enters, we remove [3, 1] because they are on the left and smaller than 4, no chance being chosen as the max element.

# The head of the increasing queue is the running max!

# The only unique thing here is that we can keep the elements in the window sorted. 

# It brings great benefits because it takes O(1) to obtain the min/max element in the window.

# That's why any DP problem where A[i] = min(A[j:k]) + C for j < k <= i and some constant C can be solved by Monotonic Queue.


# Find the nearest larger element on the left
# Given array A and an element A[i], the task is to find the maximum index j < i such that A[j] > A[i]. Namely, A[j] is the nearest larger element on the left of A[i].

# Key observation: given A[k] < A[j] > A[i] for k < j < i, A[k] never become the nearest element larger than A[i] because of A[j].

# So we should have a decreasing monotonic queue here.

#以上只是再講sliding window & monotonic queue 的思路

@@
# LC862. Shortest Subarray with Sum at Least K

# Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

# Key observation: If we accumulate array A to obtain B, then B[l] <= B[r] - K indicates sum(A[l:r]) >= K. @@重要!!
# Given B[r], the problem is equivalent to finding the nearest previous element B[l] such that B[l] <= B[r] - K.

# We maintain a increasing queue here because, given a new B[i], 
# the larger element on the left are inferior than B[i] as a candidate to make some future element B[j] >= B[i] + K (j > i).  重要!!
# 左邊比B[i]大的元素可以被刪除, 因為未來 要使 B[j] >= B[i] + K, 左邊較大的元素都沒比B[i]有用都可以被忽略

# One extra optimization is that we can also pop up the element on the left side <= B[i] - K of the increasing queue (Q) because, 
# given current element B[i], if a future element B[j] > B[i], then  B[i] - K  < elements <= B[j] would be within the queue (Q) 
# after the removal of such elements <= B[i] - K; 
# Otherwise, if a future element B[j] > B[i] then it never update the final results.


# time complexity: O(N) 

#題目有說 1 <= K <= 10 ^ 9 , K 一定是正數

# Complexity:
# Every index will be pushed exactly once.
# Every index will be popped at most once.

# Time O(N)
# Space O(N)

#time complexity O(n), space complexity O(n)
#思路: 利用sliding window, monotonic queue 解題, 一開始建立sum array, 並利用monotonic的思想, 從頭遍歷sum array, 並紀錄當下元素-以前元素, 連續增長的斷點index於deque, 
# 從頭or尾 of deque pop掉不可能的candidate, 例如從尾巴 pop掉前元素大於目前的元素, 還有從前面pop掉 已經計算完可能為最短長度斷點的元素(因為之後的元素-它就絕不會比現在計算來得短)
import collections
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        Q = collections.deque([])  #monotonic deque
        
        B = [0]
        for a in A: 
            B.append(B[-1] + a)  #sum array
            
        res = float('inf')
        for i, b in enumerate(B):
            if not Q: 
                Q.append(i)  
            else:
                while Q and B[Q[-1]] > b:  #若左邊元素比自己大, 則忽略左邊元素 因為相減一定是負數, 而且之後他們已經沒機會成為最短的subarray at least k 的斷點
                            #因為目前的元素比他們小, 下一個元素-目前的元素一定比下一個元素-淘汰的元素大且長度較短,   這就是 monotonic deque 的精神
                    Q.pop()
                while Q and B[Q[0]] <= b - K:  #注意是<=
                    res = min(res, i - Q[0])  # i- Q[0] 都是B,sum array 的 index相減
                    Q.popleft()  #逐漸縮小window
                Q.append(i)  # 若not Q, 則紀錄此index, 待下一個元素判斷
        return res if res < float('inf') else -1



# Thanks for such an amazing post..I came here for "LC862. Shortest Subarray with Sum at Least K". 
# This line "the problem is equivalent to finding the nearest previous element B[l] such that B[l] <= B[r] - K" simplified the problem a lot.. 
# Thank you very much for your explanation on other problems also..
































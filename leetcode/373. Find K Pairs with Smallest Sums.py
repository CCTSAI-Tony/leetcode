'''
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence: 
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
'''

# BFS Python 104ms with comments

#   |  1     7     11
# ------------------
#  2|  3     9     12
#  4|  5     11    15
#  6|  7     13    17

# Given the matrix for [1,7,11] and [2,4,6], we can do BFS from the top-left position to expand candidates from only right cell and bottom cell. 
# we need to skip visited vertices as I used a dictionary visited. (避免重複)

#類似 single source shortest path有用到min queue概念

# runtime = m*log(h), m is len(nums1)*len(nums2), h is the maximum size of the heap.
import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []
        if len(nums1) * len(nums2) > 0:
            queue = [(nums1[0] + nums2[0], (0, 0))]
            visited = {}
            while len(ret) < k and queue:  #and queue 是防止k > total possible pairs
                _, (i, j) = heapq.heappop(queue)  #why we don't need to heaqp.heapify first? cause just only one element, and heappush will auto sort the elements
                ret.append((nums1[i], nums2[j]))
                if j + 1 < len(nums2) and (i, j + 1) not in visited:  #j + 1 < len(nums2) avoid out of index
                        heapq.heappush(queue, (nums1[i] + nums2[j + 1], (i, j + 1)))
                        visited[(i, j + 1)] = 1  #登記key
                if i + 1 < len(nums1) and (i + 1, j) not in visited:
                        heapq.heappush(queue, (nums1[i + 1] + nums2[j], (i + 1, j)))
                        visited[(i + 1, j)] = 1
        return ret

# To find out K pairs with smallest sums, we just need start from the ’root‘ [0, 0], and traverse its children with a priority queue.(變種BFS是依照priority queue 遍歷)

# Once we get K pairs or traverse the whole 'tree', we get the result.

# The beauty of this algorithm is, it works perfectly under the fact: two array are sorted. If the arrays were to be unsorted, 
# we would not be able to guarentee that the two pairs get heappushed are always larger than the pair that gets heappopped, 
# thus it would be possible that a pair that gets heappopped ealier is larger than one gets heappopped later, which would fail to produce the correct answer.






# We create a priority queue using the sum as the priority. Note that python uses a min heap so the next item you pop off of the heap 
# will be the coords with the smallest sum. We know that the smallest pair are the items at (0,0). 
# We also know that the next smallest pair must be at either (1,0) or (0,1) since the inputs are sorted. 
# Using induction you could prove that this holds for all any arbitrary coordinate, which is left to the reader.(剩下沒被遍歷到的節點)

# When we push these items onto the heap, in logarithmic time the heap will put the smallest sum at the beginning of the heap. 
# Therefore, whenever we pop something off of the heap we are guaranteed that it is the next smallest item.

# We iterate until there are no more potential pairs or we have len(ret) == k.




# I think you can define a stricter bound like m*log(h) where m is len(nums1)*len(nums2) (number of possible pairs) and h is the maximum size of the heap. 
# I don't know exactly, but h < m since you will never have every pair in the heap at any given time.

# Also, this would make the space complexity O(k+m+h) using the above definitions.



google interview

Number of subsets with zero sum
Given an array ‘arr’ consisting of integers, the task is to find the number of subsets such that their sum is equal to zero. Empty subset should also be considered.

Examples:

Input : arr[] = {2, 2, -4}
Output : 2
All possible subsets:
{} = 0
{2} = 2
{2} = 2
{-4} = -4
{2, 2} = 4
{2, -4} = -2
{2, -4} = -4
{2, 2, -4} = 0
Since, {} and {2, 2, -4} are only possible subsets
with sum 0, ans will be 2.

One simple approach is to generate all possible subsets recursively and count number of subsets with sum equals 0. Time complexity of this approach will be O(2^n).

A better approach will be using Dynamic programming.
Let’s suppose sum of all the elements we have selected upto index ‘i-1’ is ‘S’. So, starting from index ‘i’, we have to find number of subsets of the sub-array{i, N-1} with sum equals -S.
Let’s define dp[i][S]. It means number of the subset of the subarray{i, N-1} of ‘arr’ with sum equals ‘-S’.
If we are at ith index, we have two choices, i.e. to include it in the sum or leave it.
Thus, the required recurrence relation becomes
 

dp[i][s] = dp[i+1][s+arr[i]] + dp[i+1][s]



 
# Python3 implementation of above approach  
import numpy as np 
  
maxSum = 100
arrSize = 51
  
# variable to store  
# states of dp  
dp = np.zeros((arrSize, maxSum));  
visit = np.zeros((arrSize, maxSum));  
  
# To find the number of subsets  
# with sum equal to 0. 
# Since S can be negative,  
# we will maxSum to it 
# to make it positive  
def SubsetCnt(i, s, arr, n) : 
      
    # Base cases  
    if (i == n) : 
        if (s == 0) : 
            return 1;  
        else : 
            return 0;  
      
    # Returns the value  
    # if a state is already solved  
    if (visit[i][s + arrSize]) : 
        return dp[i][s + arrSize];  
  
    # If the state is not visited,  
    # then continue  
    visit[i][s + arrSize] = 1;  
  
    # Recurrence relation  
    dp[i][s + arrSize ] = (SubsetCnt(i + 1, s + arr[i], arr, n) + 
                           SubsetCnt(i + 1, s, arr, n));  
  
    # Returning the value  
    return dp[i][s + arrSize];  
  
# Driver Code 
if __name__ == "__main__" :  
  
    arr = [ 2, 2, 2, -4, -4 ];  
    n = len(arr);  
  
    print(SubsetCnt(0, 0, arr, n));  
  
# This code is contributed by AnkitRai01 


Time Complexity : O(n*S), where n is the number of elements in the array and S is the sum of all the elements.



 










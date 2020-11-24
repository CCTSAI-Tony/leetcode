'''
Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

 

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
'''

#自己想的, time complexity O(n), space complexity O(K)
#思路: 利用prefixSum 來紀錄當下的區間和, 並利用hashtable 來記錄該區間和 % K 的值, 若hashtable 一樣%K 的key有值, 則代表有dic[區間和 % K]分段區間可以被K divide
#若當下區間和 %K = 0 記得count + 1, 因為整段區間都可以被divide
from collections import defaultdict
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        for i in range(1, len(A)):
            A[i] += A[i-1]
        count = 0
        dic = defaultdict(int)
        for num in A:
            temp = num % K
            if not temp:
                count += (1 + dic[0])
            else:
                count += dic[temp]
            dic[temp] += 1
        return count


#重寫第二次, time complexity O(n), space complexity O(K)
from collections import defaultdict
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        for i in range(1, len(A)):
            A[i] += A[i-1]
        dic = defaultdict(int)
        count = 0
        for num in A:
            temp = (num % K)
            if not temp:
                count += (dic[temp] + 1)
            else:
                count += dic[temp]
            dic[temp] += 1
        return count
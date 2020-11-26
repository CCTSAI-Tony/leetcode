'''
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  
The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  
For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

 

Example 1:



Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
 

Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
'''

#自己想的 time complexity O(len(A)+ len(B)), space complexity O(len(A)+ len(B))
#思路: 2 pointer, 個別指針放在不同list遍歷, 當其中一個指針區間的起始點>另一個指針區間的終點, 另一個指針往右移尋找下一個區間, 直到兩個指針區間出現重疊
#how to get intersection, get maximum from two interval's start point, get minimum from tow interval's end point
#after getting the intersection, if one interval's end point < another's end point, the one's pointer need to move next, if equal, tow pointers move together
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        ans = []
        while i < len(A) and j < len(B):
            if A[i][0] > B[j][1]:
                j += 1
            elif A[i][1] < B[j][0]:
                i += 1
            else:
                low = max(A[i][0], B[j][0])
                high = min(A[i][1], B[j][1])
                ans.append([low, high])
                if A[i][1] < B[j][1]:
                    i += 1
                elif A[i][1] > B[j][1]:
                    j += 1
                else:
                    i += 1
                    j += 1
        return ans
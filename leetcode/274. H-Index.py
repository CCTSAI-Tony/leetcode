'''
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h @@(if h of his/her N papers have at least h citations each, )
and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
'''


#Sort
class Solution:
    def hIndex(self, citations):
        citations.sort() #sort first
        n = len(citations)
        for i in range(n):
            if citations[i] >= (n-i): #In this case h = n-i
                return n-i
        return 0

'''
For those newcomers here:
In the first code, suppose H-index is h, so we take h numbers from the end index 
which satisfy the constraints given in the question that h numbers must be at least h
In this case h = n-i 重要!!
So we just need to check, if the smallest of them all which is at index n-h = i is >= h, 
the other numbers to the right of this index automatically satisfy this constraint because they are greater
So the index satisfying citations[i] >= h
i.e. citations[i] >= n - i
'''



#O(n) space, O(n) time 沒用sort 原理跟上面一樣
class Solution:
    def hIndex(self, citations):
        n = len(citations)
        citeCount = [0] * (n+1)
        for c in citations:
            if c >= n:
                citeCount[n] += 1
            else:
                citeCount[c] += 1
        
        i = n-1
        while i >= 0:
            citeCount[i] += citeCount[i+1]
            if citeCount[i+1] >= i+1: #ex [1,1]
                return i+1
            i -= 1
        return 0













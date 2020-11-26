'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
#自己重寫 time complexity O(sum(range(n+1)))
#思路: dynamic programing 思想, 先建立每層list, 再利用上層list的值來決定下層list, 現層除了第一個與最後一個不變外,其他都是參照上層改變
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lists = []
        for i in range(numRows):
            lists.append([1]*(i+1))
            if i > 1:
                for j in range(i):
                    if j > 0:
                        lists[i][j] = lists[i-1][j-1] + lists[i-1][j]
        return lists






class Solution:
# @return a list of lists of integers
	def generate(self, numRows):
	    lists = []
	    for i in range(numRows):
	        lists.append([1]*(i+1)) #list中建lists
	        if i>1 : #第二行開始
	            for j in range(1,i): #range(1,i) 扣除首尾
	                lists[i][j]=lists[i-1][j-1]+lists[i-1][j]
	    return lists

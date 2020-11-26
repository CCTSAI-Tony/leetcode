'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lists = []
        for i in range(rowIndex+1):
            lists.append([1]*(i+1))
            if i >1:
                for j in range(1,i):
                    lists[i][j] = lists[i-1][j-1] + lists[i-1][j]
        return lists[i]
	
'''
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. 
For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. 
And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. 
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. 
And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
'''

# In this problem, I first construct a graph with each person as a node and build an edge between two nodes 
# if those two people know each other (they are direct friends). Since the matrix is symmetric, 
# I do not have to read all the values in the matrix but only half of them. 但因為太難懂所以我還是遍歷全部,差別在於如果只遍歷一半, 要多加graph[j].append(i)

time complexity O(n*n)
#思路: undirected graph, 找有幾個component, 先建立graph, 再dfs 其中一個node並把同屬一個component的其他nodes marked起來 算一個friend circle
import collections
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] == 1:
                    graph[i].append(j)
        count = 0
        visited = [False] * len(M)
        
        for i in range(len(M)):
            if visited[i] == False:
                count += 1
            self.dfs(i, graph, visited)
        
        return count
    
    
    def dfs(self, i, graph, visited):
        if visited[i]:
            return
        visited[i] = True
        for friend in graph[i]:
            self.dfs(friend, graph, visited)

# Time Complexity: O(n^2). O(n^2) to construct the graph and O(n) to run DFS, so the total is O(n^2).
# Space Complexity: O(n^2) for the worst case. O(n^2) to store the graph dictionary, if all the nodes are connected, the space is O(n^2). C n取2
# O(n) to store visit list. The space complexity of DFS is the depth of the recursion which is no more than O(n).















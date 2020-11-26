'''
Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters in A exactly K times so that the resulting string equals B.

Given two anagrams A and B, return the smallest K for which A and B are K-similar.

Example 1:

Input: A = "ab", B = "ba"
Output: 1
Example 2:

Input: A = "abc", B = "bca"
Output: 2
Example 3:

Input: A = "abac", B = "baca"
Output: 2
Example 4:

Input: A = "aabc", B = "abca"
Output: 2
Note:

1 <= A.length == B.length <= 20
A and B contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}
'''


# We can treat each string as a node. If two strings x and y differ by one swap and that swap makes x more simliar to target string B, 
# there is a directed edges between them.
# So we can build a directed graph BFS based on that to find the value of k.

# I used a function nei to generate all children node of a node x. 
# Each child node requires one swap to change from x and each child node has one character more similiar to B than x.

# Then we just perform a regular BFS. Since A and B are garuanteed to be k-similiar. We can always reach B from A.

# Can you please talk about the time complexity too? Thanks.
# My guess is nei() is O(N^2) where N is the length of the string A/B
# Overall it looks like O(N^3). Please correct me if I am wrong.

# 自己重寫, time complexity 很複雜, each string node will have n 個 neighbors, 
# Each node searched with k matches, will have at most 2^k swaps on the unmatched characters, k form 0 to n
# 思路: 典型bfs, 利用A, B 不一樣ch的位置找尋A 後面的ch 若跟B[i] 一樣則交換位置產生neighbor node, 每次修改只換一個ch, 使用bfs來看要經歷幾輪才能k-similar
from collections import deque
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        seen = set([(A)])
        queue = deque([A])
        K = 0
        while queue:
            for _ in range(len(queue)):
                node  = queue.popleft()
                if node == B:
                    return K
                for new_node in self.helper(node, B):
                    if new_node not in seen:
                        seen.add(new_node)
                        queue.append(new_node)
            K += 1
    
    def helper(self, node, B):
        i = 0
        while node[i] == B[i]:
            i += 1
        for j in range(i+1, len(B)):
            if node[j] == B[i]: #交換x[i] and x[j], 對了A, B 裡面可以有重複元素
                yield node[:i] + node[j] + node[i+1:j] + node[i] + node[j+1:]






class Solution:
    def kSimilarity(A, B):
        q, seen = [(A,0)], {A}
        for x, d in q: #用for loop 就不能像default bfs 用 for _ in range(len(q)), first in first out
            if x == B: 
                return d
            for y in self.nei(x, B):
                if y not in seen:
                    seen.add(y)
                    q.append((y,d+1))
    def nei(self, x, B):
        i = 0
        while x[i] == B[i]: #skip 相符的
            i+=1
        for j in range(i+1, len(x)):
            if x[j] == B[i]: #交換x[i] and x[j], 對了A, B 裡面可以有重複元素
                yield x[:i]+x[j]+x[i+1:j]+x[i]+x[j+1:]








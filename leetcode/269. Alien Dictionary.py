'''
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. 
You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. 
Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
'''


# Topological Sort Based Solution

# Synoposis

# The basic idea behind this problem is simple. Build a graph from the dictionary of words. Then do a topological sort of the words. 
# The meat is in the details and corner cases.
# Meaning of Lexicographically Smaller

# Understanding what lexicographically smaller really means. Notice that adjacent words in the dictionary dictate the order. 
# Letters within the word do not determine the lexicographic order. https://discuss.leetcode.com/topic/22395/the-description-is-wrong
# Building an Input Graph

# Graph is a dictionary with key as character and edge end points as a set
# Every adjacent pair of word is extracted. All their characters are added to a graph as keys
# Now every adjacent character is compared. The first non-matching character determines a relationship u -> v and is added to graph. 
# We break at this point since the remainder mis-matches do not imply any relationship.
# Notice a pair like ("wrtkj","wrt") - > this indicates no relationship since wrt match and then the smaller word is actually longer length than bigger word. 
# This needs to be reported as an error.
# build_graph method returns the graph. If an error is found, empty graph is returned.
# Topological Sort

# DFS or BFS can be used to implement topological sort. We use DFS.
# We run topological sort on each vertex.
# Topological sort requires a directed acyclic graph. If there is a cycle, we return True.
# How do we detect a cycle? We use the concept of back-edges. We maintain a visiting and visited array.
# Topological sort can be implemented using BFS as well. https://www.youtube.com/watch?v=71eHuQvSwc0


Interesting Examples

["wrtkj","wrt"] # Incorrect input
["a","b","a"] # Cycle
["wnlb"]


# 刷題用這個, time complexity O(c), space complexity O(u + min(u^2, n)), 
# c: the total length of all the words in the input list, added together. u: the total number of unique letters in the alien alphabet
# n: the total number of strings in the input list.
# 思路: bfs + topological sort, 一開始使用zip 來偵測第一相異的letter 來create graph
from collections import defaultdict, Counter, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        # Step 0: create data structures + the in_degree of each unique letter to 0.
        adj_list = defaultdict(set)
        in_degree = Counter({c : 0 for word in words for c in word})
                
        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...
        for first_word, second_word in zip(words, words[1:]): #這招學起來, zip 來串連相鄰兩item
            for c, d in zip(first_word, second_word):
                if c != d: #找尋第一個相異letter
                    if d not in adj_list[c]: #避免 in_degree[d] 重複+1
                        adj_list[c].add(d)  #重要, 加入neighbor node
                        in_degree[d] += 1 # in_degree 越大, 代表order 越後面
                    break  # out of the for-else loop
            else: # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): return ""
        
        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)
                    
        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(in_degree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output)

# 刷題用這個, time complexity O(c), space complexity O(u + min(u^2, n)), 
# 思路: dfs + topological sort
from collections import defaultdict, Counter, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:

        # Step 0: Put all unique letters into the adj list.
        reverse_adj_list = {c : [] for word in words for c in word}

        # Step 1: Find all edges and put them in reverse_adj_list.
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d: 
                    reverse_adj_list[d].append(c) # This is the reason for calling reverse_adj_list.
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): 
                    return ""

        # Step 2: Depth-first search.
        seen = {} # False = grey, True = black.
        output = []
        def visit(node):  # Return True iff there are no cycles.
            if node in seen:
                return seen[node] # If this node was grey (False), a cycle was detected.
            seen[node] = False # Mark node as grey.
            for next_node in reverse_adj_list[node]:
                result = visit(next_node)
                if not result: 
                    return False # Cycle was detected lower down.
            seen[node] = True # Mark node as black.
            output.append(node)
            return True

        if not all(visit(node) for node in reverse_adj_list):
            return ""

        return "".join(output)

#重寫第二次, time complexity O(s), space complexity O(u + min(u^2, n))
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {c : [] for word in words for c in word}
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    graph[d].append(c) # graph[d] 有可能加入重複元素, 但沒關係, 因為只要這些元素沒有產生backedge, 這些node就會遍歷完成存在seen, 這樣seen 就能skip掉重複元素
                    break
            else:
                if len(second_word) < len(first_word):
                    return ""
        
        seen = dict()
        output = []
        if not all(self.visit(node, graph, seen, output) for node in graph):
            return ""
        return "".join(output)
        
    def visit(self, node, graph, seen, output):
        if node in seen:
            return seen[node]
        seen[node] = False
        for nxt in graph[node]:
            if not self.visit(nxt, graph, seen, output):
                return False
        seen[node] = True
        output.append(node)
        return True



    




















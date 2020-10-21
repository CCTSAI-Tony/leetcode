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

# Time complexity: O(nm), space complexity: O(n), where n = len(words), and m is the length of the longest word in words.
# 思路1:此題不能用defaultdict(set) 簡化, 因為之後遍歷 dic.values 時, 會 RuntimeError: dictionary changed size during iteration
# 所以要 add_vertices 獨立method, 來登記所有letter 的key
# 思路2: 首先建立graph, 比較兩個字的哪一個letter不一樣, 不一樣的letter就有先後順序 => 建立edge(directed graph), 但有時會出現不合理情況 ex:["wrtkj","wrt"] 就直接retrun {} 
# 讓答案輸出成"", 之後dfs 遍歷graph, 利用visited(遍歷完), visiting(遍歷中), not in visited(未遍歷) 來找出是否有circle, 若有則return "", 若沒有則登錄在visited and remove該key in visiting
# order 愈大者 愈先遍歷完 愈先被放入st, 因此最後輸出st 要先reverse()
class Solution(object):
    def alienOrder(self, words):
        if words == []:
            return ""
        graph = self.build_graph(words)
        visited, visiting, st = set([]), set([]), []
        for k in graph.keys(): #dfs forest
            if k not in visited:
                if self.topo_dfs(k, graph, visited, visiting, st): #跑上來, visiting 都是空set()
                    return "" #找到circle
        st.reverse()
        return "".join(st)

    def build_graph(self, words):
        graph = {}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            if not self.add_words_to_graph(graph, w1, w2):
                return {} #出現不合理的狀況, return 空 graph
        self.add_vertices(words[-1], graph) #最後一個字沒有neighbor
        return graph

    def add_words_to_graph(self, graph, w1, w2):
        self.add_vertices(w1, graph)
        self.add_vertices(w2, graph)        
        min_length = min(len(w1), len(w2))
        found = False
        for i in range(min_length):
            if w1[i] != w2[i]: #不同的字才能比較
                graph[w1[i]].add(w2[i])
                found = True #找到造成order的letter, 離開loop
                break
        if found == False and len(w1) > len(w2): #ex: ["wrtkj","wrt"] => incorrect
            return False # "abstract", "abs" is an error. But "abs", "abstract" is perfectly fine.
        return True

    def add_vertices(self, w, graph):
        for ch in w:
            if ch not in graph:
                graph[ch] = set([])        
        return

    def topo_dfs(self, x, g, visited, visiting, st): # Return True if there is a cycle
        visiting.add(x) #正在遍歷
        for nbr in g[x]:
            if nbr in visiting: # Back-Edge!
                return True
            if nbr not in visited: #未被遍歷的node
                if self.topo_dfs(nbr, g, visited, visiting, st): #找到Back-Edge
                    return True
        visiting.remove(x) #遍歷完成 => order愈大的, 愈先遍歷完成 被加入st, 所以最後要reverse st
        visited.add(x) 
        st.append(x)
        return False

    




















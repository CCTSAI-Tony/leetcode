'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
'''

#刷題用這個
#time complexity: O(w + (nm)^2), w 指的是words全部字數 388ms
#思路: 這題就是Trie 與 backtracking 的合體
#藉由Trie 與 TrieNode 結構 來解題, 一開始就建立prefix tree, 之後再遍歷board 看是否有相對應的word在prefix tree
#技巧, backtracking 分支遍歷結束返回上層要恢復動到過的global variable, 使其上層其他分支遍歷不受影響
#在TrieNode 部分 def __init__(self): 要先寫, 裡面defaultdict才能用TrieNode變數來代表 TrieNode class, 不然會 TrieNode not defined,
#因為TrieNode clas 還未定義完全, 若有init在定義的過程會自動跳過__init__所屬的的code, 在之後呼叫該class的物件生成instance時,才會執行__init__所屬的的code
#此時因為TrieNode class已經宣告成功, 裡面defaultdict的TrieNode 就不會not defined

import collections
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
    
class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w] #建立prefix tree, collections.defaultdict(TrieNode), 建立w key, node.children[w] 就是預設 TrieNode(), 
        node.isWord = True
    
    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord
    
class Solution(object):
    def findWords(self, board, words):
        res = []
        trie = Trie()  #使用Trie 結構
        node = trie.root #是一個 TrieNode()
        for w in words: #先建立prefix tree, trie.insert(w), 每一個新word都是從最上層的TrieNode() 一路往下建
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])): #每個cell都當頭遍歷一次
                self.dfs(board, node, i, j, "", res)
        return res
    
    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path) #藉由trieNode 特性, 收集文字串
            node.isWord = False #改回false 防止重複(board 可能出現相同字元), 繼續遍歷, ex: board["a","a"] words:["a"], or 同一個node上下左右遍歷
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]): #beyond boundary
            return 
        tmp = board[i][j]
        node = node.children.get(tmp)  #查看prefix有無這個字, 若有則node成為這個word key 的 TrieNode()
        if not node:
            return 
        board[i][j] = "#" #防止再遍歷 
        self.dfs(board, node, i+1, j, path+tmp, res)
        self.dfs(board, node, i-1, j, path+tmp, res)
        self.dfs(board, node, i, j-1, path+tmp, res)
        self.dfs(board, node, i, j+1, path+tmp, res)
        board[i][j] = tmp #遍歷結束改回temp, 這招漂亮 因為動到global variable

'''
Great solution, but no need to implement Trie.search() since the search is essentially done by dfs.
'''
time complexity: O(max(n*m, w)), w 指的是words全部字數

#自己重寫第二次, 360ms, time complexity O((m*n)^2 + w), w: words 全部字數
import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        m, n = len(board), len(board[0])
        root = trie.root
        res = []
        for i in range(m):
            for j in range(n):
                self.dfs(root, board, i, j, m, n, "", res)
        return res
    
    def dfs(self, node, board, i, j, m, n, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False #避免res 裡面有重複word
        if 0 <= i < m and 0 <= j < n: 
            temp = board[i][j]
            if temp not in node.children:
                return
            board[i][j] = "#"
            node = node.children[temp]
            self.dfs(node, board, i+1, j, m, n, path+temp, res)
            self.dfs(node, board, i-1, j, m, n, path+temp, res)
            self.dfs(node, board, i, j+1, m, n, path+temp, res)
            self.dfs(node, board, i, j-1, m, n, path+temp, res)
            board[i][j] = temp

import collections
a = collections.defaultdict(int)

b = a.get(4)  #沒有這個key 所以回報None

b == None

True

b = a[4]  #建立key 4, 預設val = 0

b

0

a[5]  #建立key 5, 預設val = 0

0

a

defaultdict(int, {4: 0, 5: 0})



#自己重寫 936ms
#思路: 要小心path重複遍歷, 還有dfs 裡面的node 指針與main 裡面的node指針是不一樣的, 所以dfs裡面修改指針的指向, 不影響main node指針的指向
#我用set() visited 來防止重複遍歷, 記得往下傳参不能直接傳参visited, 不然下層的修改都會影響它, 要另建一個新的 new_visited
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.isword = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word):
        cur = self.root
        for w in word:
            cur = cur.child[w]
        cur.isword = True
        
    def search(self, pattern):
        cur = self.root
        for w in pattern:
            cur = cur.child.get(w)
            if not cur:
                return False
        return cur.isword == True
            
    
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = Trie()
        for word in words:
            tree.add(word)
        node = tree.root
        res = set() #避免重複
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, node, res, "", set())
        return res
    
    
    def dfs(self, board, i, j, node, res, path, visited):
        if 0 <= i < len(board) and 0 <= j < len(board[0]):
            if (i,j) in visited:
                return
            node = node.child.get(board[i][j])
            new_visited = visited.union({(i,j)}) #另建一個新的 new_visited
            if node:
                if node.isword == True: #若找到後就把它改成False, 就能直接避免重複答案, res 就可以不用set()
                    res.add(path + board[i][j])  #切忌這裡就return, 因為往下可能有相同prefix但更長的word
                directions = [(0,1),(0,-1),(1,0),(-1,0)]
                for d in directions:
                    x, y = i + d[0], j + d[1]
                    self.dfs(board, x, y, node, res, path + board[i][j], new_visited)

















'''
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

# 刷題用這個, 自己重寫 284ms
# BFS, Time Complexity: O(26^len(word))  Worst case here is every word transformed happens to be in the list, 
# so each transformation needs 26 * length of word
# 思路:  此題跟word ladder最不一樣的地方就是找出所有最短路徑轉換的可能性, 最大的技巧在於每層結束後才把新加入的字加入 visited裡, 
# 這樣就能確保所有可能性, queue裡的元素則是包含path來紀錄轉換的過程

from collections import deque, defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                w = word[:i] + "_" + word[i+1:]
                graph[w].append(word)
        res = []
        visited = set([beginWord])
        queue = deque()
        queue.append((beginWord, [beginWord]))
        while queue:
            layerWordSet = set()  #紀錄每層加入的新字
            for _ in range(len(queue)): #每層的iteration
                word, path = queue.popleft()
                if word == endWord:
                    res.append(path)
                    continue
                for i in range(len(word)):
                    w = word[:i] + "_" + word[i+1:]
                    for newWord in graph[w]:
                        if newWord not in visited:
                            newPath = path[:]
                            newPath.append(newWord)
                            queue.append((newWord, newPath))
                            layerWordSet.add(newWord)
            new_visited = visited.union(layerWordSet) #把每層加入的新字連集至visited, set.union() 學起來!
            visited = new_visited #把新viaited 替換舊的
            if res:  #優化, 當層找到emdWord的答案 即是所有最短的可能性
                return res   
        return res






# It seems that exit code can be simplified:

                if w == endWord: 
                    return layer[w] # return all found sequences
# We already have all sequences in the current layer, no need to iterate over them again and build another list of lists.

# Here is simplified version with some comments:




# 524ms
import collections
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
    
        wordSet = set(wordList) # faster checks against dictionary
        layer = {}
        layer[beginWord] = [[beginWord]] # stores current word(key) and all possible sequences how we got to it(value)

        while layer:
            newlayer = collections.defaultdict(list) # returns [] on missing keys, just to simplify code
            for word in layer:
                if word == endWord: 
                    return layer[word] # return all found sequences
                for i in range(len(word)): # change every possible letter and check if it's in dictionary
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord =  word[:i] + c + word[i+1:]
                        if newWord in wordSet:
                            newlayer[newWord] += [j + [newWord] for j in layer[word]] # add new word to all sequences and form new layer element
            wordSet -= set(newlayer.keys()) # remove from dictionary to prevent loops, and acts like bfs 
            layer = newlayer # move down to new layer, 若newlayer沒有新的過度字當key, 則layer 就會變 none, 便會離開while loop

        return []


核心就是理解 layer = {}，这个东西是一个dictionary， layer[结尾单词] = [ path1, path2 , path3 , ... ] ，其中每一个path都是以“结尾单词”结束的一组单词list，代表路径。
wordSet -= set(newlayer.keys()) 是保证 BFS，拿除當層遇到的new word代表搜索完畢, 不然遇到無法走到end word 的情況 while loop會出現無限迴圈
想像終點就是endword, 每一層都是動一個字到的節點, 優先遍歷的節點都是beginWord動較少的字就到達的, 每個word 都是獨特的node,
慢慢從wordset 拿掉動較少的字就到達的word, 剩下的就是真正需要動比較多的, 若無法到達需要動比較多的layer or 字 則會離開while loop 
若不拿掉動較少的字 就會出現假循環

# newlayer[newWord] += [j + [newWord] for j in layer[word]], newlayer[newWord] 原本就是[], 所以可以直接+ list, 但被加的一方 要先list化
# ex: [1] + [2] => [1, 2]
# ex: [["dog"]] + [["cog"]] => [['dog'], ['cog']]


#set 可以remove 元素
a = set([1,2,3])
b = set([1])
a-=b
a
{2, 3}



#原版
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord: 
                    res.extend(k for k in layer[w])  #這邊要注意的是 extend(k for k in layer[w]), 括號內是list comprehension, 因此為[[a],[b],[c],[d].....]
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i]+c+w[i+1:]
                            if neww in wordList:
                                newlayer[neww]+=[j+[neww] for j in layer[w]]

            wordList -= set(newlayer.keys())
            layer = newlayer
        
        print(res)
        return res

# Your input 
# "hit"
# "cog"
# ["hot","dot","dog","lot","log","cog"]

# stdout [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]

# Output [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

# 注意這邊很有趣 extend() 裡面可以是list comprehension, 且不需要被[]包覆, 但append() 裡面則是需要被[]包覆 才能把元素表現出來
# a = []
# a.extend(i for i in [[1],[2],[3]])
# a
# [[1], [2], [3]]

# a = []
# a.append(i for i in [[1],[2],[3]])
# a
# [<generator object <genexpr> at 0x108094750>]

# a = []
# a.append([i for i in [[1],[2],[3]]])
# a
# [[[1], [2], [3]]]


#有趣的reference issue
res = []
a = [1,2,3]
b = a[:]
b.append(4)
res.append(b)
b = a[:]  #b 指針指向新的 copy list
b.append(5)
res.append(b)
res
[[1, 2, 3, 4], [1, 2, 3, 5]]
b[0] = 100 #此時的b 是指向最後一組append to res 的元素
res
[[1, 2, 3, 4], [100, 2, 3, 5]]



set 技巧, 利用 -= 大量取消交集set裡面元素(可以 -= set不存在的元素), 但不能+=連集元素
a = {1,2,3,4,5,6,7}
b = set([4,5])
a-=b
a
{1, 2, 3, 6, 7}

a = {1,2,3,4,5,6,7}
b = {9,10}
a -= b
a
{1, 2, 3, 4, 5, 6, 7}

remove 一次只能取消交集一個元素
a = {1,2,3,4,5,6,7}
a.remove(5)
a
{1, 2, 3, 4, 6, 7}

set.union() 生成一個新set 連集其他元素
a = {1,2,3,4,5,6,7}
a.union({8,9,10})
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a
{1, 2, 3, 4, 5, 6, 7}  #原set保持不變
































'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''
'''
b = set('3')
b.add(3)
b
{'3', 3}
'''

# 刷題用這個 Time Complexity: O(M^2*N), where M is the length of each word and N is the total number of words in the input word list.
# 自己重寫, 建立graph, , space complexity O(M^2*N)
#思路: 最短距離就要想到bfs, 並把它連結graph, 此題重點就是建立graph, 找尋建立連結其他字(vertex)的方法
#利用一個字不同位置切分當作key, 會對應許多字, 這些字就是鄰居, 彼此只差一個字, 利用bfs遍歷找出到endWord 最短距離, 記得設visited 以防重複遍歷
#Note, for each of M intermediate words we save the original word of length M. This simply means, for every word we would need a space of M^2
 
from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                s = word[:i] + "_" + word[i+1:]  #關鍵, 建立不同切分的狀態: 對應有哪些字
                graph[s].append(word)
        
        return self.bfs(beginWord, endWord, graph)
    
    def bfs(self, beginWord, endWord, graph):
        queue, visited = deque(), set(beginWord) #一開始就加入beginword
        queue.append((beginWord, 1))
        while queue:
            for _ in range(len(queue)):
                word, step = queue.popleft()
                if word == endWord:
                    return step
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    for nextWord in graph[s]:  #在字典種查找
                        if nextWord not in visited:  #避免重複
                            visited.add(nextWord)  #登錄
                            queue.append((nextWord, step + 1))
        return 0













#重寫第二次, time complexity O(m^2*n), space complexity O(m^2*n), where M is the length of each word and N is the total number of words in the input word list.
from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                temp = word[:i] + "_" + word[i+1:]
                graph[temp].append(word)
        queue, visited = deque([beginWord]), set([beginWord])
        step = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return step
                for i in range(len(word)):
                    temp = word[:i] + "_" + word[i+1:]
                    for nxt in graph[temp]:
                        if nxt not in visited:
                            queue.append(nxt)
                            visited.add(nxt)
            step += 1
        return 0




from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        L = len(beginWord)
        all_combo_dict = defaultdict(list) #build a dict
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word) #建立值 也可以 all_combo_dict[word[:i]+"*"+word[i+1:]] += [word]
        queue = deque([(beginWord, 1)]) #tuple
        visited = set(beginWord)
        while queue:
            current_word, level = queue.popleft() #bfs
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                for word in all_combo_dict[intermediate_word]: #在字典中查找
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1)) #進入下一層 也可以 queue += [(word, level+1)] !!不能只用+ 
        return 0

'''
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5

Only one letter can be changed at a time.
In the example, from begin word, you can change one letter in 3 ways. 3 is the length of the word.

                 hit
		   /      |      \
		   *it   h*t   hi*
		 /|\     /|\     /|\ 
# In order to continue the  Breath First Search(BFS) process,
# we need to know the children of *it, h*t, and hi*.
# so we need the information from word list.

Each transformed word must exist in the word list.
In the example, we need to record all the possible changes that could be made from the word list 
so that we can have the information to do BFS in the graph above. We use a map to store the data. 
The key is one-letter-change-word, for example," *it," the value is the word meet the key's condition in the word list.

wordList = ["hot","dot","dog","lot","log","cog"]
change_map ={ *ot : hot, dot, lot
			h*t : hot
			ho* :hot
			d*t : dot
			do* : dot, dog
			*og : dog, log, cog
			d*g : dog
			l*t : lot
			lo* : lot, log
			l*g : log
			c*g: cog
			co* : cog 
			}

With the information in change_map, we got the information to expand the breadth first search tree.

                                            hit, level = 1
							/                |                   \
					     *it                h*t                  hi*
						   |                 |                     |     
			             null  	            hot ,level = 2         null
								 /           |       \    
								/            |        \
				               *ot           h*t      ho*
				           /    |   \         |        |
                     hot,2   dot,3  lot,3   hot,2    hot,2			

# as we can see,  "hot" has been visited in level 2, but "hot" will still appear at the next level. 
# To avoid duplicate calculation, 
# we keep a visited map,  
# if the word in the visited map, we skip the word, i.e. don't append the word into the queue.
# if the word not in the visited map, we put the word into the map, and append the word into the queue.		

'''

'''
@@default_factory 接收一个工厂函数作为参数, 例如int str list set等.
defaultdict在dict的基础上添加了一个missing(key)方法, 在调用一个不存的key的时候, defaultdict会调用__missing__, 返回一个根据default_factory参数的默认值, 所以不会返回Keyerror.

s = 'mississippi'
d = defaultdict(int)
for k in s:
  d[k] += 1
print(d)

defaultdict(<class 'int'>, {'m': 1, 'i': 4, 's': 4, 'p': 2})

一般dict用法
s = 'mississippi'
d = {}
for k in s:
  d[k] = d.get(k,0) + 1 利用get先建立預設值0
print(d)
{'m': 1, 'i': 4, 's': 4, 'p': 2}



from collections import defaultdict
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
  d[k].add(v)
 
print(d)

defaultdict(<class 'set'>, {'red': {1, 3}, 'blue': {2, 4}})

from collections import defaultdict
d1 = dict()
d2 = defaultdict(list)
print(d1['a'])  -> KeyError: 'a'
print(d2['a'])  -> []
'''


        

'''
word_list = ["hot","dot","dog","lot","log","cog"]
d = {}
for word in word_list:
    for i in range(len(word)):
        s = word[:i] + "_" + word[i+1:]
        d[s] = d.get(s, []) + [word] ->key建立[]預設值 才能+[word]
print(d) 

{'_ot': ['hot', 'dot', 'lot'], 'h_t': ['hot'], 'ho_': ['hot'], 'd_t': ['dot'], 'do_': ['dot', 'dog'],
 '_og': ['dog', 'log', 'cog'], 'd_g': ['dog'], 'l_t': ['lot'], 'lo_': ['lot', 'log'], 'l_g': ['log'], 'c_g': ['cog'], 'co_': ['cog']}

Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。

dict.get(key, default=None)

dict = {'Name': 'Zara', 'Age': 27}

print "Value : %s" %  dict.get('Age')
print "Value : %s" %  dict.get('Sex', "Never")

Value : 27
Value : Never
'''

































'''
Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). 
For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed. 
Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, 
you need to use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, then just return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
Your job is to implement the following functions:

The constructor function:

AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. 
Sentences is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. 
Your system should record these historical data.

Now, the user wants to input a new sentence. The following function will provide the next character the user types:

List<String> input(char c): The input c is the next character typed by the user. 
The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). 
Also, the previously typed sentence should be recorded in your system. 
The output will be the top 3 historical hot sentences that have prefix the same as the part of sentence already typed.

 
Example:
Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
The system have already tracked down the following sentences and their corresponding times:
"i love you" : 5 times
"island" : 3 times
"ironman" : 2 times
"i love leetcode" : 2 times
Now, the user begins another search:

Operation: input('i')
Output: ["i love you", "island","i love leetcode"]
Explanation:
There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. 
Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". 
Also we only need to output top 3 hot sentences, so "ironman" will be ignored.

Operation: input(' ')
Output: ["i love you","i love leetcode"]
Explanation:
There are only two sentences that have prefix "i ".

Operation: input('a')
Output: []
Explanation:
There are no sentences that have prefix "i a".

Operation: input('#')
Output: []
Explanation:
The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.

 
Note:

The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words.
The number of complete sentences that to be searched won't exceed 100. The length of each sentence including those in the historical data won't exceed 100.
Please use double-quote instead of single-quote when you write test cases even for a character input.
Please remember to RESET your class variables declared in class AutocompleteSystem, as static/class variables are persisted across multiple test cases. 
Please see here for more details.
'''


#刷題用這個, 712ms
#思路: 利用trie 搭配 hot 來做search 與 排序
from collections import defaultdict
class TrieNode():
    def __init__(self):
        self.isEnd = False
        self.children = defaultdict(TrieNode)
        self.hot = 0 #多加這個參數
    
class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.searchTerm = ""
        # 1. add historical data
        for i, sentence in enumerate(sentences):
            self.add(sentence, times[i]) #用到自己的instance method

    def input(self, c):
        if c != "#":
            # 5. if input is not "#" add c to self.searchTerm and do self.search each time
            self.searchTerm +=c
            return self.search()
        
        else:
            self.add(self.searchTerm, 1)
            self.searchTerm ="" #reset searchTerm
            
    def add(self,sentence, hot):
        node = self.root
        #2. for each character in sentence
        for c in sentence: 
            node = node.children[c]
        #3. when last character is added,
        #   make node.isEnd = True indicate that the current node is end of the sentence
        node.isEnd = True
        #4. do -= because by negating, we can sort as ascending order later, minheap
        node.hot -= hot
        
    def search(self):
        node = self.root
        res = []
        path = ""

        for c in self.searchTerm:
            if c not in node.children:
                return res # return [], empty list
            # 6. add each character to path variable, path will added to res when we found node.isEnd ==True
            path += c
            node = node.children[c]
        # 7. at this point, node is at the given searchTerm.
        # for ex. if search term is "i_a", we are at "a" node.
        # from this point, we need to search all the possible sentence by using DFS
        self.dfs(node, path, res)
        # 11. variable res has result of all the relevant sentences
        # we just need to do sort and return [1] element of first 3
        return [item[1] for item in sorted(res)[:3]] 
            
    def dfs(self,node, path, res):
        # 8. Check if node is end of the sentence
        # if so, add path to res
        if node.isEnd:
            # 9. when add to res, we also want to add hot for sorting, and put node.hot it first for sort priority issue
            res.append((node.hot, path))
        # 10. keep going if the node has child
        # until there is no more child (reached to bottom)
        for c in node.children:
            self.dfs(node.children[c], path+c, res)

#重寫第二次
from collections import defaultdict
class TreeNode:
    def __init__(self):
        self.children = defaultdict(TreeNode)
        self.isEnd = False
        self.hot = 0

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TreeNode()
        self.term = ""
        for sentence, time in zip(sentences, times):
            self.add(sentence, time)
    
    def add(self, sentence, hot):
        node = self.root
        for c in sentence:
            node = node.children[c]
        node.isEnd = True
        node.hot -= hot
        
    def dfs(self, node, path, res):
        if node.isEnd:
            res.append((node.hot, path))
        for c in node.children:
            self.dfs(node.children[c], path + c, res)
        
    def search(self):
        node = self.root
        res = []
        path = ""
        for c in self.term:
            if c not in node.children:
                return res
            path += c
            node = node.children[c]
        self.dfs(node, path, res)
        return [item[1] for item in sorted(res)][:3]
        
        
    def input(self, c: str) -> List[str]:
        if c != "#":
            self.term += c
            return self.search()
        else:
            self.add(self.term, 1)
            self.term = ""



#自己想的, 932ms
#思路: 利用Trie 解題, 此題2個重點, 1, 排序priority (hot degree, lexicograph) 2, 遇到"#" 要insert self_term 並 update node.top3 的elements
#如何remove 舊的top3 elements, 並插入一個新的是一個重點, 設一個memo 來紀錄每個sentence 的hot degree, 用以update node.top3
#之後return search結果, 直接回傳node.top3 前三個elements
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.top3 = []

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.term = ""
        self.memo = {}
        history = zip(sentences, times)
        for sentence in history:
            self.memo[sentence[0]] = sentence[1]
            node = self.root
            self.dfs(sentence, node)
    
    def dfs(self, sentence, node):  #dfs time complexity O(k*nlogn), k: len(sentence[0]), n:len of node.top3
        for w in sentence[0]:
            node = node.children[w]
            pre_sentence = (sentence[0], (sentence[1]-1)) # tuple 以利排序
            if pre_sentence in node.top3:
                node.top3.remove(pre_sentence)
            node.top3.append(sentence)
            node.top3.sort(key=lambda x: (-x[1], x[0]))
         
    def input(self, c: str) -> List[str]:
        node = self.root
        if c != "#":
            self.term += c
            for w in self.term:
                node = node.children[w]
            return [i[0] for i in node.top3][:3]
        else:
            if self.term not in self.memo:
                self.dfs((self.term, 1), node)
                self.memo[self.term] = 1 #紀錄self.term
            else:
                self.memo[self.term] += 1
                sentence = (self.term, self.memo[self.term])
                self.dfs(sentence, node)
            self.term = "" #reset






    



























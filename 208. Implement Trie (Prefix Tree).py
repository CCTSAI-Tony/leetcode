'''
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''

#自己重寫
#思路: 典型Trie 結構, 建議背起來, 利用defaultdict 能省下很多事

from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode) #設置difaultdict key's value 可以接收TrieNode
        self.is_word = False #標誌

        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for w in word:
            cur = cur.child[w]
        cur.isword = True
        
            
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for w in word:
            cur = cur.child.get(w)
            if not cur:
                return False
        return cur.isword
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for w in prefix:
            cur = cur.child.get(w)
            if not cur:
                return False
        return True



from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode) #設置difaultdict key's value 可以接收TrieNode
        self.is_word = False #標誌
        
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        
        cur = self.root #回到根節點 最上層的TrieNode
        for w in word:
            cur = cur.child[w] #字典中的字典 行為似listnode 請看https://blog.csdn.net/fuxuemingzhu/article/details/79388432
                   #當層建立key:value pair, 再往下建立
        cur.is_word = True #完成字符串的節點 留下標誌
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for char in word:
            cur = cur.child.get(char) #get char key's value
            if not cur:
                return False
        return cur.is_word #回報是不是生成一個詞
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for char in prefix:
            cur = cur.child.get(char)
            if not cur:
                return False
        return True #若是prefix 一路都可以找到cur

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)



# from collections import defaultdict

# >>> s = 'mississippi'
# >>> d = defaultdict(int)
# >>> for k in s:
# ...     d[k] += 1
# ...
# >>> d.items()

# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# >>> d = defaultdict(list)
# >>> for k, v in s:
# ...     d[k].append(v)
# ...
# >>> d.items()
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

# a = {'1': 1, '2': 2}
# b = a.get('4')
# b == None
# True
# ccs
# 1、字符串检索
# 检索/查询功能是Trie树最原始的功能。思路就是从根节点开始一个一个字符进行比较：

# 如果沿路比较，发现不同的字符，则表示该字符串在集合中不存在。
# 如果所有的字符全部比较完并且全部相同，还需判断最后一个节点的标志位（标记该节点是否代表一个关键字）。

# 我们这里只来实现第一种方法，这种方法实现起来简单直观，字母的字典树每个节点要定义一个大小为 26 的子节点指针数组，然后用一个标志符用来记录到当前位置为止是否为一个词，
# 初始化的时候讲 26 个子节点都赋为空。那么 insert 操作只需要对于要插入的字符串的每一个字符算出其的位置，然后找是否存在这个子节点，若不存在则新建一个，
# 然后再查找下一个。查找词和找前缀操作跟 insert 操作都很类似，不同点在于若不存在子节点，则返回 false。查找次最后还要看标识位，而找前缀直接返回 true 即可。







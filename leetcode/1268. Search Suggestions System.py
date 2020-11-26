'''
Given an array of strings products and a string searchWord. 
We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. 

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
Example 4:

Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
 

Constraints:

1 <= products.length <= 1000
There are no repeated elements in products.
1 <= Σ products[i].length <= 2 * 10^4
All characters of products[i] are lower-case English letters.
1 <= searchWord.length <= 1000
All characters of searchWord are lower-case English letters.
'''


Trie + Sort
Sort
n = number of charcters in the products list
N: number of prodeuct in products
Time: O(nlog(N)) 重要!
Build Trie
k = 3
m = number of characters in the longest product
Time: O(n)
Space: O(nkm)
Output Result
s = number of characters in searchword
Time: O(s)
Space: O(sk)
#time complexity O(nlog(N))
#思路: 利用Trie 來解題, 一開始對products sort, 因為之後要依序把product 埋到Trie結構裡
#此題重點, 利用TrieNode 的 suggestion的特性 把最先經過此TrieNode 的三個product 收進裡面
#因此之後searchWord 經過此TrieNode 可以立即知道suggestion list
import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.suggestion = [] #這裡比較特別
    
    def add_sugestion(self, product):
        if len(self.suggestion) < 3:
            self.suggestion.append(product)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products) #先排序, 之後建立Trie 每個node節點 優先存入三個 lexicographycal order較小的前三個product
        root = TrieNode() #最上層TrieNode
        for p in products:
            node = root
            for char in p:
                node = node.children[char]
                node.add_sugestion(p)
        
        result, node = [], root
        for char in searchWord:
            node = node.children[char]
            result.append(node.suggestion)
        return result


#自己重寫 time complexity O(nlog(N)), n: total length in characters in products, N: length of products, 248ms
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.suggestion = []
        
    def addSuggestion(self, product):
        if len(self.suggestion) < 3:
            self.suggestion.append(product)
            
            
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        root = TrieNode()
        for product in products:
            node = root
            for w in product:
                node = node.children[w]
                node.addSuggestion(product)
        res = []
        node = root
        for w in searchWord:
            node = node.children[w] #進入下一個children節點
            res.append(node.suggestion)
        return res

























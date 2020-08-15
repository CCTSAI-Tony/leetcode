'''
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
'''

#time complexity O(n log n)
class Solution:
    def topKFrequent(self, words, k):
        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1
        
        ret = sorted(d, key=lambda word: (-d[word], word))
        
        return ret[:k]

# d[word] is the frequency of the word, so -d[word] means that sorting is reverse with the negative sign.
# And, the word behind means that if their -d[word] are equal, they will compare their alphabetical orders, as mentioned in the problem.


#自己重寫, time complexity O(nlogn)
# 思路: 利用counter 與 heapq 來pop 出 k frequent words, 注意, heapq 對tuple 排序, 會自動對elements 做lexicographical 排序
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequent_words = Counter(words)
        res = []
        heap = [(-v, i) for i,v in frequent_words.items()]
        heapq.heapify(heap)
        for _ in range(k):
            temp = heapq.heappop(heap)
            res.append(temp[1])
        return res

 





#time complexity: n(logk)
#思路: 利用自創class 來建立自己的排序規則, 之後進去heap排序就依照此規則, 要學起來
#保持heap 裡面元素控制在k個元素大小, 超過即對排序較小的pop
import collections
import heapq
class Solution:
    # Time Complexity = O(n + nlogk)
    # Space Complexity = O(n)
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = []
        for key, value in count.items():
            heapq.heappush(heap, Word(value, key))
            if len(heap) > k:
                heapq.heappop(heap)  #heap: min priority, 排除頻率較小的 or 字母排序較高的
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap).word)
        return res[::-1]

class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    
    def __lt__(self, other):  # 另一個是 __gt__(self, other)
        if self.freq == other.freq:
            return self.word > other.word  #在這裡若字母排序較大者,會被視為小於操作,在heap裡 優先被放在前面
        return self.freq < other.freq  #小於比較是基於頻率來比較
   
    def __eq__(self, other):  #__eq__其實不需要
        return self.freq == other.freq and self.word == other.word

#. If two words have the same frequency, then the word with the lower alphabetical order comes first. 

# 于比较的魔术方法
# Python对实现对象的比较，使用魔术方法进行了大的逆转，使他们非常直观而不是笨拙的方法调用。而且还提供了一种方法可以重写Python对对象比较的默认行为(通过引用)。以下是这些方法和他们的作用。

# __cmp__(self, other) __cmp__ 是最基本的用于比较的魔术方法。它实际上实现了所有的比较符号(<,==,!=,etc.)，
# 但是它的表现并不会总是如你所愿(比如，当一个实例与另一个实例相等是通过一个规则来判断，而一个实例大于另外一个实例是通过另外一个规则来判断)。
# 如果 self < other 的话 __cmp__ 应该返回一个负数，当 self == other 的时候会返回0 ，而当 self > other 的时候会返回正数。
# 通常最好的一种方式是去分别定义每一个比较符号而不是一次性将他们都定义。但是 __cmp__ 方法是你想要实现所有的比较符号而一个保持清楚明白的一个好的方法。

# __eq__(self, other) 定义了等号的行为, == 。

# __ne__(self, other) 定义了不等号的行为, != 。

# __lt__(self, other) 定义了小于号的行为， < 。

# __gt__(self, other) 定义了大于等于号的行为， >= 。

# 举一个例子，创建一个类来表现一个词语。我们也许会想要比较单词的字典序(通过字母表)，通过默认的字符串比较的方法就可以实现，
# 但是我们也想要通过一些其他的标准来实现，比如单词长度或者音节数量。在这个例子中，我们来比较长度实现。以下是实现代码:

# class Word(str):
# '''存储单词的类，定义比较单词的几种方法'''

#     def __new__(cls, word):
#         # 注意我们必须要用到__new__方法，因为str是不可变类型
#         # 所以我们必须在创建的时候将它初始化
#         if ' ' in word:
#             print "Value contains spaces. Truncating to first space."
#             word = word[:word.index(' ')] #单词是第一个空格之前的所有字符
#         return str.__new__(cls, word)

#     def __gt__(self, other):
#         return len(self) > len(other)
#     def __lt__(self, other):
#         return len(self) < len(other)
#     def __ge__(self, other):
#         return len(self) >= len(other)
#     def __le__(self, other):
#         return len(self) <= len(other)
# 现在，我们创建两个 Words 对象(通过使用 Word('foo') 和 Word('bar') 然后通过长度来比较它们。注意，我们没有定义 __eq__ 和 __ne__ 方法。
#     这是因为将会产生一些怪异的结果(比如 Word('foo') == Word('bar') 将会返回true)。这对于测试基于长度的比较不是很有意义。所以我们退回去，用 str 内置来进行比较。

# 现在你知道你不必定义每一个比较的魔术方法从而进行丰富的比较。标准库中很友好的在 functiontols 中提供给我们一个类的装饰器定义了所有的丰富的比较函数。
# 如果你只是定义 __eq__ 和另外一个(e.g. __gt__, __lt__,etc.)这个特性仅仅在Python 2.7中存在，但是你如果有机会碰到的话，那么将会节省大量的时间和工作量。
# 你可以通过在你定义的类前放置 @total_ordering 来使用。

#自己重寫
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequent_words = Counter(words)
        heap = []
        res = []
        for i, v in frequent_words.items():
            heapq.heappush(heap, Word(v, i))
            if len(heap) > k:
                heapq.heappop(heap)
        for _ in range(k):
            res.append(heapq.heappop(heap).word)
        return res[::-1]
    
class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
        
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
















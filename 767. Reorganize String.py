'''
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
'''

# Algorithm

# Say most frequently occuring character (say c) has frequency max_freq. Then arrange c leaving a space between consecutive c's. 
# The remaining characters should be more than the number of spaces for a valid arrangement. This means that max_freq + (max_freq-1)   <=   len(S). 
                                                                                                                    number of spaces      remaining characters
# We can test this quickly using Counter class from collections module and using the mostcommon(i) method which returns a list i most frequent tuples.
# Now we create an array called result to store the result. 
# We add (freq*-1,char) tuples to a heap (this is how we simulate a max-heap in Python using a min-heap. 
# We then pick the most frequent element and if that element is not the last element in the result, we add it to result, 
# If it is the last element of the result, then we pick the second most frequent element and add that to the result, 
# and also add back the most frequent element back to the heap. Note when we pop from the heap and utilize the character in the result, 
# we need to add it back to the heap if the frequency is not -1 (-1 means that only one instance of that element was in the heap and we have now used it, 
# so no need to add it back).
# Time Complexity is O(N * lg(A)). N is the length of the string. A is the size of the alphabet. The size of the heap will be at-most A. 
# But since we remove and add back elements such that at each iteration we only add one character to the result, there will be N * lg(A) calls. 
# Since A is fixed, we can assume complexity to be O(N).
# Space is also O(A).

#heap 
#思路: 優先把頻率高的element 加到result,若元素==result[-1] 則加入頻率次高的, 整題最重要觀念 max_freq+(max_freq-1)<=len(S). 
#交互加入保證相鄰不一樣, Alternate placing the most common letters. 所以用到heap
#為什麼只要確認頻率最高的空格條件就好, 因為其他字符所需要的空格都不會比頻率最高的元素來得多

# Time Complexity is O(N * lg(A)), N is the length of the string. A is the size of the alphabet
from collections import Counter
from heapq import heappush, heappop
class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        max_freq = Counter(S).most_common(1)[0][1] #why [0][1], 因為[('k', 2)] 包覆在list裡
        if 2*max_freq -1 > len(S):
            return ""
        
        heap = []
        for k,v in Counter(S).items():  #keys: values
            heappush(heap, (v*-1, k))  #min heap
        result = []
        while heap:
            v,k = heappop(heap)
            if not result or k != result[-1]: # can add the top most element
                result.append(k)
                if v != -1: 
                    heappush(heap,(v+1,k))  #v+1 add back to heap
            else:                             # cannot add the top most element
                v1,k1 = heappop(heap)  #pop 頻率次高的
                result.append(k1)
                heappush(heap, (v,k))  #先把沒用到頻率最高的加回去
                if v1 != -1:
                    heappush(heap, (v1+1,k1))  #再把有用到頻率次高的, 把頻率-1 加回去
        return "".join(result)



# import collections
# a = "rsukkhgl"
# b = collections.Counter(a)
# b
# Counter({'r': 1, 's': 1, 'u': 1, 'k': 2, 'h': 1, 'g': 1, 'l': 1})
# c = collections.Counter(a).most_common(1)
# c
# [('k', 2)]



# aaaabbbcc=> ababacabc

# aaaabbbbcccc=>abcabcabcabc

利用join(a) return 是一個字串, 就算a是list or str

a = ["a","b","c"]
"".join(a)  
'abc'

a = "1234"
" ".join(a)
'1 2 3 4'


#自己重寫
#heap 思路 優先把頻率高的element 加到result,若元素==result[-1] 則加入頻率次高的, 整題最重要觀念 max_freq+(max_freq-1)<=len(S). 
#交互加入保證相鄰不一樣, Alternate placing the most common letters. 所以用到heap
#為什麼只要確認頻率最高的空格條件就好, 因為其他字符所需要的空格都不會比頻率最高的元素來得多
from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, S: str) -> str:
        most_fq = max(Counter(S).values())
        if most_fq * 2 - 1 > len(S):
            return ""
       
        heap = []
        
        for i, v in Counter(S).items():
            heapq.heappush(heap, (-v, i))
        
        res = []
        
        while heap:
            count, letter = heapq.heappop(heap)
            if not res or res[-1] != letter:
                res.append(letter)
                if count < -1:
                    heapq.heappush(heap, (count + 1, letter))
            else:
                count_2, letter_2 = heapq.heappop(heap)
                res.append(letter_2)
                if count_2 < -1:
                    heapq.heappush(heap, (count_2 + 1, letter_2))
                heapq.heappush(heap, (count, letter))
                
        return "".join(res)






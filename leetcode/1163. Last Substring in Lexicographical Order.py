'''
Given a string s, return the last substring of s in lexicographical order.

 

Example 1:

Input: "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".
Example 2:

Input: "leetcode"
Output: "tcode"
 

Note:

1 <= s.length <= 4 * 10^5
s contains only lowercase English letters.

'''



https://leetcode.com/problems/last-substring-in-lexicographical-order/discuss/363662/Short-python-code-O(n)-time-and-O(1)-space-with-proof-and-visualization

# 另一種解法: 

# Think of two sequences matching k characters so far and only differ at s[i+k] > s[j+k]
# i ... i+k
# j ... j+k

# Regardless of j relative position to i, we could set j to j+k+1. 
# This is because for any j2 (j<j2<j+k); and i2 (i<i2<j+k), i+k-i2 = j+k-j2, substring [j2, j+k] is still smaller than [i2, i+k] 
# (these two still only differ at s[i+k] > s[j+k]).

# Reversely and similarly, if s[i+k] < s[j+k], then set i to i+k+1

# at last to break tie, when i==j, set j=j+1;

# this gives the while loop as

#刷題用這個 
#思路: two pointers, i,j 指針一開始相差1, 額外設k 代表比較相同的長度
#不斷摸索找開頭大的, 一旦找到則比誰的suffix首 比較大, i這端 suffix不會遇到比開頭大的, 因為j會先遇到, 之後就會變i的開頭
class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j, k = 0, 1, 0
        n = len(s)
        while j + k < n:
            if s[i+k] == s[j+k]:
                k += 1
                continue  #while loop 進行下一輪
            elif s[i+k] > s[j+k]:
                j = j+k+1 #跳下一個看是否字母有可能比i開頭大
            else:
                i = i+k+1
            if i==j:
                j = j+1
            k = 0  #進行下一輪前歸0
        return s[i:]






i = 1
while i < 10 :
    if i >100:
        print("if 1st")
    elif i > 200:
        print("elif")
    else:
        print("else")
    if i > 0:   #前面 if elif else 其中一條件滿足 依然要判斷這個if
        print("i =",i,"if 2nd")
        i += 1
    print("ready!")

else
i = 1 if 2nd
ready!
else
i = 2 if 2nd
ready!
else
i = 3 if 2nd
ready!
else
i = 4 if 2nd
ready!
else
i = 5 if 2nd
ready!
else
i = 6 if 2nd
ready!
else
i = 7 if 2nd
ready!
else
i = 8 if 2nd
ready!
else
i = 9 if 2nd
ready!


注意此題是substring not sunsequence
'''
https://leetcode.com/problems/last-substring-in-lexicographical-order/discuss/361121/Python-O(n)-with-explanation

# Python O(n) with explanation

# First, the answer must be starting with the largest letter, ending at the end of string S. So we save all the "candidates" by their starting point, 
# and assign a pointer to each of them (pointing at the start).
# Then we increment the pointer for each candidate, using following rules:

# We filter the candidates by the letter their pointers are at. Only the ones with the largest letter will go into next round.
# If a pointer meets a starting point, it "swallows" the next candidate like a snake.
# In the following image, pointer of A meets the starting point of B. Suppose we want to keep candidate B. 
# The only possibility is the future letters are lexicographically larger than candidate B, so appending it to B makes B larger than A. 
# Apprently it can not be, otherwise B (and A) will not be selected initially as candidates. a append b start 依舊是最大的, candidates 開頭都是最大的
# image

# Finally we will have only one candidate.
# This gives O(n) time complexity. Not very strictly, assume we start with k candidates, then eliminating all except one candidate takes n/k steps. 
# In each step, we only increment the pointer of each candidate by one.
# Correct me if I made a mistake. :)
'''

#O(n) time complexity, 想法特殊  n/k steps
class Solution:
    def lastSubstring(self, s: str) -> str:
        count=collections.defaultdict(list)
        for i in range(len(s)):
            count[s[i]].append(i)
        largeC=max(count.keys())
        starts={}
        for pos in count[largeC]:
            starts[pos]=pos+1  #一開始pointer 就指向下一個letter
        # Initialize all candidates and their pointers
        
        while len(starts)>1:
        # Eliminate till we have only one
            toDel=set()
            nextC=collections.defaultdict(list)
            for start, end in starts.items():
                if end==len(s):
                # Remove if reaching the end
                    toDel.add(start)
                    continue
                    
                nextC[s[end]].append(start)
                # Filter by current letter
                
                if end in starts:
                    toDel.add(end)
                # "Swallow" the latter candidate
            
            nextStarts={}
            largeC=max(nextC.keys())
            for start in nextC[largeC]:
                if start not in toDel:
                    nextStarts[start]=starts[start]+1
                    # Select what we keep for the next step
            starts=nextStarts  #下一輪新的 starts dict
        for start,end in starts.items():
            return s[start:]




# a = {'a':100,'b':25,'z':26}
# largeC=max(a.keys())
# largeC
# 'z'

# largeC=max(a.values())
# largeC
# 100

# b = a.copy()
# b
# {'a': 100, 'b': 25, 'z': 26}

# "z" > "a"
# True

 










   







































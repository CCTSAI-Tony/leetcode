'''
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
'''

# backtracking and caching 
# Takes about 32ms:

#  O(len(p)*len(s))
#  思路: memorize, 此題重點 '*' can eliminate the charter before it
#  memorize + backtracking 像修枝, 剪掉不需要的葉子
class Solution:
    cache = {}  #重要!! cache 放這裡的原因是要變成class variable, ex: a = Solution(), a.isMatch(s, p), Solution().cache 就會累積cache 之後解其他parameter 就會很快
    def isMatch(self, s, p):
        if (s, p) in self.cache:
            return self.cache[(s, p)]
        if not p:
            return not s  #base case!! 若s 不是none, 則return False, 若 p, s都是None return True
        if p[-1] == '*':  
            if self.isMatch(s, p[:-2]):  #Since each '*' can eliminate the charter before it, 切分小問題
                self.cache[(s, p)] = True  #紀錄
                return True
            if s and (s[-1] == p[-2] or p[-2] == '.') and self.isMatch(s[:-1], p):  #self.isMatch(s[:-1], p) 往前一格, 注意開頭要加 if s
                self.cache[(s, p)] = True
                return True
        if s and (p[-1] == s[-1] or p[-1] == '.') and self.isMatch(s[:-1], p[:-1]):
            self.cache[(s, p)] = True
            return True
        self.cache[(s, p)] = False
        return False

# a = "12345"
# a[:-1]
# '1234'

# s = "mississippi"
# p = "mis*is*p*."

#  自己重寫!! cache放裡面也行效率差一點, 刷題用這個
#  O(len(p)*len(s))
#  原出處說此方法為 backtracking and caching 很有趣
#  This programming methodology, in simple terms, is Dynamic Programming, an optimization over backtracking.
#  若這邊改成 if self.isMatch(s,p[:-2]) or self.isMatch(s,p[:-1]) => 慢十倍, 因為self.isMatch(s,p[:-1]) 創造太多不需創造的子問題, 大大增加loading
#  手動寫例子就能清楚, elif s and (s[-1] == p[-2] or p[-2] == ".") and self.isMatch(s[:-1],p) 會與self.isMatch(s,p[:-1] 重複創造許多相同子問題
#  但 self.isMatch(s,p[:-1])會創造更多不需要的子問題, 都是False的, 造成recusion stack過多導致效率下降
#  top-down 要盡量避免計算用不到的subproblems
#  思路: 此題就是 back tracking! 遇到不對的candidate, abandon it and return back to top to search other candidate
#  遇到 * 兩個 possible candidates, 包括*前一個字母一併消失, or 當*前一個字母等於s最後一個字母, 保留*, s往左一格
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        if (s,p) in cache:
            return cache[(s,p)]
        if not p:
            return not s
        if p[-1] == "*":
            if self.isMatch(s,p[:-2]): 
                cache[(s,p)] = True
                return True
            
            elif s and (s[-1] == p[-2] or p[-2] == ".") and self.isMatch(s[:-1],p):
                cache[(s,p)] = True
                return True
            
        else:
            if s and (s[-1] == p[-1] or p[-1] == ".") and self.isMatch(s[:-1],p[:-1]):
                cache[(s,p)] = True
                return True
        cache[(s,p)] = False
        return False



# DP version: 48ms
#刷題用這個 此題重點 '*' can eliminate the charter before it, dp[i][j] 定義為p[:i] s[:j]
# The DP table and the string s and p use the same indexes i and j, but
        # table[i][j] means the match status between p[:i] and s[:j], i.e.
        # table[0][0] means the match status of two empty strings, and
        # table[1][1] means the match status of p[0] and s[0]. Therefore, when
        # refering to the i-th and the j-th characters of p and s for updating
        # table[i][j], we use p[i - 1] and s[j - 1].

#  O(len(p)*len(s)), 
#  思路: 此題重點 '*' can eliminate the charter before it, dp[i][j] 定義為p[:i] s[:j]
#  這題主要判斷sufix 的各種情況, 此題有點難需要多練習
class Solution:
    def isMatch(self, s, p):
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]  #dp[p][s], => dp[i][j] 定義為p[:i] s[:j]
        dp[0][0] = True  # Update the corner case of matching two empty strings.
        for i in range(1, len(p)):
            dp[i + 1][0] = dp[i - 1][0] and p[i] == '*'  #dp[i+1][0] = True and True => True, dp[i+1][0] = True and False => False, etc
                                             #Since each '*' can eliminate the charter before it, dp[i - 1][0]=> p[:i-1] s[:0], skip p[i-1]
                                             #ex: p==[a*b*c*d*e*], s==[] => return True, 因為s是[], 因此p 都要跳掉*前面的字母, 不然怎麼比對都是False
        for i in range(len(p)):  #row
            for j in range(len(s)):  #column
                if p[i] == '*':  #Either refer to the one before previous or the previous. 注意!! "*" 前一定有元素 所以 if p[i] == '*': 的 i 不會是0, dp[i - 1] 就不用擔心
                    dp[i + 1][j + 1] = dp[i - 1][j + 1] or dp[i][j + 1]  # I.e. * eliminate the previous or count the previous., dp[i][j + 1] count 前一字符 一個
                    if p[i - 1] == s[j] or p[i - 1] == '.':  #If p's previous one is equal to the current s, with helps of *, the status can be propagated from the left.
                                                             #ex: p==[abc*] or [ab.*], s== [abc] or [abcc...] or [bbc]
                        dp[i + 1][j + 1] |= dp[i + 1][j]  # 注意這裡要用 |=, dp[i + 1][j + 1] 可能本身就是True, ex: p=="ab*a*", s=="a"
                                                          # why dp[i + 1][j], 因為 p[i]== * and p[i-1] == s[j]  所以p的 suffix 一定可以等於 s[j], 剩下看p[:i+1]s[:j] 是否match,  
                                                          # 在比對p[:i+1]s[:j] 時注意 pattern * 前面字母可以消失, suffix 依舊可以滿足s[j], 要滿足時出現即可
                else:
                    dp[i + 1][j + 1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')
        return dp[-1][-1]


var |= value is short for var = var | value

True and False
False

False or True
True

r    s    r|=s
--------------
T    T    T
T    F    T
F    T    T
F    F    F



class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]  #dp[p][s]
        dp[0][0] = True  # Update the corner case of matching two empty strings.
        for i in range(1, len(p)):
            dp[i + 1][0] = dp[i - 1][0] and p[i] == '*'  
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == '*':  
                    dp[i + 1][j + 1] = dp[i - 1][j + 1] or dp[i][j + 1] 
                    if p[i - 1] == s[j] or p[i - 1] == '.':  
                        print("dp[i + 1][j + 1]",dp[i + 1][j + 1],"dp[i + 1][j]",dp[i + 1][j])
                        print("p[:i+1]",p[:i+1],"s[:j+1]",s[:j+1] )
                        dp[i + 1][j + 1] |= dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')
        return dp[-1][-1]


#舉例說明 dp[i + 1][j + 1] |= dp[i + 1][j], dp[i + 1][j + 1] 本身有可能是True 的

a = Solution()
a.isMatch("aaa","ab*a*c*a")


dp[i + 1][j + 1] True dp[i + 1][j] False
p[:i+1] ab*a* s[:j+1] a
dp[i + 1][j + 1] True dp[i + 1][j] True
p[:i+1] ab*a* s[:j+1] aa
dp[i + 1][j + 1] False dp[i + 1][j] True
p[:i+1] ab*a* s[:j+1] aaa
Out[102]:
True


























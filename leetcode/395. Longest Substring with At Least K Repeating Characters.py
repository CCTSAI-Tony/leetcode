'''
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''


Now, we will use sliding window approach to find the window of biggest length. However, it is not that easy. Imagine, that we have s = aabbb... and k = 3, 
what should we do when we reached window aabbb: should we expand it to the right hoping that we will meet another a? Or should we start to move left side of our window? 
One way to handle this problem is to do several sliding windows passes, 
where we fix T number of different symbols we must have in our substring. So, we check all posible T = 1, ... 26 (if fact, not 26, 
    but len(Counter(s)) + 1)) and do sliding window pass:

Initialize beg = 0, end = 0, Found = 0: number of elements with frequency more or equal than k, freq is array of frequencies = [0]*26 and MoreEqK = 0, 
which count number of non-zero frequencies in our freq array.
Now, we check if MoreEqK <= T or not, that is we have T or less different symbols in our window: then we can add element to right part of our sliding window: 
we increase its frequency, if this symbol is new, that is frequency become equal to 1, we increment MoreEqK. Also, if frequency become equal to k, we increment Found.
In opposite case it means, that we already have T+1 or more different symbols in or window, so we need to move left side of our sliding window. 
Again, we check if frequency was equal to k and if it was, we decrease Found by one, if frequency become equal to zero, we decrease MoreEqK.
Finally, if we have exactly T non-zero frequencies and all T of them more or equal than k, we update our result.
Complexity: time complexity is O(26n), because we can potentially have 26 passes over our data. Space complexity is O(26). Yes, I understand, that O(26n) = O(n), 
but here I want to stress that constant is quite big.


#刷題用這個, 最佳解, time complexity O(n), space complexity O(1)
#思路: 從1個滿足k的字母到len(set(s))個滿足k的字母, 來pass 整個字串 => 問題變成最多26次的 m個symble 都滿足k的字串的最大長度
from collections import Counter
class Solution:
    def longestSubstring(self, s, k):
        result = 0
        for T in range(1, len(Counter(s))+1): #numbers of different characters in s
            beg, end, Found, freq, MoreEqK = 0, 0, 0, [0]*26, 0
            while end < len(s):
                if MoreEqK <= T:
                    s_new = ord(s[end]) - 97
                    freq[s_new] += 1
                    if freq[s_new] == 1:
                        MoreEqK += 1
                    if freq[s_new] == k:
                        Found += 1
                    end += 1
                else:
                    symb = ord(s[beg]) - 97
                    beg += 1
                    if freq[symb] == k:
                        Found -= 1
                    freq[symb] -= 1
                    if freq[symb] == 0:
                        MoreEqK -= 1
                            
                if MoreEqK == T and Found == T:
                    result = max(result, end - beg)
                    
        return result



#重寫第二次, time complexity O(n), space complexity O(1)
from collections import defaultdict
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_len = 0
        for t in range(1, len(set(s)) + 1):
            l, r, numK, freq, non_zero_f = 0, 0, 0, defaultdict(int), 0
            while r < len(s):
                if non_zero_f <= t:
                    nxt = s[r]
                    if nxt not in freq:
                        non_zero_f += 1
                    freq[nxt] += 1
                    if freq[nxt] == k:
                        numK += 1
                    r += 1
                else:
                    if freq[s[l]] == k:
                        numK -= 1
                    freq[s[l]] -= 1
                    if not freq[s[l]]:
                        non_zero_f -= 1
                        del freq[s[l]]
                    l += 1
                if numK == non_zero_f == t:
                    max_len = max(max_len, r - l)
        return max_len


# recursive 28ms Time: O(n^3) 這個超屌的
class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(z, k) for z in s.split(c))  # 好招
        return len(s)


# a = "argfugidogagfdlijwefoiapoto"
# a.split("a")

# ['', 'rgfugidog', 'gfdlijwefoi', 'poto']

# 刷題用這個, time complxity O(n^3)
# iterative
# 思路: 利用set 來找出distinct elements, 利用count 來確認有幾個相同元素, 若沒有達標, 用split 排除這元素, 剩下的子串們沒分別確認
class Solution:
    def longestSubstring(self, s, k):
        stack = []
        stack.append(s)
        ans = 0
        while stack:
            s = stack.pop()
            for c in set(s):
                if s.count(c) < k:
                    stack.extend([z for z in s.split(c)])  # 切分字串 這裡用到extend, 可以搭配list comprehension
                    break  # break for-else loop
            else:  # for 與 else 的搭配 滿少見的, else 不可省略
                ans = max(ans, len(s))
        return ans



# What is the use of “else” after “for” loop in Python?

# https://stackoverflow.com/questions/23625189/what-is-the-use-of-else-after-for-loop-in-python

# else executes after for providing for wasn't terminated with break:

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break  # out of the for-else loop,
            # if we take out of else,
            # after break, it will execute print n, 'is a prime number'
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# The for ... else statement is used to implement search loops.

# In particular, it handles the case where a search loop fails to find anything.

# In summary, the else clause will execute whenever the for loop terminates naturally.
# If a break or an exception occurs in the for loop the else statement will not execute.


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break  # out of for loop
    print n, 'is a prime number'  # break 後依舊執行


'''
Use a dict to record the letter count.
The target substring cannot contain letters with less than K repeating.
So we can use these letters as boundary and divide the source string into substrings and then check recursively on substrings.
Time: O(n)
Space: O(n)

Why time O(n)?
That's a very good question. Per descripition "(consists of lowercase letters only)". Any thought?
--If we break the string at 'a' then the substrings on the next recursion MUST NOT contain 'a', no matter how many segments you have.
--There are 26 letters in total to let you break the string. So the deepest recusion level is 26. Each level is O(N). O(26N) is also O(N).
--In fact, you can never reach 26th level, because recursion returns, if len(s) < k return 0 and if k < 2 return len(s)
'''

# 這個太複雜了 28ms


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s or len(s) < k:
            return 0
        if k < 2:  # 這個省略也ok
            return len(s)

        my_dict = {}
        for c in s:
            my_dict[c] = my_dict.get(c, 0) + 1

        left = 0
        partition = []
        for right in range(len(s)):
            if my_dict[s[right]] < k:  # s[right] must not apprear in the next recursion
                partition.append(s[left:right])
                left = right + 1
        partition.append(s[left:])  # don't forget the last segment

        if len(partition) == 1:  # substring
            return len(s)

        res = 0
        for subs in partition:
            res = max(res, self.longestSubstring(subs, k))

        return res

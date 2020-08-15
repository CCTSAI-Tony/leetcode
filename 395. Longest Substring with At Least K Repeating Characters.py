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

# recursive 28ms Time: O(n) 這個超屌的


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


# iterative
class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        stack = []
        stack.append(s)
        ans = 0
        while stack:
            s = stack.pop()
            for c in set(s):
                if s.count(c) < k:
                    stack.extend([z for z in s.split(c)])  # 這裡用到extend, 可以搭配list comprehension
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

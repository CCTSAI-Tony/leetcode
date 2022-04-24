'''
You are given a string s consisting only of characters 'a' and 'b'.

You can delete any number of characters in s to make s balanced. 
s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

 

Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.
 

Constraints:

1 <= s.length <= 105
s[i] is 'a' or 'b'.
'''

'''
Traversing the string from backwards, if a appears first, it could be a misplaced character, 
but we don't know yet. So we keep a count. If b appears first, and no a has appeared, it is always valid, so we can simply ignore it.
Now what if a has appeared, and b appears? We need to remove either an a or a b. 
It's kind of like a cancelation with each other. And we can decrement the count, meaning one pair of misplacement is gone. 
we did a deletion, which is either a or b. We don't care whether the actual deletion is a or b, we only care about the number.
After traversing the entire string, it's guaranteed that the cancelation (deletion) is minimum.

'''


# 刷題用這個, time complexity O(n), space complexity O(1)
# 思路: greedy, 逆序遍歷, 若出現b 但a 之前出現過, mismatch_count -= 1, delete += 1
# ex: bbaaaaa, 這裏mismatch_count -= 1 並不代表delete a 而是delete b, 只是代表mismatch的情況-1
# ex:bbbbbaa, 這裏mismatch_count -= 1 就是delete a
# ex: bbaa, 這裏mismatch_count -= 1 可以是delete a 也可以是delete b
class Solution:
    def minimumDeletions(self, s: str) -> int:
        mis_match = 0
        res = 0
        for i in range(len(s)-1, -1, -1): #重點 逆序遍歷
            if s[i] == "a":
                mis_match += 1
            if s[i] == "b":
                if mis_match > 0:
                    mis_match -= 1
                    res += 1
        return res


# 這個更好懂, 有點dp
class Solution:
    def minimumDeletions(self, s: str) -> int:
        # track the minimum number of deletions to make the current string balanced ending with 'a', 'b'
        end_a, end_b = 0,0 
        for val in s:
            if val == 'a':
                # to end with 'a', nothing to do with previous ending with 'a'
                # to end with 'b', need to delete the current 'a' from previous ending with 'b'
                end_b += 1
            else:
                # to end with 'a', need to delete the current 'b' from previous ending with 'a'
                # to end with 'b', nothing to do, so just pick smaller of end_a, end_b
                end_a, end_b = end_a+1, min(end_a, end_b)
        return min(end_a, end_b)



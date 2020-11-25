'''
Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing zero or more conversions.

In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

Return true if and only if you can transform str1 into str2.

 

Example 1:

Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.
Example 2:

Input: str1 = "leetcode", str2 = "codeleet"
Output: false
Explanation: There is no way to transform str1 to str2.
 

Note:

1 <= str1.length == str2.length <= 10^4
Both str1 and str2 contain only lowercase English letters.
'''

Map each character in str1 to what it needs to be in str2. 
If any of these mappings collide (e.g. str1 = "aa", str2 = "bc", "a" needs to become both "b" and "c") we immediately return False since the transformation is impossible.

Next, we check the number of unique characters in str2. If all 26 characters are represented, 
there are no characters available to use for temporary conversions, and the transformation is impossible. 
The only exception to this is if str1 is equal to str2, so we handle this case at the start of the function.

#刷題用這個, time complexity O(n), space complexity O(n)
#思路: 針對source to end 字串建立每個字轉換的有向邊, 同一個字母只能轉化成另一個字母, 若出現需要轉化成>1個字母的狀況 => 無法transform, target字串不能26個字母同時存在 => 形成環沒有多餘字母充當中間值
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        m = {}
        for i in range(len(str1)):
            if str1[i] not in m:
                m[str1[i]] = str2[i]
            elif m[str1[i]] != str2[i]:
                return False
        return len(set(str2)) < 26


#重寫第二次, time complexity O(n)
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        m = {}
        for s, e in zip(str1, str2):
            if s not in m:
                m[s] = e
            elif m[s] != e:
                return False
        return len(set(str2)) < 26



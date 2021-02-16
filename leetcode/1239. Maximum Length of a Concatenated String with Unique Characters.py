'''
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
'''



# Explanation
# Initial the result res to include the case of empty string "".
# res include all possible combinations we find during we iterate the input.

# Itearte the the input strings,
# but skip the word that have duplicate characters.
# The examples is kind of misleading,
# but the input string can have duplicate characters,
# no need to considerate these strings.

# For each string,
# we check if it's conflict with the combination that we found.
# If they have intersection of characters, we skip it.
# If not, we append this new combination to result.

# return the maximum length from all combinations.

#刷題用這個, time complexity O(16*16*16*26) => O(1), space complexity O(16^2) => O(1)
#思路: 使用到set 的運算技巧, & 交集, | 聯集, 一開始就skip 出現重複字元的單字, 利用聯集把合適的組合字串加進dp裡, 以利下一次組合找到最長unique 字串
class Solution:
    def maxLength(self, A):
        dp = [set()] #初始為空set => 技巧! 方便之後
        for a in A:
            if len(set(a)) < len(a): 
                continue
            a = set(a)
            for c in dp:
                if a & c: #a 與 c 有重複元素, skip掉
                    continue
                dp.append(a | c) #a 與 c 的連集
        return max(len(a) for a in dp)



#重寫第二次, time complexity O(16*16*16*26) => O(1), space complexity O(16^2) => O(1)
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        unique = [set()] #注意要 set(), 而不是{""}, ""也算一個元素, 所以不是空set
        max_unique = 0
        for a in arr:
            a_set = set(a)
            if len(a) != len(a_set):
                continue
            for u in unique:  #  會有元素持續添加在unique, 照理來說 for loop會不斷iterate, 然而之前加進去的組合x因為本身含有a_set元素而被continue, 所以可以結束for loop
                if a_set & u:
                    continue
                x = a_set | u
                unique.append(x) 
                max_unique = max(max_unique, len(x))
        return max_unique


#刷題用這個, time complexity O(16*16*16*26) => O(1), space complexity O(16) => O(1)
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        uniqELements = ['']
        maximum = 0
        for i in range(len(arr)):
            sz = len(uniqELements)
            for j in range(sz):
                x=arr[i]+uniqELements[j]
                if (len(x)==len(set(x))):
                    uniqELements.append(x)
                    maximum = max(maximum,len(x))
        #print(uniqELements)
        return maximum






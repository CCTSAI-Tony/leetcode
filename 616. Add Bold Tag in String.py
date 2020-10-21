'''
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. 
If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. 
Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
Example 1:

Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
 

Example 2:

Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
 

Constraints:

The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].
Note: This question is the same as 758: https://leetcode.com/problems/bold-words-in-string/
'''

#time complexity O(nlogn), space complexity O(n)
#思路: 利用local 來存儲所有指定word的區間, 同一個 word 在原始字串可能會有重複, 且還會互相重疊 or 接壤, 使用find 來找出對應的區間起始點, 一但找到, 尋找字串的起始點往右移一格 尋找下一個對應區間
#使用左閉右開存儲區間, 再使用sort 對start index 排序, 之後遍歷這些區間, 題目變成重複區間要合併 x1.start <= x0.end => 合併 => 合併後的區間要被<b> and </b> wrap
#注意: 記得區間外的元素也要append至res, ex: 區間與區間之間的word or 開頭到第一區間的字串
#注意: 若原始字串沒有指定的字 or dict is empty 造成local empty => retrun 原始字串
class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        location = []
        for word in dict:
            start = s.find(word)
            while start != -1:
                location.append([start, start+len(word)]) #location append 區間 左閉右開
                start = s.find(word, start+1) #start + 1 => 找下一個word index
        if not location: #若原始字串沒有指定的字 => retrun 原始字串
            return s
        location.sort() #針對start 做排序
        st, e = location[0][0], location[0][1]
        res = s[0:st] #起始沒被wrap 的字串
        for x in range(1, len(location)):
            if location[x][0] <= e: #重疊 or 接壤
                e = max(e, location[x][1])
            else:
                res += "<b>" + s[st:e] + "</b>"
                res += s[e:location[x][0]] #中間沒被wrap 的字串
                st = location[x][0]
                e = location[x][1]
        res += "<b>" + s[st:e] + "</b>" + s[e:] #最後的收尾
        return res

# string.find(value, start, end)
# The find() method returns -1 if the value is not found.

#自己重寫, time complexity O(nlogn), space complexity O(N)
class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        local = []
        res = ""
        for word in dict:
            start = s.find(word) 
            while start != -1:
                local.append([start, start+len(word)])
                start = s.find(word, start + 1) 
        if not local: #若原始字串沒有指定的字 => retrun 原始字串
            return s
        local.sort()
        st, ed = local[0][0], local[0][1]
        res += s[:st]
        for x in range(1, len(local)):
            if local[x][0] <= ed:
                ed = max(ed, local[x][1])
            else:
                res += "<b>" + s[st:ed] + "</b>"
                res += s[ed:local[x][0]]
                st, ed = local[x][0], local[x][1]
        res += "<b>" + s[st:ed] + "</b>" + s[ed:]
        return res

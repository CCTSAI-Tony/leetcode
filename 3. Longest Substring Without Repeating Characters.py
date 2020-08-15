class Solution(object):
	def lengthOfLongestSubstring(self, s):
        # https://leetcode.com/articles/longest-substring-without-repeating-characters/
        charMap = {}
        for i in range(256): #Ascii 完整碼表256個(包含擴充字符)
            charMap[i] = -1  #取-1是因為第一個字是從0開始
        ls = len(s)
        i = max_len = 0 #i=0, max_len=0
        for j in range(ls):
            # Note that when charMap[ord(s[j])] >= i, it means that there are
            # duplicate character in current i,j. So we need to update i.
            if charMap[ord(s[j])] >= i:  #The ord() function returns an integer representing the Unicode character. aaaaa
                #abcdd charMap[4]=3 >=3 (i=3)
                i = charMap[ord(s[j])] + 1   #abcdd i=4   #abcd defghijk klmn  
            charMap[ord(s[j])] = j  #{0:0,1:1,2:2...}
            max_len = max(max_len, j - i + 1) #0-0+1=1, 1-0+1=2..  2
        return max_len
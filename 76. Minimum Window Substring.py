'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''

# The idea is we use a variable-length sliding window which is gradually applied across the string. 
# We use two pointers: start and end to mark the sliding window. 
# We start by fixing the start pointer and moving the end pointer to the right. 
# The way we determine the current window is a valid one is by checking if all the target letters have been found in the current window. 
# If we are in a valid sliding window, we first make note of the sliding window of the most minimum length we have seen so far. 
# Next we try to contract the sliding window by moving the start pointer. 
# If the sliding window continues to be valid, we note the new minimum sliding window. 
# If it becomes invalid, we break out of the inner loop and go back to moving the end pointer to the right.

# 刷題用這個 2 pointer and sliding window, 
# 思路 運用counter 來記錄target count 與 for loop and inner while loop 來表達sliding window(2 pointers)
# 不在counter(t) 的字, start指針遍歷 key value不會大於0, 因為初始值 = 0, 但在counter(t) 的字則有機會>0, 因為初始值>0
# time complexity O(n), n = len(s)*len(t), len(t) for while loop
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_letter_counts = collections.Counter(t)
        start = 0
        end = 0
        min_window = ""
        target_len = len(t)
        
        for end in range(len(s)): 
            if target_letter_counts[s[end]] > 0:
                target_len -= 1
             
            target_letter_counts[s[end]] -= 1
            
            while target_len == 0:
                window_len = end - start + 1
                if not min_window or window_len < len(min_window):
                    min_window = s[start:end+1]
                    
                target_letter_counts[s[start]] += 1
                
                if target_letter_counts[s[start]] > 0:
                    target_len += 1
                start += 1
        
        return min_window





class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target_letter_counts = collections.Counter(t)
        start = 0
        end = 0
        min_window = ""
        target_len = len(t)        
        
        for end in range(len(s)):  #end pointer 不斷moving forward
            # If we see a target letter, decrease the total target letter count
            if target_letter_counts[s[end]] > 0:
                target_len -= 1

            # Decrease the letter count for the current end letter
            # If the letter is not a target letter, the count just becomes -value, 原本就不是target letter, key value則會變負值
            #或者出現太多重複的target letter key value也會變負值
            target_letter_counts[s[end]] -= 1 #不存在的key 預設值為0
            
            # If all letters in the target are found: 開始緊縮by moving start pointer
             while target_len == 0:
                window_len = end - start + 1  #紀錄現在的 window_len
                if not min_window or window_len < len(min_window):
                    # Note the new minimum window
                    min_window = s[start : end + 1]
                    
                # Increase the letter count of the current start letter
                target_letter_counts[s[start]] += 1
                
                # If all target letters have been seen and now, a target letter is seen with count > 0
                # Increase the target length to be found. This will break out of the loop
                if target_letter_counts[s[start]] > 0:
                    target_len += 1
                    
                start+=1 #narrow the window
                
        return min_window


a = "dlfijf"
b = collections.Counter(a)
b
Counter({'d': 1, 'l': 1, 'f': 2, 'i': 1, 'j': 1})
b["g"] #不存在的key 預設值為0
0


Accepted Python solution using hashtable


Basically I kept a dictionary to record the index of each character of T. Each time I found a window, 
(when miss == []), I checked the length of this window by subtracting the maximum index and the minimum index of the characters. 
If this window is the smallest one so far, I record its beginning and ending index as "start" and "end."

class Solution:
    # @return a string
    def minWindow(self, s, t):
        indices = {}  #dict
        for char in t:
            indices[char] = []
        miss = list(t)
        start = 0
        end = len(s)
        for i in range(len(s)):
            if s[i] in t:  #這句重要 不然會出現key error
                if s[i] not in miss and indices[s[i]] != []:
                    indices[s[i]].pop(0)  #pop 最左邊的(最早加進去的)
                elif s[i] in miss:
                    miss.remove(s[i])  #拿掉一個字符
                indices[s[i]].append(i)  #目標字符key 加入index
            if miss == []:  #包含所有的target 字符
                maximum = max([x[-1] for x in indices.values()])  #從dict 找出最大的index
                minimum = min([x[0] for x in indices.values()])  #從dict 找出最小的index
                if maximum-minimum+1 < end-start+1:
                    start = minimum
                    end = maximum
        if miss != []:
            return ""
        else:
            return s[start:end+1]


Good thoughts. I give your a vote up. Your time complex seems to be len(s)*len(t), 

a = "dlfijf"
b = list(a)
b
['d', 'l', 'f', 'i', 'j', 'f']
b.remove("f")
b
['d', 'l', 'i', 'j', 'f']













'''
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

 
Follow up:
Could you solve it using only O(1) extra space?

 
Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
 

Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
 

Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
 

Note:

All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.
'''

# Python solution with detailed explanation 2 pointers, time complexity O(n)

# Algorithm

# Maintain a rptr and wptr to write in-place.
# Use 2 while loops - outer loop rptr < len(chars) and inner loops counts the streak of common characters.
# Always write the character, but only write the frequency when it is more than 1. Note that when f = 12, we need to write two characters: "1" and "2".

#最重要是回報壓縮後的長度, 並修改長度內的元素, 長度外的元素不重要, 因為回報長度後test只會檢查長度內的元素是否正確
#思路: 使用雙指針, rptr來遍歷與紀錄有多少相同common letter, wptr 則是寫入rptr指向的letter, 若f>1, wptr 則會一格一格往前持續寫入str(f)
#rptr指針若指向不同letter, 結束while loop, 由wptr 開始寫入紀錄的資訊, 之後再由rptr紀錄下一letter資訊...
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        rptr, wptr = 0, 0
        while rptr < len(chars):
            ch, f = chars[rptr], 0 #f: frequency
            while rptr < len(chars) and chars[rptr] == ch:
                rptr, f = rptr+1, f+1
            chars[wptr], wptr = ch, wptr + 1  #wptr + 1, move to 下一個 index 若f =1 
            if f > 1:
                for c in str(f):  #ex: f = 12, we need to write two characters: "1" and "2".
                    chars[wptr], wptr = c, wptr + 1
        return wptr  #最後要回報壓縮至多長 這邊return wptr 是因為0 base index 的關係, 前面wptr 已先加1了, 所以直接return


#參照上面, 自己重寫 112ms
class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        r, w = 0, 0
        while r < len(chars):
            ch, f = chars[r], 0
            while r < len(chars) and chars[r] == ch:
                f += 1
                r += 1
                
            chars[w] = ch
            w += 1
            if f > 1:
                for s in str(f):
                    chars[w] = s
                    w += 1
        return w

#重寫第二次, time complexity O(n), space compleixty O(1)
class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        count = 1
        prev = chars[0]
        for i in range(1, len(chars)):
            if chars[i] == prev:
                count += 1
            else:
                chars[l] = prev
                l += 1
                if count > 1:
                    for s in str(count):
                        chars[l] = s
                        l += 1
                count = 1
                prev = chars[i]
        chars[l] = prev
        l += 1
        if count > 1:
            for s in str(count):
                chars[l] = s
                l += 1
        return l

#重寫第三次, time complexity O(n), space complexity O(1)
class Solution:
    def compress(self, chars: List[str]) -> int:
        l, r = 0, 0
        while r < len(chars):
            ch = chars[r]
            cnt = 0
            while r < len(chars) and chars[r] == ch:
                cnt += 1
                r += 1
            chars[l] = ch
            l += 1
            if cnt > 1:
                for s in str(cnt):
                    chars[l] = s
                    l += 1
        return l

#自己寫的, time complexity O(n), space complexity O(1), 112ms
#思路: 利用for loop and slow 雙指針, 記得離開for loop 要手動處理最後一個common letter
class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        slow = 0
        times = 0
        ch = chars[0]
        for i in range(len(chars)):
            if chars[i] == ch:
                times += 1
            elif chars[i] != ch:
                chars[slow] = ch
                slow += 1
                if times > 1:
                    for s in str(times):
                        chars[slow] = s
                        slow += 1
                times = 1  #發現新的letter, 初始值為1
                ch = chars[i]
                
        chars[slow] = ch
        slow += 1
        if times > 1:
            for s in str(times):
                chars[slow] = s
                slow += 1
         
        return slow







































































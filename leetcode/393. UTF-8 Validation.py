'''
A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx @@ 題目有錯 0010 FFFF => 001F FFFF
Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

Note:
The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.

Example 1:

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
Example 2:

data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.

Return false.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
'''

# This is a simple implementation using a marker to count bytes.
# 思路: bit represantation 一個x 代表 2^1, 1 byte 7個x, 2^7 = 128 => 0000 0000-0000 007F => 0 - 127 總共有128個字
# 此題最主要是確認8 bits 是否符合編碼規則, 利用count 來紀錄後續的bytes 是否符合規則, 最多4個1
class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count = 0
        for byte in data:
            if byte >= 128 and byte <= 191: #10xxxxxx binary string
                if not count:
                    return False
                count -= 1
            else:
                if count:  #前面的utf-8沒完全表示 例如3bytes -> 接續沒有兩個10開頭的bytes
                    return False
                if byte < 128:  #<128 可以當作一個獨立byte
                    continue
                elif byte < 224:  #"11100000"  這裡的count 是指接續有幾個開頭 10的byte
                    count = 1
                elif byte < 240:  #"11110000"
                    count = 2
                elif byte < 248:  #"11111000"
                    count = 3
                else:           #大於編碼範圍 1-4 bytes
                    return False
                    
        return count == 0  #最後再次確認count 有無歸0

#128 10000000
#191 10111111

# bin(191)
# '0b10111111'
# a = "10111111"
# int(a,2)
# 191



# 这道题不是一道算法的难题，但是，考的是阅读和UTF-8的知识点。

# 首先，我们来学习一下UTF-8. wiki：https://en.wikipedia.org/wiki/UTF-8
# 我在这里简单介绍一下，UTF-8只有四种编码：
# 0000 ~ 007F 这个范围的UTF-8编码:
# 0XXX XXXX

# 0080 ~ 07FF 这个范围的UTF-8编码 :
# 110X XXXX
# 10XX XXXX

# 0800 ~ FFFF 这个范围的UTF-8编码 :
# 1110 XXXX
# 10XX XXXX
# 10XX XXXX

# 1 0000 ~ 1F FFFF 这个范围的UTF-8编码 :
# 1111 0XXX
# 10XX XXXX
# 10XX XXXX
# 10XX XXXX

# UTF-8 不是顺序编码的，存在跳跃。所以被跳跃过去的码和大于这个范围的码就是无效代码。

# 如果我们获得了一个编码，1111 10XX。很明显的看出，不是我们这四种形式里面的某一种，因为这里面有5个1，我们上面的第四种形式中最多的 只有4个1，所以应该返回false。是大于UTF-8编码范围的码。
# 这里要稍微注意下，如果我们读取的数据的第一行是10XX XXXX，这也不是我们已知编码中的一种。我们提到的四种形式，分别是零个1，两个1，三个1和四个1。
# 这里只有一个1。10XX XXXX是被跳跃过去的码，不是UTF-8的编码范围，也应该返回false。（这里需要稍微理解一下。）

# 这里我们先来几个例子：
# 例1：{252，140，140，140，140，140，1 }
# 252(1111 1100)
# return false
# 原因是1111 1100 不在我们的四种形式里面。252里面有6个1，上面提到的4种形式里面最多有4个1. 此例子大于UTF-8的编码范围。
# 例2：{1，1，1，1，1}
# return true
# 原因是1是第一种形式，然后计算下一位，还是第一种形式。以此类推直到计算到最后一位，都是第一种形式。因此返回true；
# 例3：{240,162,138,147,17}
# return true；
# 原因是240（11110000）明显是第四种形式。后面的17是下一个UTF-8编码，且是有效码。

# 解释到这里大家是不是就明白很多了呢？


# bit manipulation, time complexity O(n), 刷題用這個
# 思路: bit represantation 一個x 代表 2^1, 1 byte 7個x, 2^7 = 128 => 0000 0000-0000 007F => 0 - 127 總共有128個字
# 此題最主要是確認8 bits 是否符合編碼規則, 利用count 來紀錄後續的bytes 是否符合規則, 最多4個1
class Solution(object):
    def validUtf8(self, data):
        i, N = 0, len(data)
        while i < N:
            if data[i] >> 3 == 0b11110:
                for j in range(i+1,i+4): #後面3個bytes 都要10開頭, 若後面沒bytes 一樣return False
                    if j >= N or data[j] >> 6 != 0b10:
                        return False
                i += 4
            elif data[i] >> 4 == 0b1110:
                for j in range(i+1,i+3):
                    if j >= N or data[j] >> 6 != 0b10:
                        return False
                i += 3
            elif data[i] >> 5 == 0b110:
                for j in range(i+1,i+2):
                    if j >= N or data[j] >> 6 != 0b10:
                        return False
                i += 2
            elif data[i] >> 7 == 0:
                i += 1
            else:  #不符編碼格式ex: 出現5個1
                return False
        
        return True


#自己重寫, 120ms
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        while i < len(data):
            if data[i] >> 3 == 0b11110:
                for j in range(i+1, i+4):
                    if j >= len(data) or data[j] >> 6 != 0b10:
                        return False
                i += 4
            elif data[i] >> 4 == 0b1110:
                for j in range(i+1, i+3):
                    if j >= len(data) or data[j] >> 6 != 0b10:
                        return False
                i += 3
            elif data[i] >> 5 == 0b110:
                for j in range(i+1, i+2):
                    if j >= len(data) or data[j] >> 6 != 0b10:
                        return False
                i += 2
            elif data[i] >> 7 == 0b0:
                i += 1
            else:
                return False
        return True























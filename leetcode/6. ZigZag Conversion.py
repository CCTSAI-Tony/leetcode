# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:

# P     I    N
# A   L S  I G
# Y A   H R
# P     I

time complexity O(n)
#思路: num = (numRows-1)*2, 建立一個pattern, 若 i % num >= numRows, 代表往上一行加入
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: 
            return s
        rows = [''] * numRows #初始行數
        num = (numRows-1)*2 # numRows-1, zero based index issue
        for i, item in enumerate(s):
            if i % num >= numRows:
                rows[(num - i % num)] += item
            else:
                rows[i % num] += item
        return ''.join(rows)

        '''Consume the numRows is 5,we see the zigzag pattern like this:
0        8
1     7  9
2   6   10
3 5     11
4       12...

we can see the numbers 0~7 is a small pattern in here,if we divide 8 we can get same number in other small patterns.like
0%8 = 0; 8%8 = 0
1%8 = 1; 9%8 = 1

build up seperate areas, and put specific items into them by order

'''


'''
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  
Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, 
and 8 rotate to themselves; 2 and 5 rotate to each other (on this case they are rotated in a different direction, 
in other words 2 or 5 gets mirrored); 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note:

N  will be in range [1, 10000].
'''

#參考別人, time complexity O(n), space complexity O(1)
#思路: 利用continue 來跳過invalid num
class Solution:
    def rotatedDigits(self, N: int) -> int:
        count = 0
        for i in range(1, N+1):
            num = str(i)
            if "3" in num or "4" in num or "7" in num:
                continue
            if "2" in num or "5" in num or "6" in num or "9" in num:
                count += 1
        return count


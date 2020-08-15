'''
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

'''

# Similar to other solutions out there.

# The code has O(1) time complexity, because all the possible watch combinations (valid or invalid) can't be more that 16 * 64.
# Regarding space complexity, it's also O(1) cause the DFS will have depth of maximum n, which can't be more than 9(0-9, 10個bits) as per problem boundary.


# In the dfs, idx is the number of dots considered so far, n is the number of dots to be allocated. 
# In the for loop, the first four dots (i = 0, 1, 2, 3) are for hours, the rest i = 4, .., 9are for minutes. 
# The binary operations, hours | 1 << i or minutes | 1 << k pushes the i or k dot in its right position in the binary representation. 
# Hope this helps.


#刷題用這個 time complexity O(1), all the possible watch combinations (valid or invalid) can't be more that 16 * 64.
#思路: dfs bcktracking
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        res = []
        self.dfs(num, 0, 0, 0, res)
        return res
    
    def dfs(self, n, hours, mins, idx, res):
            if hours >= 12 or mins > 59:  #hour <12, mins <60 超出邊界狀況return
                return
            if not n:
                res.append(str(hours) + ":" +"0" * (mins < 10) + str(mins))
                return
            for i in range(idx, 10):  #前面四個bits給hour, 後面給mins, 最多十個bits (0-9) zero-base index
                if i < 4:  #代表上面四個燈 
                    self.dfs(n-1, hours|(1<<i), mins, i+1, res)  #index, i+1 避免重複在同一個bit
                else:
                    k = i-4   #i: 4,5,6,7,8,9 => k: 0,1,2,3,4,5
                    self.dfs(n-1, hours, mins|(1<<k), i+1, res)

#(mins < 10) True or False
# mins = 11
# "0" * (mins < 10)
# ''

# mins = 1
# "0" * (mins < 10)
# '0'

# 0 | (1<<0) ==0
# 0 | (1<<2) ==4




# Generate all possible combinations of num indexes in the range from 0 to 10. For example, 
# one possible combination of 5 indexes is {0, 1, 4, 7, 8}, which is "3:25".

#好招
import itertools
class Solution(object):
    def readBinaryWatch(self, num):
        watch = [1,2,4,8,1,2,4,8,16,32]
        times = []
        for leds in itertools.combinations(range(len(watch)), num):
            h = sum(watch[i] for i in leds if i < 4) #index: 0,1,2,3
            m = sum(watch[i] for i in leds if i >= 4) #index: 4,5,6,7,8,9
            if h > 11 or m > 59: 
                continue
            times.append("{}:{:02d}".format(h, m))
        return times



# Function which returns subset or r length from n 
from itertools import combinations 
  
def rSubset(arr, r): 
  
    # return list of all subsets of length r 
    # to deal with duplicate subsets use  
    # set(list(combinations(arr, r))) 
    return list(combinations(arr, r)) 
  
# Driver Function 
if __name__ == "__main__": 
    arr = [1, 2, 3, 4] 
    r = 2
    print rSubset(arr, r) 
Output:

[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

# Input : arr[] = [1, 2, 3, 4],  
#             r = 2
# Output : [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]






class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        output = []
        for h in range(12):
          for m in range(60):
            if bin(h * 64 + m).count('1') == num:  #h * 64, 64 超過60 避免干擾<60的 bits
              output.append('%d:%02d' % (h, m))
        return output
'''
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
'''

https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/184434/JavaTrie99 建議看一下, 有圖好理解


# Python O(N) trie -- with explanation

# I found the other solutions in this discussion thread to be very confusing, so I'll do my best to explain the solution. 
# I'll skip the code implementing the trie because you can search the line. Here's what we want to do:

# Insert the binary representation of a number into the trie. Here, we insert from most significant bit to least significant bit, 
# meaning the first node in the trie is the MSB and so on.. MSB: most significant bit

# Everytime we insert a number (let's call this number A), 
#     we want to traverse the trie a second time and go the opposite way as A's binary representation as much as possible. 
#     It's important that our trie elements were entered from MSB to LSB because this will maximize the differences as we traverse down the tree.

# Find the node that diverges most with A and then return the XOR of these two numbers so we can update the max XOR.

# why time complexity is O(n), cause trie is at most 32 levels. search the trie just cost O(1)

#思路: 轉化數字成binary 存入trie, 之後遍歷與該數字最大限度相反的路徑, 這樣xor 得到的值才會最大

import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isEnd = False
        self.value = 0

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, val):
        curr = self.root
        for bit in word:
            curr = curr.children[bit]
        curr.isEnd = True
        curr.value = val
    
    def search(self, word, target):
        curr = self.root
        for bit in word:   
            if bit == '1' and curr.children.get('0'):  #最大限度往另一條路走
                curr = curr.children['0']
            elif bit == '0' and curr.children.get('1'):
                curr = curr.children['1']
            else:
                curr = curr.children[bit] 
                
        return target^curr.value  # XOR of these two numbers
            
                

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.trie = Trie()
        max_xor = -2**(32)
        
        for i in nums:
            binary_string = bin(i)[2:].zfill(31)  #總共31位數, signed integer 最大正數 2 ** 31
            self.trie.insert(binary_string, i)
            max_xor = max(max_xor, self.trie.search(binary_string, i))
        
        return max_xor


# why bin(i)[2:], 因為 bin(5) => '0b101'


# zfill() method returns a copy of the string with ‘0’ characters padded to the leftside of the given string.

# Syntax :

# str.zfill(length)

# number = "6041"
# print(number.zfill(8)) 

# 00006041






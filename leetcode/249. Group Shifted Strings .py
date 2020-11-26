'''
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of non-empty strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
'''

# We can solve this problem by mapping each string in strings to a key in a hashmap. We then return hashmap.values().

# {
#      (1, 1): ['abc', 'bcd', 'xyz'],  
#   (2, 2, 1): ['acef'],   
#       (25,): ['az', 'ba'],   
#          (): ['a', 'z']
# }
# The key can be represented as a tuple of the "differences" between adjacent characters. Characters map to integers (e.g. ord('a') = 97). 
# For example, 'abc' maps to (1,1) because ord('b') - ord('a') = 1 and ord('c') - ord('b') = 1
# We need to watch out for the "wraparound" case - for example, 'az' and 'ba' should map to the same "shift group" as a + 1 = b and z + 1 = a. 
# Given the above point, the respective tuples would be (25,) (122 - 97) and (-1,) (79 - 80) and az and ba would map to different groups. This is incorrect.
# To account for this case, we add 26 to the difference between letters (smallest difference possible is -25, za) and mod by 26. 
# So, (26 + 122 - 97) % 26 and (26 + 79 - 80) % 26 both equal (25,)

# Time complexity would be O(ab) where a is the total number of strings and b is the length of the longest string in strings.
# Space complexity would be O(n), as the most space we would use is the space required for strings and the keys of our hashmap.

#time complexity O(a*b) a: len(strings), b: length of the longest string in strings, space complexity: O(n), n: len(strings and the keys of our hashmap.)
#思路: 利用letter之間的差值來當作key, 相同的差值pattern 會被歸類為同一類, 因為總共有26個字母, 循環26個字母 使用差值 % 26 ex: az, ba 可以被歸類為同一種
#技巧: 使用% num 可以無縫接軌兩個num大小的區間 來做行跨區間的運算, ex: a(0) - z(25) - e'(30 % 26 = 4) => 4 - 25 = -21 => -21 + 26 = 5
#有時會利用% num 來避免num很大無法處理但又想計算超過num的跨區間運算
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strings:
            key = ()
            for i in range(len(s) - 1):
                circular_difference = 26 + ord(s[i+1]) - ord(s[i])
                key += (circular_difference % 26,)
            hashmap[key] = hashmap.get(key, []) + [s]
        return list(hashmap.values())


#自己重寫, 刷題用這個 time complexity O(a*b) a: len(strings), b: length of the longest string in strings, space complexity: O(n), n: len(strings and the keys of our hashmap.)
from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for string in strings:
            key = ()
            for i in range(1, len(string)):
                key += (((ord(string[i]) - ord(string[i-1])) % 26),)
            hashmap[key].append(string)
        return hashmap.values()








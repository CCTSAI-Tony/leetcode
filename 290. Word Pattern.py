'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
'''

#Use two dictionaries with index as values, 好招 看不懂請看解釋
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(" ") #['dog', 'cat', 'cat', 'dog'] 產生一個list
        if len(pattern) != len(words):
            return False

        # use two dictionaries, mapping character / string with index
        pattern_map, word_map = {}, {}
        for i in range(len(pattern)):
            if pattern_map.get(pattern[i], -1) != word_map.get(words[i], -1):
                return False
            pattern_map[pattern[i]] = word_map[words[i]] = i

        return True

# Can I know why you are using -1 in map.get()? Thank you! 為何不用0


# It gives a default value of -1 if the key isnt present in the dictionary.
# So in case of the test case "abba" and "dog cat cat fish"
# when there is an "a" at the 4th position it gives a 0 as our i starts from 0, whereas for fish we get a -1. This helps us break the loop and return False.

# Hope this help.s













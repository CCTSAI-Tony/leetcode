# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:
# All inputs will be in lowercase.
# The order of your output does not matter.



#刷題用這個, time complexity O(nk), space complexity O(nk), n: len(strs), k: maxlen of strs's element
#思路: 建立26字母數組tuple, 避免排序
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            letter = [0] * 26
            start = ord("a")
            for w in s:
                letter[ord(w) - start] += 1
            dic[tuple(letter)].append(s)
        return dic.values()

#重寫第二次, time complexity O(nk), space complexity O(nk)
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = defaultdict(list)
        for s in strs:
            letters = [0] * 26
            for w in s:
                letters[ord(w) - ord("a")] += 1
            memo[tuple(letters)].append(s)
        return memo.values()


#刷題用這個
#自己想的, time complexity O(n), n: total length of characters, 136ms
#思路: 利用frozenset 來使dict.items() set化 且 hashable, 避免排序
from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            temp = frozenset(Counter(word).items())
            groups[temp].append(word)
        return groups.values()


#重寫第二次, time complexity O(n), space complexity O(n)
from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            temp = Counter(s)
            key = frozenset(temp.items())
            dic[key].append(s)
        return dic.values()



#自己想的, time complexity O(nlogn), n: total length of characters, 200ms
#思路: 利用sort 使得anagrams 都能排序成一樣的字串, 變成tuple 當作key, 每個字若屬於同一個key, 就能加入該key
#sort 能對字母排序
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs:
            char = []
            for w in word:
                char.append(w)
            char.sort()
            group[tuple(char)].append(word)
        return group.values()



class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for w in strs:
            key = tuple(sorted(w)) #這邊要把sorted(w) tuple化 因為list 是unhashable type: 'list'
            d[key] = d.get(key, []) + [w] 
        return list(d.values()) #.values() 把各個鍵對應的值顯現出來 .keys() 把各個鍵顯現出來, 這裡list可以不加, d.values()本身就已經list化


        '''
        a = 'frank'
        print(sorted(a))
        print(a)

        ['a', 'f', 'k', 'n', 'r']
        frank


        Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
        Output:
        [
          ["ate","eat","tea"],
          ["nat","tan"],
          ["bat"]
        ]





        person = {'name': 'Phill', 'age': 22}

        print('Name: ', person.get('name'))
        print('Age: ', person.get('age'))

        # value is not provided
        print('Salary: ', person.get('salary'))

        # value is provided
        print('Salary: ', person.get('salary', 0.0))

        Name:  Phill
        Age:  22
        Salary:  None
        Salary:  0.0


        >>> numbers = [6, 9, 3, 1]
        >>> sorted(numbers)                  sorted() 可以用在tuple
        [1, 3, 6, 9]
        >>> numbers
        [6, 9, 3, 1]

        >>> values_to_sort = [5, 2, 6, 1]
        >>> # Try to call .sort() like sorted()
        >>> sort(values_to_sort)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        NameError: name 'sort' is not defined

        >>> # Try to use .sort() on a tuple   .sort()  不能用在tuple !!!!!!!!!!! 用在list
        >>> tuple_val = (5, 1, 3, 5)
        >>> tuple_val.sort()
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        AttributeError: 'tuple' object has no attribute 'sort'

        >>> # Sort the list and assign to new variable
        >>> sorted_values = values_to_sort.sort()
        >>> print(sorted_values)
        None

        >>> # Print original variable
        >>> print(values_to_sort)
        [1, 2, 5, 6]

        There are some pretty dramatic differences in how .sort() operates compared to sorted() in this code example:

        There is no ordered output of .sort(), so the assignment to a new variable only passes a None type.
        The values_to_sort list has been changed in place, and the original order is not maintained in any way.
        '''
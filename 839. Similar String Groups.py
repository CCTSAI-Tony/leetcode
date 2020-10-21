'''
Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  
Notice that "tars" and "arts" are in the same group even though they are not similar.  
Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list A of strings.  Every string in A is an anagram of every other string in A.  How many groups are there?

 

Example 1:

Input: A = ["tars","rats","arts","star"]
Output: 2
 

Constraints:

1 <= A.length <= 2000
1 <= A[i].length <= 1000
A.length * A[i].length <= 20000
All words in A consist of lowercase letters only.
All words in A have the same length and are anagrams of each other.
The judging time limit has been increased for this question.
'''


#刷題用這個 dfs, time complexity min(n*m^3, m*n^2), n = len(A), m = len(A[0]), space complexity O(n) 4600ms
#思路: dfs 尋找connected component, 但這題特別的是遍歷的維度, 因為要找similar 的words 有兩種方向
#第一個, 自己製造similar words, 看是否在A裡面 => 當字串長度 < len(A) ok, 但字串長度 >= len(A) => 導致製造字串cost太大
#第二個, 遍歷A 看裡面有沒有word與當前字串相差兩個不一樣的地方 => 找到相似word, 若len(A) 太大 => 導致遍歷A尋找similar words代價太高
#可知我們可以利用len(A) or len(A[0]) 的長度, 來切換哪一種方法來找similar words
#還有注意題目有說每個word都是anagram, 所以字串相差剛好兩個不一樣的地方 => 總元素不變所以是similar word
class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        words = set(A)
        visited = set()
        groups = 0
        for s in words:
            if s not in visited:
                groups += 1
                self.dfs(s, A, visited, words)
        return groups
    
    def dfs(self, s, A, visited, words):
        m, n = len(A[0]), len(A)
        if s in visited:
            return
        visited.add(s)
        s = list(s)
        if m < n: #遍歷m的cost 不會那麼大
            for i in range(len(s)):
                for j in range(i+1, len(s)):
                    s[i], s[j] = s[j], s[i]
                    neighbor = "".join(s) #O(n)
                    if neighbor in words:
                        self.dfs(neighbor, A, visited, words)
                    s[i], s[j] = s[j], s[i]
        else:
            for string in words:
                if string not in visited:
                    count = 0
                    for i in range(len(string)):
                        if s[i] != string[i]:
                            count += 1
                    if count == 2:
                        self.dfs(string, A, visited, words)


#自己想的, naive dfs, time complexity O(n*m3), n = len(A), m = len(A[0]) => TLE 
class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        A = set(A)
        visited = set()
        groups = 0
        for s in A:
            if s not in visited:
                groups += 1
                self.dfs(s, A, visited)
        return groups
    
    def dfs(self, s, A, visited):
        if s in visited:
            return
        visited.add(s)
        s = list(s)
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                s[i], s[j] = s[j], s[i]
                neighbor = "".join(s) #O(n)
                if neighbor in A:
                    self.dfs(neighbor, A, visited)
                s[i], s[j] = s[j], s[i]
        else:






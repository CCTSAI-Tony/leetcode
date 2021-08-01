# 5. Longest Palindromic Substring
# 用brutal force time complexity O(n^2), manacher 只要 O(n)

# time cokplexity O(n^2) 972ms
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_palindrome = ""
        for i in range(n):
            temp_odd = self.help(s, i, i)
            if len(temp_odd) > len(max_palindrome):
                max_palindrome = temp_odd
            temp_even = self.help(s, i, i+1)
            if len(temp_even) > len(max_palindrome):
                max_palindrome = temp_even
        return max_palindrome
    
    def help(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

# time complexity O(n), space complexity O(n)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_manacher = "#" + "#".join(s) + "#"
        n = len(s_manacher)
        lps = [0] * n
        r = 0
        c = 0
        for i in range(1, n):
            if r > i:
                lps[i] = min(r - i, lps[c-(i-c)])
            while i - lps[i] - 1 >= 0 and i + lps[i] + 1 < n and s_manacher[i - lps[i] - 1] == s_manacher[i + lps[i] + 1 ]:
                lps[i] += 1
            if i + lps[i] > r:
                c = i
                r = i + lps[i]
        max_lps, idx_p = max((v, i) for i, v in enumerate(lps))
        return s[(idx_p-max_lps)//2:(idx_p+max_lps)//2]


# 243. Shortest Word Distance
# time complexity O(n), space complexity O(n)
# 思路: greedy and hash table
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        index_map = {}
        min_distance = float("inf")
        for i, v in enumerate(wordsDict):
            if v == word1 and word2 in index_map:
                min_distance = min(min_distance, i - index_map[word2])
            elif v == word2 and word1 in index_map:
                min_distance = min(min_distance, i - index_map[word1])
            index_map[v] = i
        return min_distance


# 146. LRU Cache
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.memo = {}
        self.head = self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.memo:
            node = self.memo[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.memo:
            node = self.memo[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            if len(self.memo) >= self.capacity:
                last = self.tail.prev
                self.remove(last)
                del self.memo[last.key]
            node = Node(key, value)
            self.add(node)
            self.memo[node.key] = node
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        
    def add(self, node):
        head = self.head
        nxt = head.next
        head.next = node
        node.prev = head
        nxt.prev = node
        node.next = nxt


# 151. Reverse Words in a String
# time complexity O(n), space complexity O(1)
class Solution:
    def reverseWords(self, s: str) -> str:
        words = ""
        word = ""
        prev = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " " and prev == " ":
                if words != "":
                    words = words + " " + word
                else:
                    words += word
                word = s[i]
            elif s[i] != " " and prev != " ":
                word = s[i] + word
            prev = s[i]
        if not words:
            words += word
        else:
            words = words + " " + word
        return words


# 18. 4Sum
# 多重指針, time complexity (O(n^3)), 記得先對nums sort
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j > (i+1) and nums[j] == nums[j-1]:
                    continue
                l, r = j + 1, n - 1
                while l < r:
                    temp = nums[i] + nums[j] + nums[l] + nums[r]
                    if temp > target:
                        r -= 1
                    elif temp < target:
                        l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
        return res

#  63. Unique Paths II, time complexity O(mn)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
            else:
                break
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]



#  380. Insert Delete GetRandom O(1)
#  思路: remove 要交換index, 使得remove 的item 被放到最後位置, pop()
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.index = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.index:
            self.stack.append(val)
            self.index[val] = len(self.stack) - 1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.index:
            remove_idx = self.index[val]
            last_val = self.stack[-1]
            self.stack[remove_idx], self.stack[-1] = self.stack[-1], self.stack[remove_idx]
            self.index[last_val] = remove_idx
            del self.index[val]
            self.stack.pop()
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.stack)


# 772. Basic Calculator III
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = "+"
        for i, v in enumerate(s):
            if v.isdigit():
                num = num*10 + int(v)
            if v in ["+", "-", "*", "/", ")"]:
                self.update(num, op, stack)
                num = 0
                if v == ")":
                    while isinstance(stack[-1], int):
                        num += stack.pop()
                    op = stack.pop()
                    self.update(num, op, stack)
                    num = 0
                op = v
            if v == "(":
                stack.append(op)
                op = "+"
        
        self.update(num, op, stack)
        return sum(stack)
                
    
    def update(self, num, op, stack):
        if op == "+":
            stack.append(num)
        elif op == "-":
            stack.append(-num)
        elif op == "*":
            prev = stack.pop()
            stack.append(prev * num)
        elif op == "/":
            prev = stack.pop()
            stack.append(int(prev / num))


# 359. Logger Rate Limiter
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time_limit = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.time_limit:
            self.time_limit[message] = timestamp + 10
            return True
        else:
            limit = self.time_limit[message]
            if timestamp < limit:
                return False
            else:
                self.time_limit[message] = timestamp + 10
                return True


# 207. Course Schedule
from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = defaultdict(int)
        graph = defaultdict(list)
        queue = deque()
        for prerequisite in prerequisites:
            cur, pre = prerequisite
            graph[pre].append(cur)
            in_degree[cur] += 1
            
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
                del in_degree[course]
                
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                for nxt in graph[cur]:
                    in_degree[nxt] -= 1
                    if in_degree[nxt] == 0:
                        queue.append(nxt)
                        del in_degree[nxt]
        if in_degree:
            return False
        return True

# 210. Course Schedule II
from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = defaultdict(int)
        graph = defaultdict(list)
        queue = deque()
        res = []
        for prerequisite in prerequisites:
            cur, pre = prerequisite
            graph[pre].append(cur)
            in_degree[cur] += 1
            
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
                res.append(course)
                del in_degree[course]
                
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                for nxt in graph[cur]:
                    in_degree[nxt] -= 1
                    if in_degree[nxt] == 0:
                        queue.append(nxt)
                        res.append(nxt)
                        del in_degree[nxt]
        if in_degree:
            return []
        return res


# 384. Shuffle an Array
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        shuffle = self.nums[:]
        for i in range(len(self.nums)-1, 0, -1):
            j = random.randint(0, i)
            shuffle[i], shuffle[j] = shuffle[j], shuffle[i]
        return shuffle


# 1236. Web Crawler
from collections import deque
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        res = [startUrl]
        queue = deque([startUrl])
        visited = set([startUrl])
        while queue:
            for _ in range(len(queue)):
                url = queue.popleft()
                host = self.check_host(url)
                for next_url in htmlParser.getUrls(url):
                    next_host = self.check_host(next_url)
                    if host == next_host and next_url not in visited:
                        queue.append(next_url)
                        res.append(next_url)
                        visited.add(next_url)
        return res
        
        
    def check_host(self, url):
        url_split = url.split("/")
        return url_split[2]

# 300. Longest Increasing Subsequence
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sub = [nums[0]]
        for i in range(1,len(nums)):
            pos = self.bs(i, nums, sub)
            if pos == len(sub):
                sub.append(nums[i])
            else:
                sub[pos] = nums[i]
        return len(sub)
    
    def bs(self, i, nums, sub):
        left, right = 0, len(sub)-1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if sub[mid] >= nums[i]:
                right = mid
            else:
                left = mid
        if sub[left] >= nums[i]:
            return left
        elif sub[right] >= nums[i]:
            return right
        return right + 1

# 673. Number of Longest Increasing Subsequence
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1] * n
        count = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[i] == length[j]:
                        length[i] += 1
                        count[i] = count[j]
                    elif length[i] == length[j] + 1:
                        count[i] += count[j]
        max_len = max(length)
        return sum(count[i] for i in range(n) if length[i] == max_len)



# 149. Max Points on a Line
from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return 1
        lines = defaultdict(set)
        for i in range(len(points)):
            for j in range(1, len(points)):
                slope, intercept = self.check_slope(points[i], points[j])
                lines[(slope, intercept)].add(i)
                lines[(slope, intercept)].add(j)
        return max(len(lines[key]) for key in lines)
        
    def check_slope(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        if (x2 - x1) == 0:
            return float("inf"), x1
        slope = (y2 - y1) / (x2 - x1)
        intercept = y1 - slope * x1
        return slope, intercept



# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo = {}
        l = 0
        max_len = 0
        for r in range(len(s)):
            if s[r] not in memo:
                memo[s[r]] = r
                continue
            else:
                idx = memo[s[r]]
                max_len = max(max_len, r - l)
                while l <= idx:
                    del memo[s[l]]
                    l += 1
                memo[s[r]] = r
        max_len = max(max_len, len(s) - l)
        return max_len


# 733. Flood Fill
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited = set([(sr, sc)])
        origin = image[sr][sc]
        self.dfs(image, sr, sc, newColor, origin, visited)
        return image
    
    def dfs(self, image, sr, sc, newColor, origin, visited):
        image[sr][sc] = newColor
        m, n = len(image), len(image[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for d in directions:
            x, y = sr + d[0], sc + d[1]
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                color = image[x][y]
                if color == origin:
                    visited.add((x, y))
                    self.dfs(image, x, y, newColor, origin, visited)



# 205. Isomorphic Strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_pattern = self.pattern(s)
        t_pattern = self.pattern(t)
        return s_pattern == t_pattern
        
    def pattern(self, s):
        res = []
        memo = {}
        for i, v in enumerate(s):
            if v not in memo:
                memo[v] = i
                res.append(i)
            else:
                res.append(memo[v])
        return res


# 863. All Nodes Distance K in Binary Tree
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        parent_map = {}
        self.buildParentMap(root, None, parent_map)
        ans = []
        visited = []
        self.dfs(target, 0, parent_map, visited, ans, K)
        return ans
        
        
    def buildParentMap(self, node, parent, parent_map):
        if not node:
            return
        parent_map[node] = parent
        self.buildParentMap(node.left, node, parent_map)
        self.buildParentMap(node.right, node, parent_map)
    
    
    def dfs(self, node, distance, parent_map, visited, ans, K):
        if not node or node in visited:
            return
        visited.append(node)
        if distance == K:
            ans.append(node.val)
        else:
            self.dfs(node.left, distance + 1, parent_map, visited, ans, K)
            self.dfs(node.right, distance + 1, parent_map , visited, ans, K)
            self.dfs(parent_map[node], distance + 1, parent_map, visited, ans, K)

# 107. Binary Tree Level Order Traversal II
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue, res = deque([root]) , []
        while queue:
            cur_level = []
            for i in range(len(queue)): 
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            res.append(cur_level)
        return res[::-1]

# 128. Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        while nums:
            l1 = l2 = 0
            n = nums.pop()
            i = n + 1
            while i in nums:
                l1 += 1
                nums.remove(i)
                i += 1
            i = n - 1
            while i in nums:
                l2 += 1
                nums.remove(i)
                i -= 1
            max_len = max(max_len, l1 + l2 + 1)
        return max_len

# 1041. Robot Bounded In Circle
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        cur_pos = [0, 0]
        cur_dir = (-1, 0)
        l_turn = {(0, 1):(-1, 0), (0, -1): (1, 0), (1, 0):(0, 1), (-1, 0): (0, -1)}
        r_turn = {(0, 1):(1, 0), (0, -1): (-1, 0), (1, 0):(0, -1), (-1, 0): (0, 1)}
        for instruction in instructions:
            if instruction == "G":
                cur_pos[0] += cur_dir[0]
                cur_pos[1] += cur_dir[1]
            elif instruction == "L":
                cur_dir = l_turn[cur_dir]
            elif instruction == "R":
                cur_dir = r_turn[cur_dir]
                
        if cur_pos == [0, 0] or cur_dir != (-1, 0):
            return True
        return False


# 895. Maximum Frequency Stack
from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.max_freq = 0
        

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.group[self.freq[val]].append(val)
        if self.freq[val] > self.max_freq:
            self.max_freq = self.freq[val]

    def pop(self) -> int:
        item = self.group[self.max_freq].pop()
        self.freq[item] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return item


# 36. Valid Sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.check_unique(row):
                return False
        for col in zip(*board):
            if not self.check_unique(col):
                return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                block = [board[k][l] for k in range(i, i + 3) for l in range(j, j + 3)]
                if not self.check_unique(block):
                    return False
        return True
    
    def check_unique(self, items):
        items = [item for item in items if item != "."]
        return len(items) == len(set(items))


# 37. Sudoku Solver
from collections import defaultdict, deque
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols, blocks = defaultdict(set), defaultdict(set), defaultdict(set)
        remain = deque()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    blocks[(i//3, j//3)].add(board[i][j])
                else:
                    remain.append((i, j))
        return self.dfs(board, rows, cols, blocks, remain)
        
    def dfs(self, board, rows, cols, blocks, remain):
        if not remain:
            return True
        i, j = remain.popleft()
        for k in range(1, 10):
            k = str(k)
            if k not in rows[i] and k not in cols[j] and k not in blocks[(i//3, j//3)]:
                rows[i].add(k)
                cols[j].add(k)
                blocks[(i//3, j//3)].add(k)
                board[i][j] = k
                if self.dfs(board, rows, cols, blocks, remain):
                    return True
                rows[i].remove(k)
                cols[j].remove(k)
                blocks[(i//3, j//3)].remove(k)
                board[i][j] = "."
        remain.appendleft((i, j))
        return False


# 381. Insert Delete GetRandom O(1) - Duplicates allowed
# 一定要用set做
import random
from collections import defaultdict
class RandomizedCollection(object):

    def __init__(self):
        self.vals, self.idxs = [], defaultdict(set)
        

    def insert(self, val):
        self.vals.append(val)
        self.idxs[val].add(len(self.vals) - 1)  #add the specific index
        return len(self.idxs[val]) == 1  #check if there is only one element no duplicate
        

    def remove(self, val):
        if self.idxs[val]:
            out, ins = self.idxs[val].pop(), self.vals[-1]  #self.idxs[val].pop() remove set() 隨機一個
            self.vals[out] = ins  #拿最後一個元素替換
            self.idxs[ins].add(out)  #一定要先add, 因為 add 的idx 是有可能要被remove的
            self.idxs[ins].discard(len(self.vals) - 1) # Cause we take the last one to fill the vacancy.
            self.vals.pop()
            return True
        return False 

    def getRandom(self):
        return random.choice(self.vals)


# Amazon | First unique word in a stream
# Coding exercise:

# Find the first word in a stream in which it is not repeated in the rest of the stream. 
# Please note that you are being provided a stream as a source for the characters. 
# The stream is guaranteed to eventually terminate 
# (i.e. return false from a call to the hasNext() method), though it could be very long. 
# You will access this stream through the provided interface methods. 
# A call to hasNext() will return whether the stream contains any more characters to process. 
# A call to getNext() will return the next character to be processed in the stream. It is not possible to restart the stream.

# Example:

# Input: The angry dog was red. And the cat was also angry.

# Output: dog

# In this example, the word ‘dog’ is the first word in the stream in which it is not repeated in the stream.

# Use one of the following skeletons for your solution:

Using a linked list to mimic LinkedHashMap / OrderedDict. 
keeping track of order by using a linked list and using a hash map to hash the node corresponding to each word
# 思路: 使用linked list and hash table
class Stream:

    def __init__(self, s):
        self.s = s
        self.pos = 0

    def hasNext(self):
        return self.pos < len(self.s)

    def getNext(self):
        if not self.hasNext: return
        temp = self.s[self.pos]
        self.pos += 1
        return temp

class WordNode:

    def __init__(self, word):
        self.word = word
        self.next = None
        self.cnt = 1

def unique_word(stream):
    buffr = itr = WordNode(None)
    _map = {}
    word = []
    while stream.hasNext():
        c = stream.getNext()
        if c in (' ', ',', '.', ';', ':'):
            if word:
                w = ''.join(word).lower()
                word = [] # set to default
                if w in _map:
                    _map[w].cnt += 1
                else: # create a new node
                    itr.next = WordNode(w)
                    itr = itr.next
                    _map[w] = itr
        else:
            word.append(c)
    head = buffr.next
    while head:
        if head.cnt == 1: 
            return head.word
        head = head.next
    return None


# 588. Design In-Memory File System
# trie classic
from collections import defaultdict
class TreeNode:
    
    def __init__(self):
        self.child = defaultdict(TreeNode)
        self.content = ""

class FileSystem:

    def __init__(self):
        self.root = TreeNode()
        
    def find(self, path):
        if len(path) == 1:
            return self.root
        cur = self.root
        for item in path.split("/")[1:]:
            cur = cur.child[item]
        return cur

    def ls(self, path: str) -> List[str]:
        file = self.find(path)
        if file.content:
            return [path.split("/")[-1]]
        else:
            return sorted(file.child.keys())
        

    def mkdir(self, path: str) -> None:
        self.find(path)
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        file = self.find(filePath)
        file.content += content
        

    def readContentFromFile(self, filePath: str) -> str:
        file = self.find(filePath)
        return file.content


# 642. Design Search Autocomplete System
# 思路: 使用trie, trie node 增加 hot, path attribute 來方便追蹤, 增加self.cur指針 => 避免多次從root 開始遍歷
from collections import defaultdict
class TrieNode:
    
    def __init__(self):
        self.childs = defaultdict(TrieNode)
        self.isWord = False
        self.hot = 0
        self.path = ""
    
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = self.cur = TrieNode()
        self.search = ""
        for sentence, time in zip(sentences, times):
            node = self.root
            path = ""
            for s in sentence:
                node = node.childs[s]
                path += s
                node.path = path
            node.isWord = True
            node.hot = -time
        
        
    def input(self, c: str) -> List[str]:
        if c == "#":
            self.cur.isWord = True
            self.cur.hot -= 1
            self.cur = self.root
            self.search = ''
        else:
            self.search += c
            if c not in self.cur.childs:
                cur_path = self.cur.path
                self.cur = self.cur.childs[c]
                self.cur.path = cur_path + c
            else:
                self.cur = self.cur.childs[c]
            result = []
            self.dfs(self.cur, result)
            return [item[1] for item in sorted(result)][:3]
    
    def dfs(self, cur, result):
        if cur.isWord:
            result.append((cur.hot, cur.path))
        for child in cur.childs:
            self.dfs(cur.childs[child], result)



# 第二轮算法 given list of tuples: [("a", "b"), ("b", "c".....] and a target word: "hello", 
# 要求判断能否用 tuples 的字母组成 target。 每个tuple 只能用一次， tuple里两个字母是二选一。


from collections import Counter
from collections import namedtuple
 
# return True if word can be formed
# false otherwise
def dfs(tuples: dict, d: dict):     # both are
    if len(d) == 0:     # all letters found match
        return True
 
 
    if len(tuples) == 0:    # no more avaliable tuples to choose
        return False
 
 
    for char, count in d.items():
        candidate_tuples = [t for t in tuples if char in t]     # all the tuples contain this
        for t in candidate_tuples:
            d[char] -= 1
            if d[char] == 0:
                del d[char]
 
            tuples[t] -= 1
            if tuples[t] == 0:
                del tuples[t]
 
            if dfs(tuples, d):
                return True
 
            # backtracking
            d[char] += 1
            tuples[t] += 1
 
    return False
 
 
def main(lst_of_tupules, target):
    # first, change the tuples into a dictionary, since only the count of each letter matters
    d = Counter(target)         # "hello" => {"h": 1, "e": 1, "l": 2, "o":1}
    tuples = Counter(lst_of_tupules)        # [("a", "b"), ("c", "d"), ("c", "d")]      =>  {("a", "b"): 1, ("c", "d"): 2} 
    return dfs(tuples, d)
 
 
"""Let the size of tuples be n, let the lenght of target word be n, 
Time: O(m ** n), Exponential
Space: O(m + n), since we create two additional dictionary
"""
 
 
if __name__ == '__main__':
    Test = namedtuple('Test', ['tuples_lst', 'target_word'])
    test1 = Test(tuples_lst = [("a", "b"), ("c", "d"), ("h", "e")], target_word="ade")
    assert(main(test1.tuples_lst, test1.target_word) == True)
 
    test2 = Test(tuples_lst = [("a", "b"), ("c", "d"), ("h", "e")], target_word="hello")
    assert(main(test2.tuples_lst, test2.target_word) == False)
 
    test3 = Test(tuples_lst = [("h", "e"), ("f", "e"), ("l", "e"), ("l", "e"), ("m", "n"), ("o", "h")], target_word="hello")
    assert(main(test3.tuples_lst, test3.target_word) == True)
 
    test4 = Test(tuples_lst = [("h", "e"), ("f", "e"), ("l", "e"), ("l", "e"), ("m", "n")], target_word="hello")
    assert(main(test4.tuples_lst, test4.target_word) == False)
 
    test5 = Test(tuples_lst = [("t", "e"), ("p", "u"), ("a", "b"), ("c", "d"), ("m", "n")], target_word="tupac")
    assert(main(test5.tuples_lst, test5.target_word) == False)
 
    test6 = Test(tuples_lst = [("t", "e"), ("p", "u"), ("a", "b"), ("c", "d"), ("u", "p")], target_word="tupac")
    assert(main(test6.tuples_lst, test6.target_word) == True)
 
    test7 = Test(tuples_lst = [("t", "e"), ("p", "u"), ("a", "b"), ("c", "d"), ("p", "u")], target_word="tupac")
    assert(main(test7.tuples_lst, test7.target_word) == True)


# 297. Serialize and Deserialize Binary Tree
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            res.append(node.val if node else "#")
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(map(str, res))
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data == "#":
            return None
        data_s = data.split(",")
        root = TreeNode(int(data_s[0]))
        idx = 1
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if data_s[idx] != "#":
                node.left = TreeNode(int(data_s[idx]))
                queue.append(node.left)
            idx += 1
            if data_s[idx] != "#":
                node.right = TreeNode(int(data_s[idx]))
                queue.append(node.right)
            idx += 1
        return root

# 17. Letter Combinations of a Phone Number
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return None
        memo = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], 
               "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], 
               "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        res = []
        self.digits = digits
        self.dfs(memo, 0, "", res)
        return res
    
    def dfs(self, memo, idx, path, res):
        if idx == len(self.digits):
            res.append(path)
            return
        for c in memo[self.digits[idx]]:
            self.dfs(memo, idx + 1, path + c, res)


# 140. Word Break II
# 重寫第四次, time complexity O(N^2(recursion) + 2^N(每個字斷點與不斷點) + W(construct the set)), space complexity O(N^2 + 2^N*N + W)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        memo = {}
        return [" ".join(words) for words in self.dfs(s, wordDict, memo)]
    
    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return [[]]
        res = []
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                remain = self.dfs(s[i+1:], wordDict, memo)
                for words in remain:
                    res.append([s[:i+1]] + words)
        memo[s] = res
        return memo[s]


# 101. Symmetric Tree
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.dfs(root.left, root.right)
    
    def dfs(self, left, right):
        if not left and not right:
            return True
        if None in [left, right]:
            return False
        if left.val == right.val:
            inner = self.dfs(left.right, right.left)
            outer = self.dfs(left.left, right.right)
            if inner and outer:
                return True
            return False
        return False


# 237. Delete Node in a Linked List
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


# 284. Peeking Iterator
# 思路: 建立 next_item pointer 以利peek method => self.next_item = self.iterator.next() if self.iterator.hasNext() else None
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.next_item = self.iterator.next() if self.iterator.hasNext() else None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.next_item
        

    def next(self):
        """
        :rtype: int
        """
        temp = self.next_item
        self.next_item = self.iterator.next() if self.iterator.hasNext() else None
        return temp

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.next_item != None


# 695. Max Area of Island
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = self.dfs(i, j, grid, m, n)
                    max_area = max(max_area, area)
        return max_area
                    
    def dfs(self, i, j, grid, m, n):
        directs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        area = 1
        grid[i][j] = 0
        for d in directs:
            x, y = i + d[0], j + d[1]
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                area += self.dfs(x, y, grid, m, n)
        return area


# 349. Intersection of Two Arrays, time complexity O(n), space complexity O(n)
from collections import Counter
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        res = []
        for key in count1:
            if key in count2:
                res.append(key)
        return res

# 350. Intersection of Two Arrays II
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()  #重點在這裡
        nums2.sort()
        res = []
        m, n = 0, 0
        while m < len(nums1) and n < len(nums2):
            if nums1[m] == nums2[n]:
                res.append(nums1[m])
                m += 1
                n += 1
            elif nums1[m] > nums2[n]:
                n += 1
            else:
                m += 1
        return res

# 322. Coin Change
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[-1] if dp[-1] != float("inf") else -1

# 460. LFU Cache
from collections import defaultdict
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        self.freq = 1

class DLinkedList:
    def __init__(self):
        self.sentinel = Node(None, None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self.size = 0
        
    def append(self, node):
        node.next = self.sentinel.next
        self.sentinel.next = node
        node.prev = self.sentinel
        node.next.prev = node
        self.size += 1
        
    def pop(self, node=None):
        if self.size == 0:
            return
        self.size -= 1
        if node == None:
            node = self.sentinel.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        return node
    
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.nodes = {}
        self.freqs = defaultdict(DLinkedList)
        self.min_freq = 0
        
    def update(self, node):
        freq = node.freq
        self.freqs[freq].pop(node)
        if freq == self.min_freq and self.freqs[freq].size == 0:
            self.min_freq += 1
        node.freq += 1
        self.freqs[node.freq].append(node)
        
    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self.update(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.nodes:
            node = self.nodes[key]
            self.update(node)
            node.val = value
            
        else:
            node = Node(key, value)
            if self.size == self.capacity:
                last = self.freqs[self.min_freq].pop()
                self.size -= 1
                del self.nodes[last.key]
            self.min_freq = 1
            self.size += 1
            self.nodes[node.key] = node
            self.freqs[1].append(node)


# 973. K Closest Points to Origin, time complexity O(nlogk)
# Use max_heap => 使得離原點愈近的點一直保留在heap
from heapq import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point
            item = (-(x**2 + y**2), (x, y))
            if len(heap) == k:
                heappushpop(heap, item)
            else:
                heappush(heap, item)
        return [item[1] for item in heap]


# 1296. Divide Array in Sets of K Consecutive Numbers
from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = Counter(nums)
        for n in sorted(count):
            if count[n] > 0:
                need = count[n]
                for i in range(n,n+k):
                    if count[i] < need:
                        return False
                    count[i] -= need
        return True


# 62. Unique Paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

# 63. Unique Paths II
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
            else:
                break
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

# 980. Unique Paths III
# time complexity O(3 ^ n), space complexity O(h)
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        remain = 0
        start_i, start_j = None, None
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    remain += 1
                if grid[i][j] == 1:
                    start_i, start_j = i, j
                    
        return self.dfs(grid, remain, start_i, start_j, m, n)
    
    def dfs(self, grid, remain, i, j, m, n):
        if 0 <= i < m and 0 <= j < n and grid[i][j] != -1:
            original = grid[i][j]
            if original == 2:
                return remain == 1
            grid[i][j] = -1
            res = 0
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for d in directions:
                x, y = i + d[0], j + d[1]
                res += self.dfs(grid, remain - 1, x, y, m, n)
            grid[i][j] = original
            return res
        else:
            return False


# 75. Sort Colors
# Three partition
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m1, m2 = 0, 0
        pivot = 1
        for i in range(len(nums)):
            if nums[i] == pivot:
                nums[i], nums[m2] = nums[m2], nums[i]
                m2 += 1
            elif nums[i] < pivot:
                nums[i], nums[m2] = nums[m2], nums[i]
                nums[m2], nums[m1] = nums[m1], nums[m2]
                m1 += 1
                m2 += 1



# 79. Word Search
# backtracking, time complexity O(mn*3^l), space complexity O(mn)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(i, j, board, word, 0):
                        return True
        return False
    
    
    def dfs(self, i, j, board, word, index):
        if index == len(word) - 1:
            return True
        m, n = len(board), len(board[0])
        direcs = [(1,0),(-1,0),(0,-1),(0,1)]
        temp = board[i][j]
        board[i][j] = "#"  #in-place modify 防止重複遍歷
        for d in direcs:
            x, y = i + d[0], j + d[1]
            if 0 <= x < m and 0 <= y < n and board[x][y] == word[index+1]:
                if self.dfs(x, y, board, word, index+1):
                    return True
        board[i][j] = temp  #backtracking, 修復回來


# 212. Word Search II
# Trie
class TrieNode:
    def __init__(self):
        self.childs = defaultdict(TrieNode)
        self.isWord = False
        self.path = ""
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.childs:
                prev_path = node.path
                node = node.childs[c]
                node.path = prev_path + c
            else:
                node = node.childs[c]
        node.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        res = set()
        trie = Trie()
        for word in words:
            trie.insert(word)
        for i in range(m):
            for j in range(n):
                cell = board[i][j]
                if cell in trie.root.childs:
                    node = trie.root.childs[cell]
                    self.dfs(i, j, board, node, res)
        return res
    
    def dfs(self, i, j, board, node, res):
        m, n = len(board), len(board[0])
        if node.isWord:
            res.add(node.path)
        temp = board[i][j]
        board[i][j] = "#"
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for d in directions:
            x, y = i + d[0], j + d[1]
            if 0 <= x < m and 0 <= y < n:
                cell = board[x][y]
                if cell in node.childs:
                    next_node = node.childs[cell]
                    self.dfs(x, y, board, next_node, res)
        board[i][j] = temp


# 535. Encode and Decode TinyURL
# 使用 enumerate(string.digits + string.ascii_letters)} 來產生 tinyURL
import string
class Codec:
    def __init__(self):
        self.urls = []
        self.base = {v:i for i, v in enumerate(string.digits + string.ascii_letters)}
        self.m = len(self.base)
        
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.urls.append(longUrl)
        n = len(self.urls)
        code = ""
        while n:
            c = n % self.m
            code += list(self.base.keys())[c]
            n //= self.m
        return "http://tinyurl.com/{}".format(code)
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        code = shortUrl.split("/")[-1][::-1]
        n = 0
        for c in code:
            idx = self.base[c]
            n = n * self.m + idx
        return self.urls[n-1]


# 64. Minimum Path Sum
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float("inf")] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]

# 133. Clone Graph
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        copy = {}
        node_copy = Node(node.val)
        copy[node] = node_copy
        self.dfs(node, copy)
        return node_copy
        
    def dfs(self, node, copy):
        for neighbor in node.neighbors:
            if neighbor not in copy:
                neighbor_copy = Node(neighbor.val)
                copy[neighbor] = neighbor_copy
                copy[node].neighbors.append(neighbor_copy)
                self.dfs(neighbor, copy)  # 持續往下copy
            else:
                copy[node].neighbors.append(copy[neighbor]) # 遇到已遍歷的node, 單純加入至neighbors 並不持續往下copy, 不然無限迴圈




































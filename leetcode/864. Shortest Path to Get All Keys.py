'''
We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall, "@" is the starting point, ("a", "b", ...) are keys, and ("A", "B", ...) are locks.

We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.  
We cannot walk outside the grid, or walk into a wall.  If we walk over a key, we pick it up.  
We can't walk over a lock unless we have the corresponding key.

For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter of the first K letters of the English alphabet in the grid.  
This means that there is exactly one key for each lock, and one lock for each key; 
and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys.  If it's impossible, return -1.

 

Example 1:

Input: ["@.a.#",
        "###.#",
        "b.A.B"]

Output: 8

Example 2:

Input: ["@..aA",
        "..B#.",
        "....b"]
Output: 6
 

Note:

1 <= grid.length <= 30
1 <= grid[0].length <= 30
grid[i][j] contains only '.', '#', '@', 'a'-'f' and 'A'-'F'
The number of keys is in [1, 6].  Each key has a different letter and opens exactly one lock.
'''

# 分析：

# 这道题就像我在498题中说的迷宫问题一样，求到达某点的最短路径，显然是用bfs
# 那么这和普通的bfs有什么不同呢，现在给出一个具体实例[[@…a],[.###A],[b.BCc]]，你会发现这里要走回头路的，那么如果凭空就可以来回走的话，会是一个死循环，
# 但我们稍微仔细思考一下，我认为想到走回头路的条件是获得一个新key这个点应该不难想到，那么我们只需要将标准bfs写法中的visited中key值变为(i,j,key)即可
# 虽然我做出来了，但是我的代码目前比较凌乱（因为经过多次修改），现在借助一位老哥的代码，和我的思路是完全一样的，来看一看具体如何实现
# 思路：

# 首先遍历一次数组，记录下起始位置，即‘@’，以及key的数量，即小写字母的数量，记为numOfKey
# 队列中的每项元素具有如下结构(i,j,step,key,collectedkey):
# i,j表示位置,step代表bfs的深度
# key代表目前能走的格子从，初始化为'abcdef.@'，每收集到一个小写字母便将对应的大写字母加入key中
# collectedkey代表已经收集的key的数量，如果collectedkey = numOfKey，则代表成功
# 用visited记录已经走过的状态，避免无限循环，visited中值为(i,j,key)，保证只有在收集到新key之后才能走回头路

# Time complexity: O(mn2^k)
# k: number of keys
# n: column length
# m: row length

#思路: 這題就是用到bfs的精神,找尋最短路徑, 記得visited keys 要排序 可以使得 O(mnk!) => O(mn2^k)
#此題還學到在判斷是否有物件重複上 set() 比 list() 有效率多
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
        n, m = len(grid), len(grid[0])
        numOfKeys = 0
        direc = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = set() #bfs set() 是一種習慣, 還有若用list() 效率會大幅降低 此題會TLE 雖然一樣可以解
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '@':  #起始點有可能不一樣, 紀錄起始點
                    starti = i  
                    startj = j
                elif grid[i][j] in "abcdef":  #先得知此迷宮有幾把鑰匙
                    numOfKeys += 1
        
        deque = collections.deque()
        deque.append([starti, startj, 0, ".@abcdef", 0])  #why ".@abcdef" 因為題目有說key最多6個 最少1個
        visited.add((starti, startj, ".@abcdef"))

        while deque:
            i, j, steps, keys, collectedKeys = deque.popleft()  #bfs, 注意這裡一定要用popleft, 得到的steps才是最少的,優先pop最早放進stack的物件(該物件steps也較晚放進來的小)

            if grid[i][j] in "abcdef" and grid[i][j].upper() not in keys:  #grid[i][j].upper() not in keys 注意! 因為有可能走回頭路
                keys += grid[i][j].upper()
                key = "".join(sorted(keys))  #記得給key 排序, 不然set一樣會重複
                collectedKeys += 1
            
            if collectedKeys == numOfKeys:
                return steps

            for (x, y) in direc:
                ni = i+x
                nj = j+y
                if 0<=ni<n and 0<=nj<m and grid[ni][nj] in keys:
                    if (ni, nj, keys) not in visited:  #走過的地方就不回頭再走,除非獲得新key
                        visited.add((ni,nj,keys))
                        deque.append([ni, nj, steps + 1, keys, collectedKeys])
                
        return -1

@@重要@@
# Python Sets vs Lists

# In Python, which data structure is more efficient/speedy? 
# Assuming that order is not important to me and I would be checking for duplicates anyway, is a Python set slower than a Python list?

# It depends on what you are intending to do with it.

# Sets are significantly faster when it comes to determining if an object is present in the set (as in x in s), 
# but are slower than lists when it comes to iterating over their contents.

a = "rwtaert"
sorted(a)
['a', 'e', 'r', 'r', 't', 't', 'w']
"".join(sorted(a))
'aerrttw'

# great job! A little suggestion: after the following line, it's better to sort the key in a certain order, 
# which would reduce the run time to 300+ ms

# if grid[i][j] in "abcdef" and grid[i][j].upper() not in keys:
#             keys += grid[i][j].upper()
              # keys = "".join(sorted(keys))

#重要 key: ".@abcdefABC" & ".@abcdefBAC" 是不一樣的, 但針對此題我們要把它視為一樣, 不然會重複走

# This is O(mnk!) not (Omn2^k) because your keys depend on in which order keys are discovered. 
# So the number of states is permutations of keys, which is k!. To make it 2^k, you should assign unique orders for each key (e.g. by sorting or using bits).


## more general approach

from collections import deque
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        keys = set()
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j].islower():
                    keys.add(grid[i][j])
                if grid[i][j] == "@":
                    queue.append(((i, j), [(i, j)], [0]*26))
        keys_num = len(keys)
        direcs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = {((0, 0), (0,) * 26)}
        while queue:
            for _ in range(len(queue)):
                cur, path, collects = queue.popleft()
                if sum(collects) == keys_num:
                    print(len(path) - 1)
                    print(path)
                    return len(path) - 1
                for d in direcs:
                    x, y = cur[0] + d[0], cur[1] + d[1]
                    next_collects = collects.copy()
                    if 0 <= x < m and 0 <= y < n and grid[x][y] != "#":
                        if grid[x][y].islower():
                            next_collects[ord(grid[x][y]) - ord("a")] = 1
                        elif grid[x][y].isupper():
                            start = next_collects[ord(grid[x][y]) - ord("A")]
                            if not start:
                                continue
                        if ((x, y), tuple(next_collects)) not in visited:
                            visited.add(((x, y), tuple(next_collects)))
                            queue.append(((x, y), path + [(x, y)], next_collects))
        return -1



















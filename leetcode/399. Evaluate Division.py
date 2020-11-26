'''
Equations are given in the format A / B = k, where A and B are variables represented as strings, 
and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , 
where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
'''

# Although this looks like a math problem, we can easily model it with graph.
# For example:
# Given:
# a/b = 2.0, b/c = 3.0
# We can build a directed graph:
# a -- 2.0 --> b -- 3.0 --> c
# If we were asked to find a/c, we have:
# a/c = a/b * b/c = 2.0 * 3.0
# In the graph, it is the product of costs of edges.

# Do notice that, 2 edges need to added into the graph with one given equation,
# because with a/b we also get result of b/a, which is the reciprocal of a/b.

# so the previous example also gives edges:
# c -- 0.333 --> b -- 0.5 --> a

# Now we know how to model this problem, what we need to do is simply build the
# graph with given equations, and traverse the graph, either DFS or BFS, to find a path
# for a given query, and the result is the product of costs of edges on the path.



# We can treat each equation as an edge, variables as nodes and value as weight, and build a weighted graph. Then for each queries (x, y), 
# we try to find a path from x to y. The answer is the product of all edges' weights. 
# If either x or y is not in graph or x and y are not connected in graph, the answer doesn't exist.
# We can use a defaultdict(dict) G to build a weighted graph and G[x][y] will be the weight of edge x->y which is the value of x / y

# So one solution is BFS (or DFS) for each query.
# Given the number of variables N, and number of equations E,
# building the graph takes O(E), each query takes O(N), N is vertex, space for graph takes O(E)




# 自己重寫, time complexity O(len(query)*N), build graph: O(E), 刷題用這個, 44ms
# 使用一般bfs 模板
from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (u,v), w in zip(equations, values):
            graph[u][v] = w
            graph[v][u] = 1/w
        return [self.bfs(a,b,graph) for (a, b) in queries]
    
    def bfs(self, src, dst, graph):
        if not src in graph or not dst in graph:
            return -1
        queue = deque([[src, 1]])
        seen = set([src])
        while queue:
            for _ in range(len(queue)):
                u, w = queue.popleft()
                if u == dst:
                    return w
                for v in graph[u]:
                    if v not in seen:
                        queue.append([v, w*graph[u][v]])
                        seen.add(v)
        return -1






# bfs, time complexity O(len(query)*N), 刷題用下面, 44ms
# 思路: 遇到directed grapgh + weight 慣用手法 => G = collections.defaultdict(dict) => G[a][b] = 5, G[b][a] = 1/5
# 利用 equations and values 先建立graph, 並從query 的(src, dst) 用bfs從src開始遍歷, 初始wight = 1, 看是否能找到dst, 每經過一個edge, 就要乘上edge weight
# 找到dst, 回報累積的weight, 這裡的bfs 有些許變形
import collections
class Solution(object):
    def calcEquation(self, equations, values, queries):
        G = collections.defaultdict(dict)  
        for (x, y), v in zip(equations, values):
            G[x][y] = v  #directed graph + weight 慣用手法
            G[y][x] = 1/v
        
        return [self.bfs(s, d, G) for s, d in queries]


    def bfs(self, src, dst, G):
        if not (src in G and dst in G):  #(True and False = False)
            return -1.0
        q = [(src, 1.0)] #起始點, weight 初始為1
        seen = set([src])
        for x, v in q:  #這裡q 會隨著下面q.append不斷增加, 但會接著往下走, 並照append 的先後順序, 所以是bfs
            if x == dst: 
                return v
            for y in G[x]:
                if y not in seen:  #跳過已遍歷過的 典型bfs 可看課本 不然a/b * b/a 回到原點
                    q.append((y, v*G[x][y]))
                    seen.add(y)          
        return -1.0 #無法到dst, return -1

a = [["a","b"],["b","c"]]
b = [2.0,3.0]
c = zip(a,b)
list(c)
[(['a', 'b'], 2.0), (['b', 'c'], 3.0)]

#bfs 變形
q = [1]
res = []
for i in q:
    print(i)
    if i == 5:
        print(res)
        break
    q.append(i+1)
    res.append(i)
1
2
3
4
5
[1, 2, 3, 4]



# One optimization, is to "compress" paths for
# past queries, which will make future searches faster. This is the same idea used in
# compressing paths in union find set. So after a query is conducted and a result is found,
# we add two edges for this query if these edges are not already in the graph.
# I think if we start to compress paths, the graph will grow to O(N^2), and we
# can optimize the query to O(1), please correct me if I'm wrong.

# Another solution is Union Find.
# Our root map is root and each root[x] is in form of (root(x), ratio) where ratio = x/root(x). If x == root(x), then ratio = 1.0. 
# So just consider root as a denominator here. 
# Then, we process the equations. For each x/y = v, we union x to y or set root(root(x)) = root(y) as y is the denominator. 
# After union all x, y in the equations, for each a, b in the queries, if a and b are not in the same union set, 
# then a and b are not transmissable to each other so a/b should return -1.0.

# Now that we have a ratio element in each root[x], we need to update it in find() and union() as well.
# In find(x), we have root[x] = (p, x/p) where p is the parent node of x and not neccessarily the root node. 
# But we will do path compression and recursively update all the parent nodes in the path to root. And ratio should be updated as well. 
# Eventually find(p) returns updated root[p] = (root(p), p/root(p)).
# So root[x] should be updated to (root(x), x/root(x)) = (root(p), x/p * p/root(p))) = (root[p][0], root[x][1] * root[p][1])
                                                                # x/(p/root(p)) => x/p * p/root(p)

# For union(x, y) in equations processing, we make root(root(x)) = root(y) as mentiond previously. 
# And for root[root(x)]'s ratio, as root(y) is root(x)'s new root, => new_ratio = root(x)/root(y)
# we update it to root(x)/root(y) = (x/y) * (y/root(y)) / (x/root(x)) = x/y * root[y][1] / root[x][1]. x/y is the provided equation outcome value.

# For queries(x,y), we can just simply return x/y = (x/root(x)) / (y/root(y)) = root[x][1]/root[y][1] if root(x) == root(y)

# Time: O(E+Q) , Union is approx O(1) because it's using path compression during find. Space:  O(E), 28ms, E: equations
# 思路: root[x] is in form of (root(x), ratio) where ratio = x/root(x). If x == root(x), then ratio = 1.0.
# union: a/b => b 為 a 的 parent node, a/c => c 為 b 的 parent node, 此時b的ratio 會因為c成為新的root而改變=> new_b_ratio = b/c
# find: root[x] =(p, x/p),需要更新ratio, 因為parent node 的ratio有可能改變了=>(p, x/p) => (root(x), x/root(x)) = (root(p), x/p * p/root(p))) = (root[p][0], root[x][1] * root[p][1])
# query: 確認x, y的 root node 是否一樣, 若不一樣則無法比較 return -1, 若一樣則return ratio_x/ratio_y
class Solution(object):
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        root = {}
        for (x, y), v in zip(equations, values):
            self.union(x, y, v, root)
        return [self.query(x, y, root) if x in root and y in root else -1.0 for x, y in queries]

    # if root(x) = root(y), equations "x / y" doable as (x/root(x)) / (y/root(y)) = xr / yr => x/y(ratio) * root(y)/root(x) = xr/yr
    # ratio * yr/xr = root(x)/root(y) == root[px][1], from root[px] = (py, ratio*(yr/xr))
    def union(self, x, y, ratio, root):
        px, xr, py, yr = *self.find(x, root), *self.find(y, root)
        if px != py: #使x的root node 認 y的root node 為parent node
            root[px] = (py, ratio*(yr/xr)) #update px的ratio

    # xr = x/parent(x), pr = parent(x)/root(x), update xr to xr*pr = x/root(x)
    def find(self, x, root):
        p, xr = root.setdefault(x, (x, 1.0))
        if x != p:
            r, pr = self.find(p, root)
            root[x] = (r, xr*pr)
        return root[x]

    def query(self, x, y, root):
        px, xr, py, yr = *self.find(x, root), *self.find(y, root)
        if px == py:
            return xr/yr
        return -1


#自己重寫 28ms
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        root = {}
        for (u, v) , w in zip(equations, values):
            self.union(u, v, w, root)
        return [self.query(a, b, root) if a in root and b in root else -1 for a, b in queries]
    
    def union(self, x, y, w, root):
        (px, xr), (py, yr) = self.find(x, root), self.find(y, root)
        if px != py:
            root[px] = (py, w*yr/xr)
    
    def find(self, x, root):
        p, xr = root.setdefault(x, (x, 1))
        if p != x:
            r, pr = self.find(p, root)
            root[x] = (r, xr*pr)
        return root[x]
    
    def query(self, x, y, root):
        px, xr, py, yr = *self.find(x, root), *self.find(y, root)
        if px == py:
            return xr/yr
        return -1




a = {}
a.setdefault(4,(1,2)) #第一次setdefault的條件不會被第二次以上覆蓋
(1, 2)
a
{4: (1, 2)}
a.setdefault(4,(3,4))
(1, 2)
a
{4: (1, 2)}

# equations = [ ["a", "b"], ["b", "c"] ]
# values = [2.0, 3.0]
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
# a = zip(equations,values)
# a
# <zip at 0x10e887748>
# [(x,y) for x,y in a]
# [(['a', 'b'], 2.0), (['b', 'c'], 3.0)]

# [((x,y), v) for (x,y), v in a]
# [(('a', 'b'), 2.0), (('b', 'c'), 3.0)]


















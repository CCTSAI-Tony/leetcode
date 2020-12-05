leetcode: 322, 221, 124, 428, 235, 547

from collections import defaultdict
def bestTrio(friend_nodes, friends_edges, friends_from, friends_to):
    graph = defaultdict(set)
    for f, t in zip(friends_from, friends_to):
        graph[f].add(t)
        graph[t].add(f)
        trios = set()
        for i in range(1, friend_nodes + 1):
            for f1 in graph[i]:
                for f2 in graph[f1]:
                    if i in graph[f2]:
                        group = sorted([i, f1, f2])
                        trios.add(tuple(group))
    if not trios:
        return -1
    score = 0
    for f1, f2, f3 in trios:
        degree = 0
        for f in [f1, f2, f3]:
            degree += len(graph[f])
        degree -= 6
        score += degree
    return score
                
        
        
bestTrio(6, 6, [1,2,2,3,4,5], [2,4,5,5,5,6])       


def waysToSum(n: int, k: int) -> int:
    mod = 10**9 + 7
    coins = [i for i in range(1, k + 1)]

    f = [1] + [0] * n
    for coin in coins:
        for i in range(coin, n + 1):
            f[i] += f[i - coin]
    return f[n] % mod

    
waysToSum(5, 3)





from collections import defaultdict
class NTreeNode:
    def __init__(self, val = 0):
        self.val = val
        self.child = []
def theJungleBook(predators):
    Tree = []
    for i in range(len(predators)):
        node = NTreeNode(i)
        Tree.append(node)
    for i in range(len(predators)):
        if predators[i] != -1:
            node = Tree[predators[i]]
            node.child.append(Tree[i])
    levels = defaultdict(list)
    for i in range(len(predators)):
        if predators[i] == -1:
            root = Tree[i]
            dfs(root, 1, levels)
    return len(list(levels.keys()))
        
def dfs(node, level, levels):
    levels[level].append(node)
    for nxt in node.child:
        dfs(nxt, level + 1, levels)


#time complexity O(nlogn), space complexity O(n)
def universityCareerFair(arrival, duration):
    aux = sorted(list(zip(arrival, duration)), key=lambda p: (sum(p), p[1])) #sum(p) = 以結束時間排序, 相同結束時間, duration 越小排前面 => greedy, 個人認為以p[1] 排序是多餘的
    ans, end = 0, -float('inf')
    for star, dur in aux:
        if star >= end:
            ans, end = ans + 1, star + dur
    return ans
    

print(universityCareerFair([1, 3, 3, 5, 7], [2, 2, 1, 2, 1])) # 4
print(universityCareerFair([1, 2], [7, 3])) # 1


from collections import deque
class NTreeNode:
    def __init__(self, val=0):
        self.val = val
        self.child = deque()
from collections import defaultdict
def bestSumAnyTreePath(parent, values):
    tree = []
    for i in range(len(values)):
        node = NTreeNode(values[i])
        tree.append(node)
    for i in range(len(parent)):
        if parent[i] != -1:
            tree[parent[i]].child.append(tree[i])
    max_sum = float("-inf")
    stack = []
    d = defaultdict(list)
    t = defaultdict(int)
    root = tree[0]
    while root or stack:
        while root.child:
            stack.append(root)
            root = root.child[0]
        node = root
        if stack:
            root = stack.pop()
            root.child.popleft()
            d[root].append(node)
        else:
            root = None
        first, second = 0, 0
        if d[node]:
            first = max(first, max(t[c] for c in d[node]))
        for k in d[node]:
            if t[k] == first:
                d[node].remove(k)
        if d[node]:
            second = max(second, max(t[c] for c in d[node]))
        max_sum = max(max_sum, node.val + first + second)
        t[node] = node.val + first
    return max_sum
        
bestSumAnyTreePath([-1, 0, 1, 2, 0], [5, 7, -10, 4, 15]) 




















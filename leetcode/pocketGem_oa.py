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



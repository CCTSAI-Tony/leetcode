from collections import defaultdict
def waysToSum(total, k):
    memo = defaultdict(set)
    arr = range(1, k+1)
    dfs(total, arr, memo)
    return len(memo[total]) % (10**9 + 7)
    
def dfs(t, arr, memo):
    if t in memo or t == 0:
        return memo[t]
    for num in arr:
        temp = t - num
        if temp == 0:
            memo[t].add((num,))
        elif temp < 0:
            break
        for comb in dfs(temp, arr, memo):
            temp = comb + (num,)
            temp = sorted(list(temp))
            memo[t].add(tuple(temp))
    return memo[t]
   
waysToSum(8,2)



from collections import deque
def diskSpaceAnalysis(n, x, space):
    queue = deque()
    min_space = []
    s = 0
    for i in range(n-1):
        helper(queue, i, space)
    for e in range(x-1, n):
        helper(queue, e, space)
        if queue[0] < s:
            queue.popleft()
        s += 1
        min_space.append(space[queue[0]])
    return max(min_space)
        
        
        
def helper(queue, i, space):
    while queue and space[queue[-1]] >= space[i]:
        queue.pop()
    queue.append(i)

    
diskSpaceAnalysis(4, 2, [8,2,4,6])
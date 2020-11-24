# Given an mxn grid of 0s,1s and 2s (0 denoting an obstacle, 1 denoting empty cell and 2 denoting cell with gold).
# Find the path used to reach from (0,0) to (m - 1, n - 1) collecting maximum gold if you are allowed to travel in any four directions and can take a maximum of k steps.
# Given {operator - precedence - explanation} :
# a. '!' -1 - x!y = (y - x) % 10007
# b. '@' -1 - x@y = (x + y) % 10007
# c. '#' - 2 - x#y = (xxy) % 10007
# d. '$' - 2 - x$y = (xyy) % 10007
# Operators with higher precedence have higher priority.
# Operators with precedence 1 are calculated from left to right and those with precedence 2 are calculated right to left. Operations in paranthesis() have higher priority.
# Given an expression consisiting of the operators, paranthesis and digits, find it's result.
# Eg. 1!(2$1) = 1
# Eg. 1$2#3 = 144

# 這個答案是錯的
# 思路: 只記住gold 的visited, 因為若記住empted cell的話, 回程會回不來
from itertools import combinations
from collections import Counter
from collections import defaultdict
from collections import deque


def bfs(grid, k):
    q = deque()
    # initialize origin point and also collected gold and steps taken
    q.append((0, 0, 0, 0, [], set()))
    # initialize possible movement dirs
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    gold_max = 0
    max_path = None
    while q:
        x, y, gold, steps, path, hit_gold = q.popleft()
        for px, py in dirs:
            curr_x = x+px
            curr_y = y+py
            if 0 <= curr_x < len(grid[0]) and 0 <= curr_y < len(grid):
                if curr_x == len(grid[0])-1 and curr_y == len(grid)-1:
                    if gold > gold_max:
                        gold_max = max(gold, gold_max)
                        max_path = path
                elif steps < k:
                    if grid[curr_y][curr_x] == 1:
                        q.append((curr_x, curr_y, gold, steps+1, path+[(curr_x, curr_y)], hit_gold))
                    elif grid[curr_y][curr_x] == 2 and (curr_x, curr_y) not in hit_gold:
                        q.append((curr_x, curr_y, gold+1, steps + 1,
                                  path + [(curr_x, curr_y)], hit_gold | {(curr_x, curr_y)}))
    return max_path, gold_max


grid = [[1, 1, 2], [1, 1, 0], [0, 2, 1], [0, 1, 1], [1, 1, 1]]
k = 9

print(bfs(grid, k))


def searchSnippet(s, q1, q2):
    s_list = s.split()
    s, e = 0, 0
    max_len = float("inf")
    sd, ed = 0, 0
    for e in range(len(s_list)):
        start = s_list[s][:-1].lower() if not s_list[s].isalpha() else s_list[s].lower()
        end = s_list[e][:-1].lower() if not s_list[e].isalpha() else s_list[e].lower()
        if end in [q1, q2]:
            if start in [q1, q2] and (e-s) < max_len:
                sd, ed = s, e
                max_len = (e-s)
            s = e
    if sd < 3:
        return " ".join(s_list[0:ed+4])
    return " ".join(s_list[sd-3:ed+4])


searchSnippet("Say hello to the world, Hello World", "hello", "world")


def buildNewRoads(road_list):
    n, m = road_list[0]
    roads = defaultdict(list)
    for i, j in road_list[1:]:
        roads[i].append(j)
        roads[j].append(i)
    visited = set()
    counts = 0
    for i in range(n):
        if i not in visited:
            counts += 1
            dfs(i, visited, roads)
    return counts - 1


def dfs(i, visited, roads):
    if i in visited:
        return
    visited.add(i)
    for j in roads[i]:
        dfs(j, visited, roads)


buildNewRoads([(4, 2), (0, 1), (1, 2)])


def blackJackProbability(N, S, X):
    cards = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
             "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
    pool = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4
    initial = Counter(S)
    points = sum(cards[k]*initial[k] for k in initial)
    if points > 21:
        return 0
    for s in S:
        pool.remove(s)
    remain = 21 - points
    safe = []
    combs = combinations(pool, X)
    combs = list(combs)
    for comb in combs:
        temp = sum(cards[k] for k in comb)
        if temp <= remain:
            safe.append(comb)
    prob = len(safe) / len(list(combs))
    return round(prob, 6)


blackJackProbability(2, "K8", 2)


def versionControl(v1, v2):
    v1 = v1.replace("-", ".")
    v2 = v2.replace("-", ".")
    v1 = v1.split(".")
    v1 += ["0"] * (4-len(v1))
    v2 = v2.split(".")
    v2 += ["0"] * (4-len(v2))
    for t1, t2 in zip(v1, v2):
        if t1.isalpha() and not t2.isalpha():
            return -1
        elif not t1.isalpha() and t2.isalpha():
            return 1
        elif t1.isalpha() and t2.isalpha():
            return 0
        if int(t1) > int(t2):
            return 1
        elif int(t2) > int(t1):
            return -1
    return 0


versionControl("1.0.0-alpha", "1.0.0")


def selectPairs(arr):
    n = arr[0]
    nums = arr[1:]
    su = sum(nums)
    dp = [[False for j in range(su+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1, n+1):
        for j in range(1, su+1):
            dp[i][j] = dp[i-1][j]
            if nums[i-1] <= j:
                dp[i][j] |= dp[i-1][j-nums[i-1]]
    for j in range(su//2, -1, -1):
        if dp[-1][j]:
            diff = su - (2*j)
            break
    return diff


selectPairs([5, 6, 7, 8, 10, 11])


def smallestRectangle(arr):
    n, k = arr[0]
    points = arr[1:]
    if k >= len(points):
        return 0
    memo = {}
    return dfs(points, k, memo)


def dfs(points, k, memo):
    if (tuple(points), k) in memo:
        return memo[(tuple(points), k)]
    x_min, x_max, y_min, y_max = float("inf"), float("-inf"), float("inf"), float("-inf")
    for point in points:
        x_min = min(x_min, point[0])
        x_max = max(x_max, point[0])
        y_min = min(y_min, point[1])
        y_max = max(y_max, point[1])
    if k == 1:
        return (x_max-x_min) * (y_max-y_min)
    if k == len(points):
        return 0
    min_area = float("inf")
    for x in range(x_min, x_max+1):
        l = [point for point in points if point[0] <= x]
        r = [point for point in points if point[0] > x]
        if len(r) < k-1:
            continue
        temp = dfs(l, 1, memo) + dfs(r, k-1, memo)
        min_area = min(min_area, temp)

    for x in range(x_max, x_min-1, -1):
        l = [point for point in points if point[0] < x]
        r = [point for point in points if point[0] >= x]
        if len(l) < k-1:
            continue
        temp = dfs(l, k-1, memo) + dfs(r, 1, memo)
        min_area = min(min_area, temp)
    for y in range(y_min, y_max+1):
        l = [point for point in points if point[1] <= y]
        r = [point for point in points if point[1] > y]
        if len(r) < k-1:
            continue
        temp = dfs(l, 1, memo) + dfs(r, k-1, memo)
        min_area = min(min_area, temp)

    for x in range(y_max, y_min-1, -1):
        l = [point for point in points if point[0] < y]
        r = [point for point in points if point[0] >= y]
        if len(l) < k-1:
            continue
        temp = dfs(l, k-1, memo) + dfs(r, 1, memo)
        min_area = min(min_area, temp)
    memo[(tuple(points), k)] = min_area
    return memo[(tuple(points), k)]


smallestRectangle([(4, 2), (1, 1), (1, 5), (1, 6), (1, 7)])


def commonElementsInArray(arr1, arr2):
    a1 = Counter(arr1)
    a2 = Counter(arr2)
    res = []
    for num in range(1000):
        if num in a1 and num in a2:
            q = min(a1[num], a2[num])
            temp = [num] * q
            res += temp
    return res


commonElementsInArray([3, 1, 3], [3, 3])


def realProgrammerGame(N, M, K):
    count = N//M + 1 if N % M else N//M
    if K < count:
        return 0.0000
    prob = 0
    prev = 0
    for k in range(count, K+1):
        comb = helper(count, k)
        prob += (comb-prev) * 0.5**k
        prev = comb
    return prob


def helper(count, k):
    temp1, num = 1, k
    for _ in range(count):
        temp1 *= num
        num -= 1
    temp2, num = 1, 1
    for _ in range(count):
        temp2 *= num
        num += 1
    return temp1 / temp2


realProgrammerGame(100, 5, 2)


def realProgrammerGame(N, M, K):
    dp = [1.0] + [0.0] * (N - 1)
    for _ in range(K):
        newdp = [0] * N
        for i in range(len(dp)):
            if dp[i] > 0:
                for j in range(M + 1):
                    if i + j < N:
                        newdp[i + j] += dp[i] / (M + 1)
        dp = newdp
    return 1 - sum(dp)


realProgrammerGame()


def incrementalMemoryLeak(*args):
    n = args[0]
    for m1, m2 in args[1:]:
        print(helper(m1, m2))


def helper(m1, m2):
    queue = [(m1, m2, 0)]
    while queue:
        t1, t2, s = queue.pop()
        if s > t1 and s > t2:
            return (s, t1, t2)
        if t1 >= t2:
            queue.append((t1-s, t2, s+1))
        elif t1 < t2:
            queue.append((t1, t2-s, s+1))


incrementalMemoryLeak(2, (2, 2), (8, 11))


def incrementalMemoryLeak(*args):
    n = args[0]
    for m1, m2 in args[1:]:
        l, t1, t2 = binary(m1, m2)
        print(helper(t1, t2, l+1))


def helper(m1, m2, t):
    queue = [(m1, m2, t)]
    while queue:
        t1, t2, s = queue.pop()
        if s > t1 and s > t2:
            return (s, t1, t2)
        if t1 >= t2:
            queue.append((t1-s, t2, s+1))
        elif t1 < t2:
            queue.append((t1, t2-s, s+1))


def binary(m1, m2):
    if m1 == m2:
        return 0, m1, m2
    if m1 > m2:
        l, r = 0, 10**9
        while l + 1 < r:
            mid = l + (r-l) // 2
            temp = (0+mid)*(mid-0+1)/2
            if m1 - temp > m2:
                l = mid
            elif m1 - temp <= m2:
                r = mid
        if m1 - (0+l)*(l-0+1)/2 < m2:
            return l - 1, m1 - (0+l)*(l-0+1)/2 + l, m2
        if m1 - (0+l)*(l-0+1)/2 == m2:
            return l, m1 - (0+l)*(l-0+1)/2, m2
        if m1 - (0+r)*(r-0+1)/2 < m2:
            return r-1, m1 - (0+r)*(r-0+1)/2 + r, m2
        if m1 - (0+r)*(r-0+1)/2 == m2:
            return r, m1 - (0+r)*(r-0+1)/2, m2
    if m1 < m2:
        l, r = 0, 10**9
        while l + 1 < r:
            mid = l + (r-l) // 2
            temp = (0+mid)*(mid-0+1)/2
            if m2 - temp > m1:
                l = mid
            elif m2 - temp <= m1:
                r = mid
        if m2 - (0+l)*(l-0+1)/2 < m1:
            return l - 1, m1, m2 - (0+l)*(l-0+1)/2 + l
        if m2 - (0+l)*(l-0+1)/2 == m1:
            return l, m1, m2 - (0+l)*(l-0+1)/2
        if m2 - (0+r)*(r-0+1)/2 < m1:
            return r-1, m1, m2 - (0+r)*(r-0+1)/2 + r
        if m2 - (0+r)*(r-0+1)/2 == m1:
            return r, m1, m2 - (0+r)*(r-0+1)/2


incrementalMemoryLeak(2, (2, 2), (8, 11))


def minimumCharacterTransformation(s1, s2):
    m = {}
    if not check(s1, s2, m):
        return -1
    count = 0
    visited = set()
    for k in m:
        if k not in visited:
            count += helper(k, m, visited, 0)
    return count


def helper(k, m, visited, path):
    if k not in m:
        return path
    if k in visited:
        return path+1
    visited.add(k)
    return helper(m[k], m, visited, path+1)


def check(s1, s2, m):
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            continue
        elif s1[i] not in m:
            m[s1[i]] = s2[i]
        elif m[s1[i]] != s2[i]:
            return False
    return True


minimumCharacterTransformation("abc", "efg")

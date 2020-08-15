'''
Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]


Follow up:

What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?
'''


# Since there is no standard TreeMap library for python, I am implementing this structure with a min heap.
# The idea is straight froward:
# Append interval to heap when addNum called
# Merge intervals when getIntervals called

# python solution using heap, 刷題用這個 利用heap排序 好招學起來
import heapq as hq
class SummaryRanges:

    def __init__(self):
        self.intervals = []
        self.visited = set()  # 這邊也可用list [], 但runtime 會提升

    def addNum(self, val: int) -> None:  #跟下面方法比較 這裡 add num 沒merge, 所以get intervals 要用while loop 來不斷merge
        if val not in self.visited:
            hq.heappush(self.intervals, [val, val])
            self.visited.add(val)

    def getIntervals(self) -> List[List[int]]:
        res = []
        while self.intervals:
            res.append(hq.heappop(self.intervals))  # heappop(self.intervals) pop 出 最小的[val,val]
            # 這步進行marge, 若前面沒有去除重複 這邊要改成 res[-1][1]+1 >= self.intervals[0][0]
            while self.intervals and (res[-1][1]+1 == self.intervals[0][0]):
                res[-1][1] = hq.heappop(self.intervals)[1]  # (1,6) (7,10) => (1,10), 記得要pop,
        self.intervals = res  # update self.intervals, 以利下次使用
        return res
# why update 後 self.intervals不用heapify, 因為原本就以排好序, 之後heappush自然就會自動堆疊


# 若前面沒有去除重複 visited 這邊要改成

def getIntervals(self) -> List[List[int]]:
    res = []
    while self.intervals:
        res.append(hq.heappop(self.intervals))
        while self.intervals and (res[-1][1]+1 >= self.intervals[0][0]):  # 記得 >=, 因為重複的起頭 有可能比上一個end小
            res[-1][1] = max(res[-1][1], hq.heappop(self.intervals)[1])
    self.intervals = res
    return res


# simple python solution with binary search, 面試用這個, 刷題用這個
# 模板1
class SummaryRanges:
    def __init__(self):
        self.intervals = []

    def merge(self, idx):
        # idx+1 < len(self.intervals) and idx >= 0, 確保都在區間內 不然會報錯
        if idx+1 < len(self.intervals) and idx >= 0 and self.intervals[idx+1][0]-self.intervals[idx][1] <= 1:
            self.intervals[idx][1] = max(self.intervals[idx][1], self.intervals[idx+1][1])
            self.intervals.pop(idx+1)  # 指定pop index + 1位置, 合併成功

    def addNum(self, val: int) -> None:  # add number自動進行merge
        l, r = 0, len(self.intervals)-1
        while l <= r:
            mid = (l+r)//2
            if self.intervals[mid][0] >= val:  # 利用binary search 確認要插在哪, 依照[val, val] 第一個元素比較
                r = mid - 1
            else:
                l = mid + 1

        # 極端case (1,4), (5,5), (6,10)->(1,4),(5,10)->(1,10), insert(l) 位置, 先跟後併再跟前併
        self.intervals.insert(l, [val, val])
        self.merge(l)  # ex: (4,4), (5,8), corner case (4,4),(4,8) 不會重現重複, (4,4), (6,8) 不能maerge
        self.merge(l-1)  # 看是否可以被前一個index merge, ex: (3,7),(5,5), 
                          #這種情況merge發生 self.intervals[idx+1][0]-self.intervals[idx][1] <= 1, 因為(5,5)已在(3,7) 區間內, 
    def getIntervals(self) -> List[List[int]]:
        return self.intervals


# Follow up:

# What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?
# ans: use binary search


# Short Python Union-Find Solution

# Idea:

# on every new element (if doesn't exist in union find)
# perform union with val-1, val+1
# on union perform interval adjustment
# together with union-find forest maintain intervals for the roots of the trees
# make_set:

# on make set create a new interval with [x,x]
# union:

# on union we need to remove one interval (the one which is not root anymore)
# merge the union by taking the min of the start and max of the end
# getIntervals:

# return all intervals in the sorted order
# Complexity:

# O(1) for addNum
# O(nlogn) for getIntevals where n is number of unique intervals
class DSU:
    def __init__(self):
        self.p = {}
        self.intervals = {}

    def exists(self, x):
        return x in self.p  # if x in self.p return True

    def make_set(self, x):
        self.p[x] = x  # 建立key: val
        self.intervals[x] = [x, x]  # 建立key: val

    def find(self, x):
        if not self.exists(x):
            return None

        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])

        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)

        if xr is None or yr is None:  # val+1, val-1 都沒出現
            return

        self.p[xr] = yr  # 在self.p[xr]紀錄被併入到哪裡

        # interval adjusting logic
        x_interval = self.intervals[xr]
        del self.intervals[xr]  # del key

        self.intervals[yr] = [min(self.intervals[yr][0], x_interval[0]),
                              max(self.intervals[yr][1], x_interval[1])]


class SummaryRanges:
    def __init__(self):
        self.dsu = DSU()

    def addNum(self, val: int) -> None:
        if self.dsu.exists(val):  # 避免重複
            return

        self.dsu.make_set(val)

        self.dsu.union(val, val-1)  # 先被小的併
        self.dsu.union(val, val+1)  # 再被大的併, 順序顛倒沒差

    def getIntervals(self) -> List[List[int]]:
        return sorted(self.dsu.intervals.values())  # 依照dict val 排序, time complexity O(nlogn)

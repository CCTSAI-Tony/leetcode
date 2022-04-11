'''
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
 

Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
 

Constraints:

1 <= length <= 50000
At most 50000 calls will be made to set, snap, and get.
0 <= index < length
0 <= snap_id < (the total number of times we call snap())
0 <= val <= 10^9
'''


# Backward While Loop
# We can make this search faster by replacing linear query with a binary search

#刷題用這個 time complexity set O(1), get O(n), space complexity O(n)
#思路: 使用defaultdict(dict), 利用copy_id 來節省空間, 有set的元素才會紀錄在對應的snap_id 裡, 
#使用while loop 來線性尋找有該index存在且離snap_id 最近的id, 因為這中間該index 元素沒變過, 這樣能節省空間 => 重要!! 類似掃描線概念
from collections import defaultdict
class SnapshotArray:
    def __init__(self, length: int):
        self.snap_id = 0
        self.history = defaultdict(dict)
    
    def set(self, index: int, val: int) -> None:
        self.history[self.snap_id][index] = val
    
    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
    
    def get(self, index: int, snap_id: int) -> int: #若index 不在snap_id 找尋最近一次變動的copy_id, 因為元素沒更動, 不會登記在新id => 節省空間
        copy_id = snap_id
        while copy_id > 0 and index not in self.history[copy_id]:
            copy_id -= 1
        if index in self.history[copy_id]:
            return self.history[copy_id][index]
        return 0


# 重寫第二次, time complexity set O(1), get O(n), space complexity O(n)
from collections import defaultdict
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.history = defaultdict(dict)

    def set(self, index: int, val: int) -> None:
        self.history[self.snap_id][index] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        copy_id = snap_id
        while copy_id and index not in self.history[copy_id]:
            copy_id -= 1
        if index in self.history[copy_id]:
            return self.history[copy_id][index]
        return 0


# 重寫第三次, 使用bisect => time complexity set O(1), get O(logn), space complexity O(n)
from bisect import bisect
class SnapshotArray:

    def __init__(self, length: int):
        self.array = [[(-1, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.array[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect(self.array[index], (snap_id + 1, ))
        return self.array[index][i-1][1]


# 重寫第四次, 不用bisect, time complexity set O(1), get O(logn), space complexity O(n)
class SnapshotArray:

    def __init__(self, length: int):
        self.array = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.array[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        i = self.binary_search(self.array[index], (snap_id + 1))
        return self.array[index][i-1][1]
    
    def binary_search(self, array, target):
        left, right = 0, len(array) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if array[mid][0] < target:  # 不能<=, 在相同smap_id 元素區間裡, 我們要取最左端 
                left = mid
            else:
                right = mid
        if array[right][0] < target:
            return right + 1
        if array[right][0] == target or array[left][0] < target:
            return right
        return left


Backward Binary Search
Code Snippet from @lee215

#刷題用這個, bisect.bisect = bisect.bisectright, time complexity set O(1), get O(logn), space complexity O(n)
#思路: 使用bisect.bisect 相當於 (bisect.bisectright) 來尋找最近的snap_id
#使用bisect.bisect 因為搜尋只用到單一元素, 因此會排在正確snap_id的最左邊, 所以要snap_id + 1, 若沒有該正確snap_id, 也會找到離正確最近的snap_id的最右邊的位置
#用到單一元素[snap_id]是為了區分同snap_id 的所有元素, 使用bisect.bisect 會把單一元素排在(相同snap_id, 不同val)  元素最左邊
import bisect
class SnapshotArray:
    def __init__(self, n):
        self.A = [[[-1, 0]] for _ in range(n)]
        self.snap_id = 0

    def set(self, index, val):
        self.A[index].append([self.snap_id, val])

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        i = bisect.bisect(self.A[index], [snap_id + 1]) - 1
        return self.A[index][i][1]

import bisect
a = [[1,100], [2,200], [3,300]]
bisect.bisect(a, [2]) => 1
bisect.bisect(a, [2,200]) => 2

#自己重寫, time complexity set O(1), get O(logn), space complexity O(n)
import bisect
class SnapshotArray:

    def __init__(self, length: int):
        self.A = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0
        
        
    def set(self, index: int, val: int) -> None:
        self.A[index].append([self.snap_id, val])
        

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect(self.A[index], [snap_id+1]) - 1
        return self.A[index][i][1]



Brute Force | Memory Limit Exceeded
Memory usage needs to be more efficient. In this code snippet, too many unused 0 element were stored in the dictionary value. 
Instead, only store used index and value. A nested dictionary does the trick

class SnapshotArray(object):

    def __init__(self, length):
        self.length = length
        self.arr = [0] * self.length
        self.snap_id = -1
        self.dic = {}
        

    def set(self, index, val):
        if index >= 0 and index < len(self.arr):
            self.arr[index] = val

    def snap(self):
        self.snap_id += 1
        self.dic[self.snap_id] = self.arr[:]
        return self.snap_id
        

    def get(self, index, snap_id):
        if snap_id in self.dic:
            return self.dic[snap_id][index]


# Hashmap + Deepcopy
# This code snippet still duplicates previous snap_array, thus create redundency in elements. for example:

from collections import defaultdict
class SnapshotArray(object):
    def __init__(self, length):
        self.dic = defaultdict(dict)
        self.snap_id = 0
        
        
    def set(self, index, val):
        self.dic[self.snap_id][index] = val
        

    def snap(self):
        self.snap_id += 1
        self.dic[self.snap_id] = self.dic[self.snap_id - 1].copy()
        return self.snap_id -1
        

    def get(self, index, snap_id):
        if index in self.dic[snap_id]:
            return self.dic[snap_id][index]
        else:
            return 0

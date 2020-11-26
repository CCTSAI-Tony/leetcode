'''
Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").
 

Example 1:

Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:   
TimeMap kv;   
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1   
kv.get("foo", 1);  // output "bar"   
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"   
kv.set("foo", "bar2", 4);   
kv.get("foo", 4); // output "bar2"   
kv.get("foo", 5); //output "bar2"   

Example 2:

Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], 
inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output: [null,null,null,"","high","high","low","low"]
 

Note:

All key/value strings are lowercase.
All key/value strings have length in the range [1, 100]
The timestamps for all TimeMap.set operations are strictly increasing.
1 <= timestamp <= 10^7
TimeMap.set and TimeMap.get functions will be called a total of 120000 times (combined) per test case.
'''

# Python Binary Search Solution

# The idea is using binary search to find the closest timestamp_prev in TimeMap


# a common bug in binary search is to do mid = (l + r) // 2 as the sum can overflow. 
# A better approach to calculate the middle is: mid = l + (r - l)//2


# But, there is no overflow in python

# True, still a good thing to point out. That gives the interviewer the data that you think beyond just your code.


#使用模板2, 刷題用這個
#思路: 利用defaultdict list 來儲存同一個key 不同timestamp 的值, 再利用binary search 來找time_prev <= timestamp 的值
import collections
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        li = self.dic[key]
        n = len(li)
        l, r = 0, n-1
        if n == 0:
            return ""
        if li[0][1] > timestamp:
            return ""
        while l + 1 < r:
            mid = l + (r-l) // 2
            if timestamp == li[mid][1]:
                return li[mid][0]
            elif timestamp > li[mid][1]:
                l = mid 
            else:
                r = mid    
        if li[r][1] <= timestamp:  #這裡要做判斷, 記得 <=, 因為 li[r][1] 有可能就是 timestamp
            return li[r][0]
        else:
            return li[l][0]
# 使用模板1 刷題用這個
import collections
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        li = self.dic[key]
        n = len(li)
        l, r = 0, n-1
        
        while l <= r:
            mid = l + (r-l) // 2
            if timestamp == li[mid][1]:
                return li[mid][0]
            elif timestamp > li[mid][1]:
                l = mid + 1
            else:
                r = mid - 1
                
        
        
        return "" if l == 0 else li[r][0]  #why li[r][0] 此題目是回報不滿足條件的最大值, 脫離while loop, l = r + 1








#左閉右開
import collections
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        li = self.dic[key]
        n = len(li)
        l, r = 0, n
        
        while l < r:
            mid = l + (r-l) // 2
            if timestamp >= li[mid][1]:  #這邊一定要>=, 否則,  timestamp <= li[mid][1] 等於條件落在r,左閉右開規定r是區間外的, 矛盾!!(有可能造成index out of range)
                l = mid + 1
            else:
                r = mid 
        
        return "" if l == 0 else li[l-1][0]  #why l-1, 因為l 已在區間外

# return "" if l == 0, 有兩種情況, 1, timestamp 比 li[0] 小, 2. 還有沒這個key時, l = 0, r = 0 直接return
        

#左閉右閉
import collections
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        li = self.dic[key]
        n = len(li)
        l, r = 0, n-1
        
        while l <= r:
            mid = (l+r) // 2
            if timestamp >= li[mid][1]:  #這邊一定要>=, 否則,  timestamp <= li[mid][1] 等於條件落在r+1, 但r+1 是區間外的, 矛盾!!(有可能造成index out of range)
                l = mid + 1
            else:
                r = mid - 1
        
        return "" if l == 0  else li[r][0]  #why l-1, 因為timestamp >= li[mid][1] => l = mid + 1, 等於成立時, mid = l-1

# return "" if l == 0, 有兩種情況, 1, timestamp 比 li[0] 小, 2. 還有沒這個key時, l = 0, r = -1 直接return






#以下真他媽重要!! 
**左闭右闭：包括End区间，end inclusive**
```
def binarySearch(arr, target):
    '''
    定义：在[l...r]的范围里寻找target, 因为这里定义是需要将r归入范围区间, inclusive，所以while循环的边界需要包含r
    '''
    l , r = 0, len(arr) - 1  
    while l <= r:            

        mid = (l+r)//2
        if arr[mid] == target:
            return mid
        if target > arr[mid]:
            l = mid + 1   # 明确区间的要求，只要使用过的，一律绕过。
        else:
            r = mid - 1   # 明确区间的要求，只要使用过的，一律绕过。
    return -1



**左闭右开，不包括End区间, end exclusive**
```
def binarySearch(arr, target):
    '''
    定义：在[l...r)的范围里寻找target, 因为这里定义是不需要将end归入范围区间
    exclusive，所以while循环的边界小于End即可，因为length本身长度会比index大1
    相对应的，每次target的value小于arr[mid]的时候，我们在重新定义新的end时候，
    也选择exclusive的模式，r = mid即可
    '''
    l , r = 0, len(arr)
    while l < r:            
        mid = l + (r-l)//2
        if arr[mid] == target:
            return mid
        if target > arr[mid]:
            l = mid + 1  
        else:
            r = mid
    return -1
        











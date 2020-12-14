'''
You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
'''


# First get rank, the smallest number will be rank 1, the second smallest will be rank 2...
# With this rank info binary indexed tree can be used to count smaller numbers as we scan from right to left.

# https://www.acwing.com/blog/content/80/

# Binary Indexed Tree Method 樹狀數組
# time complexity: O(nlogn), build a binary index tree O(n), query O(logn), space complecity O(n)
# 思路: 此題經典, 希望要熟練, 最大困難在於如何把nums轉化成num_to_index 數組
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_unique = set(nums) #用set避免重複來防止數組index錯亂, 原序列是可以有重複元素的
        nums_sorted = sorted(nums_unique)  #先進行排序以利之後決定原序列元素放在哪個數組index, sorted(set) => list
        num_to_idx = {num:i + 1 for i,num in enumerate(nums_sorted)}  #dict comprehension, why num:i + 1 方便之後索引因為, bit[0]是不放元素的
        
        bit = [0 for _ in range(len(nums_unique) + 1)]  #樹狀數組索引0不放元素, 初始值都為0
        res = []
        for i in range(len(nums) - 1,- 1,- 1):  #從右數到左
            self.update(bit,num_to_idx[nums[i]]) #num_to_idx 關鍵的一步, 把原序列對應成數組, 原序列大的元素在數組裡index較高, num_to_idx[nums[i]] => 數組index
            res.append(self.query(bit,num_to_idx[nums[i]] - 1)) #此時計算bit index比我小一個的節點的query(總合值=右邊有幾個比我小的元素, 重點在於倒序的操作來模仿原序列右邊有幾個元素)
        
        return res[:: - 1]  #因為是從右到左append, 因此要倒序
    
    def update(self,bit,num):
        while num <= len(bit) - 1: #why len(bit) - 1, 因為 zero based index issue
            bit[num] += 1
            num += self.lowbit(num)
    
    def query(self,bit,num):
        res = 0
        while num > 0:
            res += bit[num]
            num -= self.lowbit(num)
        return res
    
    def lowbit(self,num):
        return num & - num 



#重寫第二次, time complexity O(nlogn), space complexity O(n)
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        temp = sorted(set(nums))
        numsIndex = {v: i + 1 for i, v in enumerate(temp)}
        bits = [0] * (len(numsIndex) + 1)
        res = []
        for i in range(len(nums) - 1, -1, -1):
            idx = numsIndex[nums[i]]
            self.update(bits, idx)
            res.append(self.query(bits, idx - 1))
        return res[::-1]
    
    def update(self, bits, idx):
        while idx <= len(bits) - 1:
            bits[idx] += 1
            idx += (idx & -idx)
            
    def query(self, bits, idx):
        res = 0
        while idx > 0:
            res += bits[idx]
            idx -= (idx & -idx)
        return res














nums: [5,2,6,1] -> sorted(nums): [1,2,5,6]
res: [0,1,1,2]
res[:: - 1]: [2,1,1,0]

nums_sorted = [1,2,5,6]
num_to_idx = {num:i + 1 for i,num in enumerate(nums_sorted)}
num_to_idx
{1: 1, 2: 2, 5: 3, 6: 4}


a = [1,1,2,3,4,4,5]
b = set(a)
b
{1, 2, 3, 4, 5}
b[2]
TypeError: 'set' object is not subscriptable
list(b)
[1, 2, 3, 4, 5]

a = set([2,6,4,5])
sorted(a)
[2, 4, 5, 6]

# Segment Tree
#https://www.youtube.com/watch?v=ZBHKZF5w4YU 影片講的真好
# https://blog.csdn.net/Yaokai_AssultMaster/article/details/79599809 這ppt很重要, 這題看圖就清楚
#filter 是生成器

# Same idea with the segment tree but using an array.
# A little bit explanation:
# In the loop, we simply append result when building the tree.
# Size of tree is relative with the number of distinct values.
# Time O(n*log(n)), space O(n)


# segment tree
class Solution(object):
    def countSmaller(self, nums):
        res = []
        d = {v:i for i,v in enumerate(sorted(set(nums)))}
        L = self.L = len(d)
        tree = self.tree = [0]*(L<<1) #2n, tree[0]是不放元素的, tree[1]包含整段區間
        for i in range(len(nums)-1, -1, -1):
            res.append(self.range_sum(0, d[nums[i]]-1))
            self.update(d[nums[i]], 1)
        return res[::-1]
    
    def update(self, i, val):
        i += self.L
        tree = self.tree
        tree[i] += val
        while i > 1:
            tree[i>>1] = tree[i] + tree[i^1] #左右child i = 偶數 鄰居: 2^1 =3, i = 奇數 鄰居:3^1 = 2
            i >>= 1
        
    def range_sum(self, i, j):
        i += self.L
        j += self.L
        tree = self.tree
        res = 0
        while i <= j:
            if i & 1:  #start是奇數 看網頁圖表就知道為什麼了
                res += tree[i]
                i += 1 
            if j & 1 == 0:  #end 是偶數
                res += tree[j]
                j -= 1 
            i >>= 1
            j >>= 1
        return res


2^1
3
3^1
2



# Binary Search Tree 不難懂! 比較直覺傾向刷題用
# time complexity: build a binary search tree O(n), query O(logn), space complecity O(n)
class BinarySearchTreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1
        self.leftTreeSize = 0


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val, root):
        if not root:
            self.root = BinarySearchTreeNode(val)
            return 0  #目前序列最後一個 右邊沒東西

        if val == root.val:
            root.count += 1  #出現跟root一樣大的值,為了之後右邊有幾個比較小的數計算, root.count+1
            return root.leftTreeSize  #r計算目前比root小的數有幾個

        if val < root.val:
            root.leftTreeSize += 1

            if not root.left:
                root.left = BinarySearchTreeNode(val)
                return 0
            return self.insert(val, root.left) #往左邊樹遍歷並回報有幾個比自身小的數

        if not root.right: # val > root.val case
            root.right = BinarySearchTreeNode(val)
            return root.count + root.leftTreeSize #回報包含root自身的count + 總共有幾個比root小的數

        return root.count + root.leftTreeSize + self.insert(val, root.right)  #回報包含root自身的count + 總共有幾個比root小的數 並往右邊樹遍歷


class Solution(object):
    def countSmaller(self, nums):
        tree = BinarySearchTree()
        return [tree.insert(nums[i], tree.root) for i in range(len(nums) - 1, -1, -1)][::-1]








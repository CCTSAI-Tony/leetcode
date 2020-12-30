### QuickSort, time complexity O(nlogn) if random => O(n), space complexity O(1)                  
import random               
class Solution:             
    def quicksort(self, nums):              
                
        def partition(left, right, pivot_index):                
            pivot = nums[pivot_index]               
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]                 
            store_index = left              
            for i in range(left, right):                
                if nums[i] < pivot:             
                    nums[store_index], nums[i] = nums[i], nums[store_index]             
                    store_index += 1                
            nums[right], nums[store_index] = nums[store_index], nums[right]                 
            return store_index              
                        
        def sort(left, right):              
            if left < right:                    
                pivot_index = random.randint(left, right)                   
                pivot_index = partition(left, right, pivot_index)               
                sort(left, pivot_index-1)               
                sort(pivot_index+1, right)              
                
        return sort(0, len(nums) - 1)               





### QuickSelect leetcode 215                    
import random                   
class Solution:                 
    def findKthLargest(self, nums, k):                  
                    
        def partition(left, right, pivot_index):                    
            pivot = nums[pivot_index]                   
            # 1. move pivot to end                  
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]                     
                                
            # 2. move all smaller elements to the left                  
            store_index = left                  
            for i in range(left, right):                    
                if nums[i] < pivot:                 
                    nums[store_index], nums[i] = nums[i], nums[store_index]                 
                    store_index += 1                    
                    
            # 3. move pivot to its final place                  
            nums[right], nums[store_index] = nums[store_index], nums[right]                     
                                
            return store_index                  
                            
        def select(left, right, k_smallest):                    
            """                 
            Returns the k-th smallest element of list within left..right                    
            """                 
            if left == right:       # If the list contains only one element,                    
                return nums[left]   # return that element                   
                                
            # select a random pivot_index between                   
            pivot_index = random.randint(left, right)                       
                                                
            # find the pivot position in a sorted list                      
            pivot_index = partition(left, right, pivot_index)                   
                                
            # the pivot is in its final sorted position                 
            if k_smallest == pivot_index:                   
                 return nums[k_smallest]                    
            # go left                   
            elif k_smallest < pivot_index:                  
                return select(left, pivot_index - 1, k_smallest)                    
            # go right                  
            else:                   
                return select(pivot_index + 1, right, k_smallest)                   
                    
        # kth largest is (n - k)th smallest index                   
        return select(0, len(nums) - 1, len(nums) - k)                  



歸併排序 time complexity O(nlogn), space complexity O(n)
def merge_sort(q, l, r):
    if l >= r:
        return
    mid = l + (r - l) // 2
    merge_sort(q, l, mid)
    merge_sort(q, mid + 1, r)
    i, j, temp = l, mid + 1, []
    while i <= mid and j <= r:
        if q[i] <= q[j]:
            temp.append(q[i])
            i += 1
        else:
            temp.append(q[j])
            j += 1
    while i <= mid:
        temp.append(q[i])
        i += 1
    while j <= r:
        temp.append(q[j])
        j += 1
    k = 0
    for i in range(l, r + 1):
        q[i] = temp[k]
        k += 1

a = [5,7,2,4,33,9,1,0,7,3,100,77]
l, r = 0, len(a) - 1
merge_sort(a, l, r)
a => [0, 1, 2, 3, 4, 5, 7, 7, 9, 33, 77, 100]



Binary Search | 模板选择, leetcode 34 classic

第二个模板专门针对的是第一个模板的短板：当要access数组边界的数，如果边界在运行中出现更改，可能越界。                               
#基本觀念, 何時使用模板2, 當運行過程or return 要 access 數組區間邊界的數 ex: nums[left], nums[right] 時, 避免越界而使用                             
binary search 模板1,2 最大差別在於是否會越界且要取得越界array值, 若是, 請用模板2                              

模板2缺點, array必須不能是empty, 不然跳出while loop的比較會出現index out of range error                            
                         

@gengwuli 提出了模板一致性的观点，我也十分赞同。公瑾的策略是95%的情况下都用以下模板：       
def binarySearch(arr, target):      
    l , r = 0, len(arr) - 1         
    while l <= r:                   
        mid = (l+r)//2      
        if arr[mid] == target:      
            return mid      
        if target > arr[mid]:       
            l = mid + 1     
        else:       
            r = mid - 1         
    return -1       
        
极个别情况会采用以下的模板：      
def binary_search(array, target):       
    start, end = 0, len(array) - 1      
    while start + 1 < end:      
        mid = (start + end) / 2     
        if array[mid] == target:        
            start = mid     
        elif array[mid] < target:       
            start = mid     
        else:       
            end = mid       
        
    if array[start] == target:      
        return start        
    if array[end] == target:        
        return end      
    return -1       



# 找insert position請用模板1, 用模板2會比較麻煩   

class Solution:     模板1         
    def searchInsert(nums, target):                     
        l, r = 0, len(nums) - 1                     
        while l <= r:                       
            mid = l + (r-l)//2                      
            if target > nums[mid]:   #一定要  >            
                l = mid + 1                     
            else:                       
                r = mid - 1                     
        return l                    



class Solution:     模板2                     
    def searchInsert(nums, target):                             
        l, r = 0, len(nums) - 1                             
        while l + 1 < r:                            
            mid = l + (r-l)//2                              
            if target > nums[mid]:                              
                l = mid                         
            else:                               
                r = mid     
        if target <= nums[l]:       
            return l        
        elif target <= nums[r]:     
            return r                            
        return r + 1        



高精度加法
def add():
    A_str = input()
    B_str = input()
    A, B = [0 for i in range(max(len(A_str), len(B_str)) + 1)], [0 for i in range(max(len(A_str), len(B_str)) + 1)]
    i, j, t = 0, 0, 0
    for k in range(len(A_str) - 1, -1, -1):
        A[i] = int(A_str[k])
        i += 1
    for k in range(len(B_str) - 1, -1, -1):
        B[j] = int(B_str[k])
        j += 1

    C = [0 for i in range(len(A) + 1)]
    for k in range(len(A)):
        if A[k] + B[k] + t >= 10:
            C[k] = (A[k] + B[k] + t) % 10
            t = 1
        else:
            C[k] = A[k] + B[k] + t
            t = 0
    while len(C) > 1 and C[-1] == 0:
        C.pop()

    C.reverse()
    ans = ''.join(map(str,C))

    print(ans)
add()



高精度減法
def cmp(A, B): #判断 if a>=b
    if len(A) != len(B):
        return len(A) > len(B)
    else:
        for i in range(len(A)-1, 0, -1):
            if A[i] != B[i]:
                return A[i] > B[i]
        return True #相等也是true

def sub():
    A = list(map(int, input()))
    B = list(map(int, input()))
    A.reverse()
    B.reverse()   
    if cmp(A, B):
        i, t, C = 0, 0, []
        while i < len(A):
            if i < len(B):
                t = A[i] - B[i] - t
            else:
                t = A[i] - t
            C.append((t + 10) % 10)
            if t >= 0:
                t = 0
            else:
                t = 1
            i += 1
        #把C中的0去掉[0,0,3]        
        while len(C) > 1 and C[-1] == 0:
            C.pop()
        C.reverse()
        
        print("".join(map(str, C)))
    else: # B 比 A大
        return ("-" + sub(B, A))
sub()


高精度乘法 python 加法替代乘法算法
*9435，需要进行 9+4+3+5+4=25 次加法。即循环25次加法函数，时间可以接受。
加法的函数来自于前两题我写的加法函数，但是有两点需要注意一下。
一是传入函数的两个list要固定住，不能在计算过程中被修改。
二是函数式编程中各个函数的变量名要区分开，否则嵌套的时候容易混淆。

def add(A_str, B_str):
    A, B = [0 for i in range(max(len(A_str), len(B_str)) + 1)], [0 for i in range(max(len(A_str), len(B_str)) + 1)]
    i, j, t = 0, 0, 0
    for k in range(len(A_str) - 1, -1, -1):
        A[i] = int(A_str[k])
        i += 1
    for k in range(len(B_str) - 1, -1, -1):
        B[j] = int(B_str[k])
        j += 1

    C = [0 for i in range(len(A) + 1)]
    for k in range(len(A)):
        if A[k] + B[k] + t >= 10:
            C[k] = (A[k] + B[k] + t) % 10
            t = 1
        else:
            C[k] = A[k] + B[k] + t
            t = 0
    while len(C) > 1 and C[-1] == 0:
        C.pop()

    C.reverse()
    return C


def multi():
    m1 = list(input())
    m2 = list(input())
    ans_in_diff_dim = []
    m2.reverse()
    for i in range(len(m2)):
        m3 = []
        for u in range(int(m2[i])):
            m3 = add(m3, m1)
        for k in range(i):
            m3.append(0)
        ans_in_diff_dim.append(m3)
    m4 = []
    for i in range(len(ans_in_diff_dim)):
        m4 = add(m4, ans_in_diff_dim[i])
    print("".join(list(map(str, m4))))

multi()


一维前缀和 —— 模板题 AcWing 795. 前缀和
S[i] = a[0] + a[1] + ... a[i - 1], S[0] = 0
a[l] + ... + a[r] = S[r] - S[l - 1]


二维前缀和 —— 模板题 AcWing 796. 子矩阵的和
S[i, j] = 第i行j列格子左上部分所有元素的和
以(x1, y1)为左上角，(x2, y2)为右下角的子矩阵的和为：
S[x2, y2] - S[x1 - 1, y2] - S[x2, y1 - 1] + S[x1 - 1, y1 - 1]

def matrix_sum(matrix):
    m, n = len(matrix), len(matrix[0])
    for j in range(1, n):
        matrix[0][j] += matrix[0][j - 1]
    for i in range(1, m):
        matrix[i][0] += matrix[i - 1][0]
    for i in range(1, m):
        for j in range(1, n):
            matrix[i][j] += matrix[i][j - 1] + (matrix[i -1][j] - matrix[i - 1][j - 1])
matrix = [[1,2,3,4], [5,6,7,8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix_sum(matrix)
matrix => [[1, 3, 6, 10], [6, 14, 24, 36], [15, 33, 54, 78], [28, 60, 96, 136]]
sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) => 136



#差分用處, 給原數組某區間都加上c 只需花 time complexity O(1)
一维差分 —— 模板题 AcWing 797. 差分, A: 前綴和, B: 差分
给区间[l, r]中的每个数加上c：B[l] += c, B[r + 1] -= c => 使得前綴和A[l, r] 都加上C, 但其他區間不加上

二维差分 —— 模板题 AcWing 798. 差分矩阵
给以(x1, y1)为左上角，(x2, y2)为右下角的子矩阵中的所有元素加上c：
S[x1, y1] += c, S[x2 + 1, y1] -= c, S[x1, y2 + 1] -= c, S[x2 + 1, y2 + 1] += c => S 是差分矩正


位运算 —— 模板题 AcWing 801. 二进制中1的个数
求n的第k位数字: n >> k & 1, 從0開始算
返回n的最后一位1：lowbit(n) = n & -n => 樹狀數組的重要技巧

-x = ~x + 1 => sign integer => 取反補1   => 知識點: 原碼, 反碼, 補碼

def count1bits(n):
    count = 0
    while n:
        n -= (n & -n)
        count += 1
    return count

count1bits(550) => => 4
bin(550) => '0b1000100110'


整數離散 acwing 802
def find(x):
    """二分查找模板，从索引数组alls中找到大于等于x的最小的索引"""
    l = 0
    r = len(alls)-1
    while l <= r:
        mid = l + (r - l) // 2
        if alls[mid] >= x: 
            r = mid - 1   
        else: l = mid+1
    return l+1    # 因为要计算前缀和，所以加1保证索引从1开始

if __name__=="__main__":
    n, m = map(int, input().split())
    N = 300010
    a = [0]*N    # 用于存储离散化后的索引和对应值，其中索引对应离散化后的索引，值对应离散化前索引的取值
    s = [0]*N    # 存a数组的前缀和数组

    add = []    # 存储插入操作的二元组
    query = []    # 存储查询操作的二元组

    alls = []    # 存储离散化前输入的所有索引，n+2*m

    for i in range(n):
        x, c = map(int, input().split())
        add.append((x, c))
        alls.append(x)

    for i in range(m):
        l, r = map(int, input().split())
        query.append((l, r))
        alls.append(l)
        alls.append(r)
    
    alls = sorted(set(alls)) # 将alls数组排序并去重


    # 1. 处理插入
    for x, c in add:
        x2 = find(x)
        a[x2]+=c

    # 2. 处理前缀和
    for i in range(1, len(alls)+1):
        s[i] = s[i-1] + a[i]

    # 3. 处理查询
    for l, r in query:
        l2 = find(l)
        r2 = find(r)
        res = s[r2]-s[l2-1]
        print(res)























        
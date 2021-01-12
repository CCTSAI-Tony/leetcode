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



#c++

单链表 —— 模板题 AcWing 826. 单链表
// head存储链表头，e[]存储节点的值，ne[]存储节点的next指针，idx表示当前用到了哪个节点
int head, e[N], ne[N], idx;

// 初始化
void init()
{
    head = -1;
    idx = 0;
}

// 在链表头插入一个数a
void insert(int a)
{
    e[idx] = a, ne[idx] = head, head = idx ++ ;
}

// 将头结点删除，需要保证头结点存在
void remove()
{
    head = ne[head];
}


双链表 —— 模板题 AcWing 827. 双链表
// e[]表示节点的值，l[]表示节点的左指针，r[]表示节点的右指针，idx表示当前用到了哪个节点
int e[N], l[N], r[N], idx;

// 初始化
void init()
{
    //0是左端点，1是右端点
    r[0] = 1, l[1] = 0;
    idx = 2;
}

// 在节点a的右边插入一个数x
void insert(int a, int x)
{
    e[idx] = x;
    l[idx] = a, r[idx] = r[a];
    l[r[a]] = idx, r[a] = idx ++ ;
}

// 删除节点a
void remove(int a)
{
    l[r[a]] = l[a];
    r[l[a]] = r[a];
}

KMP —— 模板题 AcWing 831. KMP字符串
// s[]是长文本，p[]是模式串，n是s的长度，m是p的长度
求模式串的Next数组：
for (int i = 2, j = 0; i <= m; i ++ )
{
    while (j && p[i] != p[j + 1]) j = ne[j];
    if (p[i] == p[j + 1]) j ++ ;
    ne[i] = j;
}

// 匹配
for (int i = 1, j = 0; i <= n; i ++ )
{
    while (j && s[i] != p[j + 1]) j = ne[j];
    if (s[i] == p[j + 1]) j ++ ;
    if (j == m)
    {
        j = ne[j];
        // 匹配成功后的逻辑
    }
}


Trie树 —— 模板题 AcWing 835. Trie字符串统计
int son[N][26], cnt[N], idx;
// 0号点既是根节点，又是空节点
// son[][]存储树中每个节点的子节点
// cnt[]存储以每个节点结尾的单词数量

// 插入一个字符串
void insert(char *str)
{
    int p = 0;
    for (int i = 0; str[i]; i ++ )
    {
        int u = str[i] - 'a';
        if (!son[p][u]) son[p][u] = ++ idx;
        p = son[p][u];
    }
    cnt[p] ++ ;
}

// 查询字符串出现的次数
int query(char *str)
{
    int p = 0;
    for (int i = 0; str[i]; i ++ )
    {
        int u = str[i] - 'a';
        if (!son[p][u]) return 0;
        p = son[p][u];
    }
    return cnt[p];
}



1)朴素并查集：

    int p[N]; //存储每个点的祖宗节点

    // 返回x的祖宗节点
    int find(int x)
    {
        if (p[x] != x) p[x] = find(p[x]);
        return p[x];
    }

    // 初始化，假定节点编号是1~n
    for (int i = 1; i <= n; i ++ ) p[i] = i;

    // 合并a和b所在的两个集合：
    p[find(a)] = find(b);


(2)维护size的并查集：

    int p[N], size[N];
    //p[]存储每个点的祖宗节点, size[]只有祖宗节点的有意义，表示祖宗节点所在集合中的点的数量

    // 返回x的祖宗节点
    int find(int x)
    {
        if (p[x] != x) p[x] = find(p[x]);
        return p[x];
    }

    // 初始化，假定节点编号是1~n
    for (int i = 1; i <= n; i ++ )
    {
        p[i] = i;
        size[i] = 1;
    }

    // 合并a和b所在的两个集合：
    size[find(b)] += size[find(a)];
    p[find(a)] = find(b);


(3)维护到祖宗节点距离的并查集：

    int p[N], d[N];
    //p[]存储每个点的祖宗节点, d[x]存储x到p[x]的距离

    // 返回x的祖宗节点
    int find(int x)
    {
        if (p[x] != x)
        {
            int u = find(p[x]);
            d[x] += d[p[x]];
            p[x] = u;
        }
        return p[x];
    }

    // 初始化，假定节点编号是1~n
    for (int i = 1; i <= n; i ++ )
    {
        p[i] = i;
        d[i] = 0;
    }

    // 合并a和b所在的两个集合：
    p[find(a)] = find(b);
    d[find(a)] = distance; // 根据具体问题，初始化find(a)的偏移量



堆 —— 模板题 AcWing 838. 堆排序, AcWing 839. 模拟堆
// h[N]存储堆中的值, h[1]是堆顶，x的左儿子是2x, 右儿子是2x + 1
// ph[k]存储第k个插入的点在堆中的位置
// hp[k]存储堆中下标是k的点是第几个插入的
int h[N], ph[N], hp[N], size;

// 交换两个点，及其映射关系
void heap_swap(int a, int b)
{
    swap(ph[hp[a]],ph[hp[b]]);
    swap(hp[a], hp[b]);
    swap(h[a], h[b]);
}

void down(int u)
{
    int t = u;
    if (u * 2 <= size && h[u * 2] < h[t]) t = u * 2;
    if (u * 2 + 1 <= size && h[u * 2 + 1] < h[t]) t = u * 2 + 1;
    if (u != t)
    {
        heap_swap(u, t);
        down(t);
    }
}

void up(int u)
{
    while (u / 2 && h[u] < h[u / 2])
    {
        heap_swap(u, u / 2);
        u >>= 1;
    }
}

// O(n)建堆
for (int i = n / 2; i; i -- ) down(i);



一般哈希 —— 模板题 AcWing 840. 模拟散列表
(1) 拉链法
    int h[N], e[N], ne[N], idx;

    // 向哈希表中插入一个数
    void insert(int x)
    {
        int k = (x % N + N) % N;
        e[idx] = x;
        ne[idx] = h[k];
        h[k] = idx ++ ;
    }

    // 在哈希表中查询某个数是否存在
    bool find(int x)
    {
        int k = (x % N + N) % N;
        for (int i = h[k]; i != -1; i = ne[i])
            if (e[i] == x)
                return true;

        return false;
    }

(2) 开放寻址法
    int h[N];

    // 如果x在哈希表中，返回x的下标；如果x不在哈希表中，返回x应该插入的位置
    int find(int x)
    {
        int t = (x % N + N) % N;
        while (h[t] != null && h[t] != x)
        {
            t ++ ;
            if (t == N) t = 0;
        }
        return t;
    }


字符串哈希 —— 模板题 AcWing 841. 字符串哈希
核心思想：将字符串看成P进制数，P的经验值是131或13331，取这两个值的冲突概率低
小技巧：取模的数用2^64，这样直接用unsigned long long存储，溢出的结果就是取模的结果

typedef unsigned long long ULL;
ULL h[N], p[N]; // h[k]存储字符串前k个字母的哈希值, p[k]存储 P^k mod 2^64

// 初始化
p[0] = 1;
for (int i = 1; i <= n; i ++ )
{
    h[i] = h[i - 1] * P + str[i];
    p[i] = p[i - 1] * P;
}

// 计算子串 str[l ~ r] 的哈希值
ULL get(int l, int r)
{
    return h[r] - h[l - 1] * p[r - l + 1];
}



C++ STL简介
vector, 变长数组，倍增的思想
    size()  返回元素个数
    empty()  返回是否为空
    clear()  清空
    front()/back()
    push_back()/pop_back()
    begin()/end()
    []
    支持比较运算，按字典序

pair<int, int>
    first, 第一个元素
    second, 第二个元素
    支持比较运算，以first为第一关键字，以second为第二关键字（字典序）

string，字符串
    size()/length()  返回字符串长度
    empty()
    clear()
    substr(起始下标，(子串长度))  返回子串
    c_str()  返回字符串所在字符数组的起始地址

queue, 队列
    size()
    empty()
    push()  向队尾插入一个元素
    front()  返回队头元素
    back()  返回队尾元素
    pop()  弹出队头元素

priority_queue, 优先队列，默认是大根堆
    size()
    empty()
    push()  插入一个元素
    top()  返回堆顶元素
    pop()  弹出堆顶元素
    定义成小根堆的方式：priority_queue<int, vector<int>, greater<int>> q;

stack, 栈
    size()
    empty()
    push()  向栈顶插入一个元素
    top()  返回栈顶元素
    pop()  弹出栈顶元素

deque, 双端队列
    size()
    empty()
    clear()
    front()/back()
    push_back()/pop_back()
    push_front()/pop_front()
    begin()/end()
    []

set, map, multiset, multimap, 基于平衡二叉树（红黑树），动态维护有序序列
    size()
    empty()
    clear()
    begin()/end()
    ++, -- 返回前驱和后继，时间复杂度 O(logn)

    set/multiset
        insert()  插入一个数
        find()  查找一个数
        count()  返回某一个数的个数
        erase()
            (1) 输入是一个数x，删除所有x   O(k + logn)
            (2) 输入一个迭代器，删除这个迭代器
        lower_bound()/upper_bound()
            lower_bound(x)  返回大于等于x的最小的数的迭代器
            upper_bound(x)  返回大于x的最小的数的迭代器
    map/multimap
        insert()  插入的数是一个pair
        erase()  输入的参数是pair或者迭代器
        find()
        []  注意multimap不支持此操作。 时间复杂度是 O(logn)
        lower_bound()/upper_bound()

unordered_set, unordered_map, unordered_multiset, unordered_multimap, 哈希表
    和上面类似，增删改查的时间复杂度是 O(1)
    不支持 lower_bound()/upper_bound()， 迭代器的++，--

bitset, 圧位
    bitset<10000> s;
    ~, &, |, ^
    >>, <<
    ==, !=
    []

    count()  返回有多少个1

    any()  判断是否至少有一个1
    none()  判断是否全为0

    set()  把所有位置成1
    set(k, v)  将第k位变成v
    reset()  把所有位变成0
    flip()  等价于~
    flip(k) 把第k位取反



树与图的存储
树是一种特殊的图，与图的存储方式相同。
对于无向图中的边ab，存储两条有向边a->b, b->a。
因此我们可以只考虑有向图的存储。

(1) 邻接矩阵：g[a][b] 存储边a->b

(2) 邻接表：

// 对于每个点k，开一个单链表，存储k所有可以走到的点。h[k]存储这个单链表的头结点
int h[N], e[N], ne[N], idx;

// 添加一条边a->b
void add(int a, int b)
{
    e[idx] = b, ne[idx] = h[a], h[a] = idx ++ ;
}

// 初始化
idx = 0;
memset(h, -1, sizeof h);
树与图的遍历
时间复杂度 O(n+m)O(n+m), nn 表示点数，mm 表示边数
(1) 深度优先遍历 —— 模板题 AcWing 846. 树的重心

int dfs(int u)
{
    st[u] = true; // st[u] 表示点u已经被遍历过

    for (int i = h[u]; i != -1; i = ne[i])
    {
        int j = e[i];
        if (!st[j]) dfs(j);
    }
}
(2) 宽度优先遍历 —— 模板题 AcWing 847. 图中点的层次

queue<int> q;
st[1] = true; // 表示1号点已经被遍历过
q.push(1);

while (q.size())
{
    int t = q.front();
    q.pop();

    for (int i = h[t]; i != -1; i = ne[i])
    {
        int j = e[i];
        if (!st[j])
        {
            st[j] = true; // 表示点j已经被遍历过
            q.push(j);
        }
    }
}
拓扑排序 —— 模板题 AcWing 848. 有向图的拓扑序列
时间复杂度 O(n+m)O(n+m), nn 表示点数，mm 表示边数
bool topsort()
{
    int hh = 0, tt = -1;

    // d[i] 存储点i的入度
    for (int i = 1; i <= n; i ++ )
        if (!d[i])
            q[ ++ tt] = i;

    while (hh <= tt)
    {
        int t = q[hh ++ ];

        for (int i = h[t]; i != -1; i = ne[i])
        {
            int j = e[i];
            if (-- d[j] == 0)
                q[ ++ tt] = j;
        }
    }

    // 如果所有点都入队了，说明存在拓扑序列；否则不存在拓扑序列。
    return tt == n - 1;
}
朴素dijkstra算法 —— 模板题 AcWing 849. Dijkstra求最短路 I
时间复杂是 O(n2+m)O(n2+m), nn 表示点数，mm 表示边数
int g[N][N];  // 存储每条边
int dist[N];  // 存储1号点到每个点的最短距离
bool st[N];   // 存储每个点的最短路是否已经确定

// 求1号点到n号点的最短路，如果不存在则返回-1
int dijkstra()
{
    memset(dist, 0x3f, sizeof dist);
    dist[1] = 0;

    for (int i = 0; i < n - 1; i ++ )
    {
        int t = -1;     // 在还未确定最短路的点中，寻找距离最小的点
        for (int j = 1; j <= n; j ++ )
            if (!st[j] && (t == -1 || dist[t] > dist[j]))
                t = j;

        // 用t更新其他点的距离
        for (int j = 1; j <= n; j ++ )
            dist[j] = min(dist[j], dist[t] + g[t][j]);

        st[t] = true;
    }

    if (dist[n] == 0x3f3f3f3f) return -1;
    return dist[n];
}
堆优化版dijkstra —— 模板题 AcWing 850. Dijkstra求最短路 II
时间复杂度 O(mlogn)O(mlogn), nn 表示点数，mm 表示边数
typedef pair<int, int> PII;

int n;      // 点的数量
int h[N], w[N], e[N], ne[N], idx;       // 邻接表存储所有边
int dist[N];        // 存储所有点到1号点的距离
bool st[N];     // 存储每个点的最短距离是否已确定

// 求1号点到n号点的最短距离，如果不存在，则返回-1
int dijkstra()
{
    memset(dist, 0x3f, sizeof dist);
    dist[1] = 0;
    priority_queue<PII, vector<PII>, greater<PII>> heap;
    heap.push({0, 1});      // first存储距离，second存储节点编号

    while (heap.size())
    {
        auto t = heap.top();
        heap.pop();

        int ver = t.second, distance = t.first;

        if (st[ver]) continue;
        st[ver] = true;

        for (int i = h[ver]; i != -1; i = ne[i])
        {
            int j = e[i];
            if (dist[j] > distance + w[i])
            {
                dist[j] = distance + w[i];
                heap.push({dist[j], j});
            }
        }
    }

    if (dist[n] == 0x3f3f3f3f) return -1;
    return dist[n];
}
Bellman-Ford算法 —— 模板题 AcWing 853. 有边数限制的最短路
时间复杂度 O(nm)O(nm), nn 表示点数，mm 表示边数
注意在模板题中需要对下面的模板稍作修改，加上备份数组，详情见模板题。

int n, m;       // n表示点数，m表示边数
int dist[N];        // dist[x]存储1到x的最短路距离

struct Edge     // 边，a表示出点，b表示入点，w表示边的权重
{
    int a, b, w;
}edges[M];

// 求1到n的最短路距离，如果无法从1走到n，则返回-1。
int bellman_ford()
{
    memset(dist, 0x3f, sizeof dist);
    dist[1] = 0;

    // 如果第n次迭代仍然会松弛三角不等式，就说明存在一条长度是n+1的最短路径，由抽屉原理，路径中至少存在两个相同的点，说明图中存在负权回路。
    for (int i = 0; i < n; i ++ )
    {
        for (int j = 0; j < m; j ++ )
        {
            int a = edges[j].a, b = edges[j].b, w = edges[j].w;
            if (dist[b] > dist[a] + w)
                dist[b] = dist[a] + w;
        }
    }

    if (dist[n] > 0x3f3f3f3f / 2) return -1;
    return dist[n];
}
spfa 算法（队列优化的Bellman-Ford算法） —— 模板题 AcWing 851. spfa求最短路
时间复杂度 平均情况下 O(m)O(m)，最坏情况下 O(nm)O(nm), nn 表示点数，mm 表示边数
int n;      // 总点数
int h[N], w[N], e[N], ne[N], idx;       // 邻接表存储所有边
int dist[N];        // 存储每个点到1号点的最短距离
bool st[N];     // 存储每个点是否在队列中

// 求1号点到n号点的最短路距离，如果从1号点无法走到n号点则返回-1
int spfa()
{
    memset(dist, 0x3f, sizeof dist);
    dist[1] = 0;

    queue<int> q;
    q.push(1);
    st[1] = true;

    while (q.size())
    {
        auto t = q.front();
        q.pop();

        st[t] = false;

        for (int i = h[t]; i != -1; i = ne[i])
        {
            int j = e[i];
            if (dist[j] > dist[t] + w[i])
            {
                dist[j] = dist[t] + w[i];
                if (!st[j])     // 如果队列中已存在j，则不需要将j重复插入
                {
                    q.push(j);
                    st[j] = true;
                }
            }
        }
    }

    if (dist[n] == 0x3f3f3f3f) return -1;
    return dist[n];
}
spfa判断图中是否存在负环 —— 模板题 AcWing 852. spfa判断负环
时间复杂度是 O(nm)O(nm), nn 表示点数，mm 表示边数
int n;      // 总点数
int h[N], w[N], e[N], ne[N], idx;       // 邻接表存储所有边
int dist[N], cnt[N];        // dist[x]存储1号点到x的最短距离，cnt[x]存储1到x的最短路中经过的点数
bool st[N];     // 存储每个点是否在队列中

// 如果存在负环，则返回true，否则返回false。
bool spfa()
{
    // 不需要初始化dist数组
    // 原理：如果某条最短路径上有n个点（除了自己），那么加上自己之后一共有n+1个点，由抽屉原理一定有两个点相同，所以存在环。

    queue<int> q;
    for (int i = 1; i <= n; i ++ )
    {
        q.push(i);
        st[i] = true;
    }

    while (q.size())
    {
        auto t = q.front();
        q.pop();

        st[t] = false;

        for (int i = h[t]; i != -1; i = ne[i])
        {
            int j = e[i];
            if (dist[j] > dist[t] + w[i])
            {
                dist[j] = dist[t] + w[i];
                cnt[j] = cnt[t] + 1;
                if (cnt[j] >= n) return true;       // 如果从1号点到x的最短路中包含至少n个点（不包括自己），则说明存在环
                if (!st[j])
                {
                    q.push(j);
                    st[j] = true;
                }
            }
        }
    }

    return false;
}
floyd算法 —— 模板题 AcWing 854. Floyd求最短路
时间复杂度是 O(n3)O(n3), nn 表示点数
初始化：
    for (int i = 1; i <= n; i ++ )
        for (int j = 1; j <= n; j ++ )
            if (i == j) d[i][j] = 0;
            else d[i][j] = INF;

// 算法结束后，d[a][b]表示a到b的最短距离
void floyd()
{
    for (int k = 1; k <= n; k ++ )
        for (int i = 1; i <= n; i ++ )
            for (int j = 1; j <= n; j ++ )
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
}
朴素版prim算法 —— 模板题 AcWing 858. Prim算法求最小生成树
时间复杂度是 O(n2+m)O(n2+m), nn 表示点数，mm 表示边数
int n;      // n表示点数
int g[N][N];        // 邻接矩阵，存储所有边
int dist[N];        // 存储其他点到当前最小生成树的距离
bool st[N];     // 存储每个点是否已经在生成树中


// 如果图不连通，则返回INF(值是0x3f3f3f3f), 否则返回最小生成树的树边权重之和
int prim()
{
    memset(dist, 0x3f, sizeof dist);

    int res = 0;
    for (int i = 0; i < n; i ++ )
    {
        int t = -1;
        for (int j = 1; j <= n; j ++ )
            if (!st[j] && (t == -1 || dist[t] > dist[j]))
                t = j;

        if (i && dist[t] == INF) return INF;

        if (i) res += dist[t];
        st[t] = true;

        for (int j = 1; j <= n; j ++ ) dist[j] = min(dist[j], g[t][j]);
    }

    return res;
}
Kruskal算法 —— 模板题 AcWing 859. Kruskal算法求最小生成树
时间复杂度是 O(mlogm)O(mlogm), nn 表示点数，mm 表示边数
int n, m;       // n是点数，m是边数
int p[N];       // 并查集的父节点数组

struct Edge     // 存储边
{
    int a, b, w;

    bool operator< (const Edge &W)const
    {
        return w < W.w;
    }
}edges[M];

int find(int x)     // 并查集核心操作
{
    if (p[x] != x) p[x] = find(p[x]);
    return p[x];
}

int kruskal()
{
    sort(edges, edges + m);

    for (int i = 1; i <= n; i ++ ) p[i] = i;    // 初始化并查集

    int res = 0, cnt = 0;
    for (int i = 0; i < m; i ++ )
    {
        int a = edges[i].a, b = edges[i].b, w = edges[i].w;

        a = find(a), b = find(b);
        if (a != b)     // 如果两个连通块不连通，则将这两个连通块合并
        {
            p[a] = b;
            res += w;
            cnt ++ ;
        }
    }

    if (cnt < n - 1) return INF;
    return res;
}
染色法判别二分图 —— 模板题 AcWing 860. 染色法判定二分图
时间复杂度是 O(n+m)O(n+m), nn 表示点数，mm 表示边数
int n;      // n表示点数
int h[N], e[M], ne[M], idx;     // 邻接表存储图
int color[N];       // 表示每个点的颜色，-1表示未染色，0表示白色，1表示黑色

// 参数：u表示当前节点，c表示当前点的颜色
bool dfs(int u, int c)
{
    color[u] = c;
    for (int i = h[u]; i != -1; i = ne[i])
    {
        int j = e[i];
        if (color[j] == -1)
        {
            if (!dfs(j, !c)) return false;
        }
        else if (color[j] == c) return false;
    }

    return true;
}

bool check()
{
    memset(color, -1, sizeof color);
    bool flag = true;
    for (int i = 1; i <= n; i ++ )
        if (color[i] == -1)
            if (!dfs(i, 0))
            {
                flag = false;
                break;
            }
    return flag;
}
匈牙利算法 —— 模板题 AcWing 861. 二分图的最大匹配
时间复杂度是 O(nm)O(nm), nn 表示点数，mm 表示边数
int n1, n2;     // n1表示第一个集合中的点数，n2表示第二个集合中的点数
int h[N], e[M], ne[M], idx;     // 邻接表存储所有边，匈牙利算法中只会用到从第一个集合指向第二个集合的边，所以这里只用存一个方向的边
int match[N];       // 存储第二个集合中的每个点当前匹配的第一个集合中的点是哪个
bool st[N];     // 表示第二个集合中的每个点是否已经被遍历过

bool find(int x)
{
    for (int i = h[x]; i != -1; i = ne[i])
    {
        int j = e[i];
        if (!st[j])
        {
            st[j] = true;
            if (match[j] == 0 || find(match[j]))
            {
                match[j] = x;
                return true;
            }
        }
    }

    return false;
}

// 求最大匹配数，依次枚举第一个集合中的每个点能否匹配第二个集合中的点
int res = 0;
for (int i = 1; i <= n1; i ++ )
{
    memset(st, false, sizeof st);
    if (find(i)) res ++ ;
}
















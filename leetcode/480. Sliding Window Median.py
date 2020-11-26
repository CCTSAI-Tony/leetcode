'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position. 
Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
Answers within 10^-5 of the actual value will be accepted as correct.
'''

# To calculate the median, we can maintain divide array into subarray equally: small and large. All elements in small are no larger than any element in large. 
# So median would be (largest in small + smallest in large) / 2 if small's size = large's size. If large's size = small's size + 1, median is smallest in large.

# Thus, we can use heap here to maintain small(max heap) and large(min heap) so we can fetch smallest and largest element in logarithmic time.

# We can also maintain "large's size - small's size <= 1" and "smallest in large >= largest in small" by heap's property: once large's size - small's size > 1, 
# we pop one element from large and add it to small. And vice versa when small's size > large's size.

# Besides, since its a sliding window median, we need to keep track of window ends. So we will also push element's index to the heap. 
# So each element takes a form of (val, index). Since Python's heapq is a min heap, so we convert small to a max heap by pushing (-val, index).

# Intially for first k elements, we push them all into small and then pop k/2 element from small and add them to large.
# Then we can intialize our answer array as [large[0][0] if k & 1 else (large[0][0]-small[0][0])/2] as we discussed above.

# Then for rest iterations, each time we add a new element x whose index is i+k, and remove an old element nums[i] which is out of window scope. 
# Then we calculate our median in current window as the same way before.
# If right end's x is no smaller than large[0], then it belongs to large heap. If left end's nums[i] is no larger than large[0], then it belongs to small heap. 
# So we will add one to large while remove one from small and heaps' sizes will be unbalanced. So we will move large[0] to small to rebalance two heaps.
# Vice versa when we have to add one to small while remove one from large.

# But we don't have to hurry and remove element in each iteration. As long as nums[i] is neither small[0] nor large[0], it has no effect to median calculation. 
# So we wait later and use a while loop to remove those out-of-window small[0] or large[0] at one time. This also make whole logic clearer.

# Since we are using k-size heap here, the time complexity is O(nlogk) and space complexity is O(k).

#刷題用這個, time complexity O(nlogk) and space complexity is O(k)
#思路: 利用small, large heap 來算出該window 的median, 若k是奇數=> median = large[0], 若k是偶數=> median = (small[0]+large[0]) / 2
#初始先push k個元素至small, 再pop k - (k/2) 至 large
#當window移動時, check 右邊新元素是否小於large[0], 若是代表屬於small, 同時check 左邊out window 的nums[i], 看是否>=large[0], 若是代表small將比large多一個, 從small pop 一個給large
#當window移動時, check 右邊新元素是否>=large[0], 若是代表屬於large, 同時check 左邊out window 的nums[i], 看是否<=large[0], 若是代表small將比large少一個, 從large pop 一個給small
#若左邊nums[i] 跟新元素在同一個陣營, 則small 與 large的平衡依舊保持, 若nums[i] 不是small[0] 也不是 large[0] 則不用急著刪除, 因為不影響median 計算且沒破壞平衡, 
#可以想像成這些nums[i] 只是幽靈, 早已不見, 除非nums[i] = small[0] or large[0] => 利用while loop 一次刪除
#注意: heap push 的元素 為 (x, i), small 要用 maxheap
#同value, 但 index 較小的會被排在前面
import heapq
class Solution:
    def medianSlidingWindow(nums, k):
        small, large = [], []
        for i, x in enumerate(nums[:k]):  #起始前k個元素push to small
            heapq.heappush(small, (-x,i))
        for _ in range(k-(k>>1)): #分出一半給large, 若k是奇數, large 會比small 多 1
            self.move(small, large)
        ans = [self.get_med(small, large, k)] #初始window median
        for i, x in enumerate(nums[k:]):
            if x >= large[0][0]: #x屬於large
                heapq.heappush(large, (x, i+k))
                if nums[i] <= large[0][0]: #代表nums[i]屬於small => 此時small會少一個, large多一個 => 從large pop一個去填補small
                    self.move(large, small)
            else: #x屬於small
                heapq.heappush(small, (-x, i+k)) 
                if nums[i] >= large[0][0]: #代表nums[i]屬於large => large會少一個, small多一個 => 從small pop一個去填補large
                    self.move(small, large)
            while small and small[0][1] <= i: #若nums[i] 不是 small[0] nor large[0],不用急著刪除, 等到它變small[0] nor large[0] 再用while loop 一次刪
                heapq.heappop(small)
            while large and large[0][1] <= i: 
                heapq.heappop(large)
            ans.append(self.get_med(small, large, k))
        return ans

    def move(self, h1, h2):
        x, i = heapq.heappop(h1)
        heapq.heappush(h2, (-x, i))
        
    def get_med(self, h1, h2, k):  # if k & 1  確認k是否為奇數
        return h2[0][0] * 1 if k & 1 else (h2[0][0]-h1[0][0]) / 2


#自己重寫, time complexity O(nlogk) and space complexity is O(k)
import heapq
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small, large = [], []
        for i, x in enumerate(nums[:k]):
            heapq.heappush(small, (-x, i))
        for _ in range(k-(k//2)):
            self.move(small, large)
        ans = [self.get_med(small, large, k)]
        for i, x in enumerate(nums[k:]):
            if x >= large[0][0]:
                heapq.heappush(large, (x, i+k))
                if nums[i] <= large[0][0]: #這邊一定要 <=, 因為nums[i] 在small 有可能 = large[0][0] => -small[0][0] == large[0][0], ex: [1,1,1,1] k=2
                    self.move(large, small)
            else:
                heapq.heappush(small, (-x, i+k))
                if nums[i] >= large[0][0]:
                    self.move(small, large)
            while small and small[0][1] <= i: #k= 1, small 有可能會變空
                heapq.heappop(small)
            while large[0][1] <= i:
                heapq.heappop(large)
            ans.append(self.get_med(small, large, k))
        return ans
                    
                
    def move(self, a, b):
        x, i = heapq.heappop(a)
        heapq.heappush(b, (-x, i))
        
    def get_med(self, small, large, k):
        return large[0][0] if k & 1 else (large[0][0] - small[0][0]) / 2







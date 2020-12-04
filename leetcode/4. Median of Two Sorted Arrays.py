# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# Follow up: The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# Example 3:

# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
# Example 4:

# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
# Example 5:

# Input: nums1 = [2], nums2 = []
# Output: 2.00000
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106


@@

# https://www.youtube.com/watch?v=LPFhl65R7ww 影片強烈建議看, 真的幫助很多

# 思路： 利用兩指針i,j 來對nums1, nums2 切割, 若找到nums1[:i] and nums2[:j] 皆小於 nums1[i:] and nums2[j:], 則看整體nums1 + nums2 是奇數還是偶數
# 若是奇數, 左邊最大值就是中位數, 若是偶數 (左邊最大值+ 右邊最小值) / 2 就是中問數, 這邊不能//2 因為答案要float
# 因為i+j = half_len 這個關係, 可以移動i指針順便移動j指針, 因此對較小序列做binary search 找尋最佳i指針位置是整題重點!!
# combined partition: (m + n + 1)//2 此公式特指左邊partition, 若m+n 是odd, left side partition 會比右邊partition 多一個, 這樣安排是故意的
# 因此若整體是奇數的狀況下 median 會放在left partition, 針對比較短的序列做binary search, 因此 time complexity O(log min(m,n))
# time complexity O(log min(m,n))
# 重要constraint: 0 <= m <= 1000, 0 <= n <= 1000, 1 <= m + n <= 2000
# 只有這題強烈建議用模板1, binary search 的部分

class Solution:
    def median(A, B):
        m, n = len(nums1), len(nums2)
        if m > n:  #預設m 是較小的序列, 這樣之後code可以針對nums1 是空序列做check
            nums1, nums2, m, n = nums2, nums1, n, m
        
        imin, imax, half_len = 0, m, (m + n + 1) // 2   #imin = 0, 代表 nums1 沒有一個元素在左邊, imin = m, 代表 nums1 全部元素在左邊
        while imin <= imax:  # 左閉右閉
            i = (imin + imax) // 2 # 這裡的i 指的是 [:i] => nums1, 所以imax可以是m
            j = half_len - i  # 這裡的j 指的是 [:j] => nums2, 因為i+j = half_len 這個關係, 可以移動i指針順便移動j指針
            if i < m and nums2[j-1] > nums1[i]:  # i < m, nums1[i] index not out of range
                # i is too small, must increase it
                imin = i + 1 #二分法
            elif i > 0 and nums1[i-1] > nums2[j]: # 0 < i, nums1[i-1] index not out of range
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect or i = 0 or i = m

                if i == 0: 
                    max_of_left = nums2[j-1]  #max_left_m == None, 所以直接為 max_left_n
                elif j == 0: 
                    max_of_left = nums1[i-1]  #max_left_n == None, 所以直接為 max_left_m
                else: 
                    max_of_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:  #整體是奇數的狀況,左邊多一個元素就是median
                    return max_of_left
                #考慮整體是偶數所以要算min_of_right
                if i == m: 
                    min_of_right = nums2[j]  #min_right_m == None, 所以直接為 min_right_n
                elif j == n: 
                    min_of_right = nums1[i]  ##min_right_n == None, 所以直接為 min_right_m
                else: 
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2  #整體是偶數的狀況下


# found:
#     max_left_m <= min_right_n
#     max_left_n <= min_right_m
# else if:
#     max_left_m > min_right_n
#     move towards left in m
# else if: 
#     max_left_n > min_right_m
#     move towards right in m

[]
[1]



#自己重寫, time complexity O(log min(m,n)), 這題用左閉右閉才比較順, 應該說只能用左閉右閉
#這個code可以解決這個例子, nums1 = [], nums2 = [1], 自己推導一下不難, 就知道為什麼要用模板1了
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        half_len = (m + n + 1) // 2
        imin, imax = 0, m
        while imin <= imax:  #左閉右閉, 模板1
            i = (imin + imax)//2
            j = half_len - i
            if i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            elif i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            else:
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])
                
                if (m + n) % 2 != 0:  #這行一定要先放這裡, 不然若m+n == odd, 下面代碼有可能 index out of range, ex: nums1 = [1], nums2 = [2, 3]
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right) / 2


#重寫第二次, time complexity O(log(min(m,n))) space complexity O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        half_len = (m+n+1)//2
        imin, imax = 0, m
        while imin <= imax:
            i = (imin+imax) // 2
            j = half_len - i
            if i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            elif i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            else:
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])
                if (m + n) % 2:
                    return max_of_left
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right) / 2

#重寫第三次, time complexity O(log(min(m, n))), space complexity O(1)
#指針只針對nums1 做check boundary
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2
        imin, imax = 0, m
        while imin <= imax:
            i = (imin + imax) // 2
            j = half - i
            if i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            elif i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            else:
                if i == 0:
                    max_left = nums2[j-1]
                elif j == 0:
                    max_left = nums1[i-1]
                else:
                    max_left = max(nums1[i-1], nums2[j-1])
                if (m + n) % 2:
                    return max_left
                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])
                return (max_left + min_right) / 2









































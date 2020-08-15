'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent,
 with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

'''
#3 way partition, time complexity O(n), 自己重寫, 刷題用這個
#思路: pivot 就是中間值, 分成 比pivot小, pivot, 比pivot大 三塊
#m1指針代表第一個與pivot 大小相同的元素index, m2指針代表第一個比pivot大的元素index, 自己推算就知道了, [0,1,0,2,0,1,2]
#以這樣的思維就能分成三堆
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m1, m2 = 0, 0
        pivot = 1
        for i in range(len(nums)):
            if nums[i] == pivot:
                nums[i], nums[m2] = nums[m2], nums[i]
                m2 += 1
            
            elif nums[i] < pivot:
                nums[i], nums[m2] = nums[m2], nums[i]
                nums[m2], nums[m1] = nums[m1], nums[m2]
                m1 += 1
                m2 += 1


#  3 pointers, 自己演練就清楚
#  Complexity: Time complexity is O(n), because each moment of time we move at least one of the pointers. Additional space complexity is O(1)
#  思路: 利用三指針的方式來分別擺放0,1,2 => 利用cur指針遍歷元素, 0擺左邊, 2擺右邊, 交換完左右指針往內縮, cur指針依情況往右移動, 一但超過右指針代表遍歷結束
#  因為右指針以右的地方元素都已決定好了, 左指針往右移動cur指針也要一起往右移動, 因為與左指針交換回來的只有可能是1, 還有一個可能是l,c 在同一個位置 == 0, 要同時往右因為此位置已決定了
class Solution:
    def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead. 2 pointer skill
    """
        p_left, p_right = 0, len(nums)-1
        cur = 0
        while cur <= p_right:
            if nums[cur]==0:  #why 交換後 cur指針也要跟著往右動, 因為交換回來的只有可能是1, 還有一個可能是l,c 在同一個位置 == 0, 要同時往右因為此位置已決定了
                nums[p_left], nums[cur] = nums[cur], nums[p_left] #遇到0擺左邊 值交換 [00 (1) 1 (0) 22]>[00 (0) 1 (1) 22]
                cur += 1 
                p_left += 1 #往右移動 最終大於p_right
            elif nums[cur]==1: #遇到1 不做任何動作 前往下一個
                cur += 1
            elif nums[cur]==2: #這邊也可用else, 注意只動right指針, cur沒動, why? 因為交換回來的有可能是2 or 0, 待cur指針來判斷
                nums[p_right],  nums[cur] = nums[cur], nums[p_right] #遇到2擺右邊 值交換
                p_right -= 1 #往左移動 最終小於cur, 代表遍歷結束


#3 way quick sort, time complexity O(n), 看來只適用這種只有三個數字的序列, 因為< target or > target 區間都不會排序
# Function 3-way partition partition the array a into three parts: < x part, = x part, and > x part.
#         We need to three pointer to do that ,which is left , right , i
#         where i scans the array
#         [m1, m2) indicates the ' = x part'
#         To be more specific : m1 indicates the index of the first digit whose value equals to pivot,
#         m2 indicates the first index of the digit among the array whose value is greater than the pivot (but it may not be  the smallest digit among them cuase no sort)

#刷題用這個, time complexity O(n)
#思路: pivot 就是中間值, 分成 比pivot小, pivot, 比pivot大 三塊
#m1指針代表第一個與pivot 大小相同的元素index, m2指針代表第一個比pivot大的元素index, 自己推算就知道了, [0,1,0,2,0,1,2]
#以這樣的思維就能分成三堆
class Solution: 
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.partition3(nums,0,len(nums),1)


    def partition3(self, a, left, right,pivot):
        m1 = left 
        m2 = left
        for i in range(left, right):
            if a[i] == pivot : 
                # if it equals the pivot ,only m2 changes ,
                # length of [m1,m2) will increase one
                a[i], a[m2] = a[m2],a[i] 
                m2 += 1;
            elif a[i] < pivot :
                # if it is smaller than the pivot ,then both of them
                # will increase one ,thus the length of [m1,m2) stays the same.
                # Since the element is smaller than the pivot, we should swap with m2 first
                # and then swap with m1 to let it in the right position. 
                # first swap a[i] with a[m2]
                a[i],a[m2] = a[m2],a[i]
                # Then Swap a[m2] with a[m1]
                a[m1],a[m2] = a[m2],a[m1]
                m1 += 1
                m2 += 1






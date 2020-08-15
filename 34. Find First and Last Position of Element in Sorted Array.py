#這題是好題 釐清binary search

time complexity: O(log n), space complexity O(1)


#模板1
#左閉右閉!!  這題很有趣
class Solution:
    def searchRange(self, nums, target):
        def binarySearchLeft(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if x > A[mid]: 
                    left = mid + 1
                else: 
                    right = mid - 1
            return left

        def binarySearchRight(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if x >= A[mid]: #重點在這
                    left = mid + 1
                else: 
                    right = mid - 1
            return right
        
        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return (left, right) if left <= right else [-1, -1]


# 模板2, 136ms
# 思路: left, right 指針針對nums[mid] = target 的動作來過濾左邊重複元素還是右邊重複元素
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: 
            return [-1, -1]
        left, right = self.binarySearchLeft(nums, target), self.binarySearchRight(nums, target)
        return [left, right]

    def binarySearchLeft(self, A, x):
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if x > A[mid]:  #重點在這
                left = mid 
            else: 
                right = mid 
        if x == A[left]:
            return left
        if x == A[right]:
            return right
        return -1
        
    def binarySearchRight(self, A, x):
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if x >= A[mid]:  #重點在這
                left = mid
            else: 
                right = mid   
        if x == A[right]:
            return right
        if x == A[left]:
            return left
        return -1

















    '''
    最終left, right 會碰再一起, 此時mid 就是他們所處位置
    def binarySearchRight(A, x):

        if x >= A[mid]: left = mid + 1, 這裡>= 使得x = A[mid], left 往右超過right, right 所處last posotion of element

    def binarySearchLeft(A, x):
        if x > A[mid]: left = mid + 1   這裡 > 使得x = A[mid], right往左 超過left, left 所處first posotion of element
                else: right = mid - 1

        a.searchRange([5,7,7,8,8,10],8) ans:(3,4)

        binarySearchLeft

        left:0 right:5 
        mid=2
        left:3 right:5
        mid=4
        left:3 right:3
        mid=3
        left:3 right:2
        return left 3

        binarySearchRight

        left:0 right:5 
        mid=2
        left:3 right:5
        mid=4
        left:5 right:5
        mid=5
        left:5 right:4
        return right 4 

        a.searchRange([5,7,7,8,8,10],9) ans:(-1,-1)

        binarySearchLeft

        left:0 right:5 
        mid=2
        left:3 right:5
        mid=4
        left:5 right:5
        mid=5
        left:5 right:4
        return left 5

        binarySearchRight

        left:0 right:5 
        mid=2
        left:3 right:5
        mid=4
        left:5 right:5
        mid=5
        left:5 right:4
        return right 4

        right < left return (-1,-1) 

'''


        










    '''
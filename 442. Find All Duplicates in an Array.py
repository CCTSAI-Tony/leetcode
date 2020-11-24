'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
'''

#自己想的, time complexity O(nlogn)
#思路: 先對nums sort, 重複的一定倆倆再一起, 若當前指針指到的元素跟前一個一樣, 就是重複元素
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        return [nums[i] for i in range(1, len(nums)) if nums[i] == nums[i-1]]


# The elements are between 1 and N and N is the size of the array. 
# Therefore we can implicitly map an element to an index i.e. 1 maps to index 0, 2 maps to index 1, ...N maps to index N-1
# Say for example that the number 4 appears twice. 4 implies index 3. We know that there are no negative numbers in the array. 
# How about I mark the number at index 3 as negative when I first encounter 4. 
# Now at the next occurence of 4, I will find the position implied by it (i.e. number at index 3) as negative. This means that 4 is a duplicate!
# Make sure you use the abs(x)-1 to select the index implied by x. That is because, in a previous iteration, the position of x might have been marked negative.
 
#  自己重寫, 刷題用這個, time complexity O(n), space complexity O(1)
#  思路: 利用in place modify的方式 來紀錄出現的元素, 因為裡面元素的值介於 1 ~ n, 剛好搭配zero baseed index, 1 map index 0, 2 map index 1....
#  mark 的方式 就是把map index的元素乘以-1, 若出現同個元素那map的位置是一樣的, map到的元素就是負數, 就知道之前有出現相同元素
#  注意的地方就是要使用abs(nums[i]), 因為nums[i] 有可能被前面元素map 而變負數
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                res.append(abs(nums[i]))
            else:
                nums[abs(nums[i])-1] = nums[abs(nums[i])-1] * -1
        return res


#重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                res.append(abs(nums[i]))
            else: 
                nums[abs(nums[i]) - 1] *= -1
        return res









#time complexity O(n), space complexity O(1)
class Solution(object):
    def findDuplicates(self, nums):
        result = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                result.append(abs(x))
            else:
                nums[abs(x)-1] = -1*nums[abs(x)-1]
        return result

# input and output are not counted in space complexity calculations






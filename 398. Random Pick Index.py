'''
Given an array of integers with possible duplicates, randomly output the index of a given target number. 
You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
'''

O(N) memory, O(N) init, O(1) pick.
import random
class Solution(object):
    def __init__(self, nums):
        self.nums = nums
    
    def pick(self, target):
        res = None
        count = 0
        for i, x in enumerate(self.nums):
            if x == target:
                count += 1
                chance = random.randint(1, count)
                if chance == count:
                    res = i
        return res

# In case people are wondering, the check 'chance == count' , can be replaced with 'chance == 1' . Result will be the same.

# wait how can it be same? it getting updated as we see more occurances of the target in nums.

# it's because chance==1 and chance==0 have the same probability

# How does it guarantee that res won't be None at the end?

# When we hit the first target (and we are guaranteed that there is at least one target element), count = 1 and chance = random.randint(1, count) = 1. 

# Therefore, res gets updated.
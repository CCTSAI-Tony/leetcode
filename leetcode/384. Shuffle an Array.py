'''
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

@@The solution expects that we always use the original array to shuffle() else some of the test cases fail. (Credits; @snehasingh31)

so we use nums[:] to represent the original list
'''

# easy python solution based on generating random index and swapping

#思路: 利用random 來做隨機shuffling, 記得建一個attribute 來存原本的nums, 在做shuffling 的時候, 要copy() or [:], 不然原序列會被影響
#shuffling 的range 與 該index有可能被swap的機率呈反比
# For example, assume there are 5 numbers are in a hat, you picked one and placed it outside 
# ( in our case swapped it with the one in the position we are looking to fill), 
# Now the next time you want to pick a number from the remaining 4.
import random
class Solution(object):

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        ans = self.nums[:]  #這個[:] 很重要代表copy 原來的list, 所以以下交換時不影響原來的list               
        for i in range(len(ans)-1, 0, -1):     # start from end, but not include 0, cause randrange(0, 1) always 0, trivial
            j = random.randrange(0, i+1)    # generate random index 
            ans[i], ans[j] = ans[j], ans[i]    # swap
        return ans


# For the last position, once you generate a random number in range (0,len(ans)), you would have decided the value 
# that is going to go in that position after shuffling. So once the swap is done, the new element there is already in its 'random' position 
# (or in other words a random element of that array has been put at that position. 
#     In the next iteration you are looking for a random index among the leftover numbers for the last but one position, 
#     so the index has to be from a range one less.

# For example, assume there are 5 numbers are in a hat, you picked one and placed it outside 
# ( in our case swapped it with the one in the position we are looking to fill), 
# Now the next time you want to pick a number from the remaining 4.


nums[:] vs nums
# This syntax is a slice assignment. A slice of [:] means the entire list. The difference between nums[:] = and nums = is that the latter 
# doesn't replace elements in the original list. This is observable when there are two references to the list

# >>> original = [1, 2, 3]
# >>> other = original
# >>> original[:] = [0, 0] # changes the contents of the list that both
#                          # original and other refer to 
# >>> other # see below, now you can see the change through other
# [0, 0]
# To see the difference just remove the [:] from the assignment above.

# >>> original = [1, 2, 3]
# >>> other = original
# >>> original = [0, 0] # original now refers to a different list than other
# >>> other # other remains the same
# [1, 2, 3]


# nums = foo rebinds the name nums to refer to the same object that foo refers to.

# nums[:] = foo invokes slice assignment on the object that nums refers to, 
# thus making the contents of the original object a copy of the contents of foo.

# Try this:

# >>> a = [1,2]
# >>> b = [3,4,5]
# >>> c = a
# >>> c = b
# >>> print(a)
# [1, 2]
# >>> c = a
# >>> c[:] = b
# >>> print(a)
# [3, 4, 5]


# a = [1,2,3,4,5]
# b = a
# b[1],b[2] = b[2], b[1]
# b
# [1, 3, 2, 4, 5]
# a
# [1, 3, 2, 4, 5]
# a = [1,2,3,4,5]
# b = a[:]  #copy list identical like a 
# b[1],b[2] = b[2], b[1]
# b
# [1, 3, 2, 4, 5]
# a
# [1, 2, 3, 4, 5]

#重點 
# a = b[:] copy list identical like b
# a = b, a[1],a[2] = a[2], a[1] 會間接影響 b, 若a = b[:] a[2] = a[2], a[1] 則不會影響

# a = b, a = c, b不會變, a只是改reference
# a = b, a[:]=c, b會變, 這裡a[:]可以想像成a = b[:] a[2] = a[2], a[1] 類似的情況, 


















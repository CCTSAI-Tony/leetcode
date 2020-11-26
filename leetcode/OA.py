# Question is as follows:

# You are given an array of integers arr. Your task is to count the number of contiguous subarrays, such that each element of the subarray appears at least twice.

# Language : Java
# Method signature : int duplicatesOnSegement(int[] arr){}

# Example:
# • For arr = [0, 0, 0], the output should be duplicatesOnSegment(arr) = 3.

# There are 3 subarrays that satisfy the criteria of containing only duplicate elements:
# • arr[0..1] = [0, 0]
# • arr[1..2] = [0, 0]
# • arr[0..2] = [0, 0, 0]

# • For arr = [1, 2, 1, 2, 3], the output should be duplicatesOnSegment(arr) = 1.

# There is only 1 applicable subarray arr[0..3] = [1, 2, 1, 2].

# Input/Output
# • [execution time limit] 3 seconds (java)
# • [input] array.integer arr

# An array of integers.

# Guranteed Constraints:
# 3 <= arr.length <= 10^3,
# 0 <= arr[i] <= 10^4,

# • [output] integer
# Return the number of contiguous subarrays in which each element occurs at least twice.

# time complexity O(n^2)
from collections import defaultdict
def func(A):
    result = 0
    for i in range(0,len(A)):
        counter = 0
        hash = defaultdict(int)
        for j in range (i, len(A)):
            hash[A[j]] += 1
            if hash[A[j]] == 2:
                counter += 1
            if counter != 0 and counter == len(hash):
                result += 1
    return result
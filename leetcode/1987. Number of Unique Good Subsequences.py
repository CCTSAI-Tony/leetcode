'''
You are given a binary string binary. A subsequence of binary is considered good if it is not empty and has no leading zeros (with the exception of "0").

Find the number of unique good subsequences of binary.

For example, if binary = "001", then all the good subsequences are ["0", "0", "1"], so the unique good subsequences are "0" and "1". 
Note that subsequences "00", "01", and "001" are not good because they have leading zeros.
Return the number of unique good subsequences of binary. Since the answer may be very large, return it modulo 109 + 7.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: binary = "001"
Output: 2
Explanation: The good subsequences of binary are ["0", "0", "1"].
The unique good subsequences are "0" and "1".
Example 2:

Input: binary = "11"
Output: 2
Explanation: The good subsequences of binary are ["1", "1", "11"].
The unique good subsequences are "1" and "11".
Example 3:

Input: binary = "101"
Output: 5
Explanation: The good subsequences of binary are ["1", "0", "1", "10", "11", "101"]. 
The unique good subsequences are "0", "1", "10", "11", and "101".
 

Constraints:

1 <= binary.length <= 105
binary consists of only '0's and '1's.
'''

'''
This problem is very similar to problem 940. Distinct Subsequences II, so if you already solved or at least have seen it, it will help a lot. 
The idea is to use dp, where dp[i] is number of unique subsequences for string S[0], ... S[i] - which do not start with 0 (we will deal with 0 case in the end). 
Then, each time we add symbol we need to do the following:

Imagine that we have t1, t2, ..., tk unique subsequences for i-1. We also have options t1 + S[i], t2 + S[i], ..., tk + S[i].
However some of strings are the same, exactly for this we keep dictionary last: is the last place for each symbol so far. So, we subtract dp[last[x]] number of options.
Also if we meet symbol 0 for the first time, we need to subtract 1.
Let us go through example S = 111000101 and see what what options we have:

S = 111000101
dp[0] = 1, we have only one option: empty string "".
Consider next symbol: 1, we have "", 1, dp[1] = 2.
Consider next symbol: 1. We need to double number of options: we have 4 of them: "", 1 and 1, 11 but one of them is repetition, it is dp[last[1]], so we have options "", 1, 11 and dp[3] = 3.
Similarly dp[4] = 4 and we have options "", 1, 11, 111.
Now we have element 0 and we meet it for the first time, so we have "", 1, 11, 111, 0, 10, 110, 1110. We need to remove option 0 at the moment, so we have "", 1, 11, 111, 10, 110, 1110 and dp[5] = 7.
Now we have again element 0. We meet it not for the first time, so we have previous options "", 1, 11, 111, 10, 110, 1110, new options are 0, 10, 110, 1110, 100, 1100, 11100. 
How many of this options are intersect: it is 10, 110, 1110 and also we need to remove "0", so optoins we are not happy with is 0, 10, 110, 1110, 
which is exaclty what we had on step 4 but with added 0.
I think you understand the logic now and can continue this for the rest of the string: I leave it to you as exercise, put your solutions in comments :)
In the end we need to deal with 0 case: we need to subtract -1 for empty set and add int("0" in S) to check if we have 0 in our string.
'''

# 刷題用這個, time complexity O(n), space complexity O(n)
# 思路: 使用dp, 詳情請看上面解說, 技巧就是推演
class Solution:
    def numberOfUniqueGoodSubsequences(self, S):
        dp, last = [1], {}
        for i, x in enumerate(S):
            dp.append(dp[-1] * 2)
            dp[-1] -= dp[last[x]] if x in last else int(x == "0")
            dp[-1] = dp[-1] % (10**9 + 7)
            last[x] = i

        return dp[-1] - 1 + int("0" in S)


# 重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        dp = [1]
        last = {}
        for i, num in enumerate(binary):
            dp.append(dp[-1] * 2)
            dp[-1] -= dp[last[num]] if num in last else int(num) == 0
            last[num] = i
        return (dp[-1] - 1 + int("0" in binary)) % (10**9 + 7)













'''
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
'''

# The number only has 8 digits, so there are only 8 choose 2 = 28 available swaps. Brute force them all for an O(N^2) solution which passes.

# We will store the candidates as lists of length len(num). For each candidate swap with positions (i, j), 
# we swap the number and record if the candidate is larger than the current answer, then swap back to restore the original number. 
# The only detail is possibly to check that we didn't introduce a leading zero. 
# We don't actually need to check it, because our original number doesn't have one(leading zero).

#brute force, time complexity O(n^2), space complexity O(n)
#思路: 把所有的交換組合走跑一遍, 看是否比ans大, 若是ans = A[:], 比較完後改回原本的狀態 => 換回原本元素位置
#交換後不用考慮leading zero的問題, 因為一開始的num沒有leading zero, 交換出來的組合就算有leading zero 也不會比原num大
class Solution:
    def maximumSwap(self, num):
        A = list(str(num))
        ans = A[:]
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                A[i], A[j] = A[j], A[i]
                if A > ans: 
                    ans = A[:]
                A[i], A[j] = A[j], A[i] #換回來
        return int("".join(ans))

["2","5"] > ["2","8"] => False
["2","5"] > ["2","2"] => True
["0","5"] > ["5","0"] => False

We can also get an O(N) solution. At each digit, if there is a larger digit that occurs later, we want the swap it with the largest such digit that occurs the latest.

#time complexity O(n), space complexity O(n)
#思路: 讓大的digit 盡量交換到左邊, 讓小的digit盡量交換到右邊 => 位數的關係, 一開始建立dict紀錄每個digit最右邊的index, 
#從左邊開始遍歷, 找尋比該digit大的數字是否存在num裡, 從9往下找, 若找到則對比該數字的last index是否 > i, 若是則交換
#這樣一來, 大的數字位元最大程度提高, 小的數字位元最大程度降低
class Solution:
    def maximumSwap(self, num):
        a = list(map(int, str(num)))
        last = {x: i for i,x in enumerate(a)} #紀錄每個數字最後的index
        for i,x in enumerate(a):
            for d in range(9,x,-1): #倒序遍歷比自己大的digit O(10)
                if d in last:
                    if last[d]>i:
                        a[last[d]],a[i]=a[i],a[last[d]]
                        return int(''.join(map(str,a)))
        return num


#自己重寫, time complexity O(n), space complexity O(n)
class Solution:
    def maximumSwap(self, num: int) -> int:
        A = list(map(int, str(num)))
        last = {v:i for i, v in enumerate(A)}
        for i in range(len(A)):
            for d in range(9, A[i], -1):
                if d in A and last[d] > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(map(str, A)))
        return num









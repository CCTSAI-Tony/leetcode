'''
Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  The guards have gone and will come back in H hours.

Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, and eats K bananas from that pile.  
If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.

Return the minimum integer K such that she can eat all the bananas within H hours.

 

Example 1:

Input: piles = [3,6,7,11], H = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], H = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], H = 6
Output: 23
 

Note:

1 <= piles.length <= 10^4
piles.length <= H <= 10^9
1 <= piles[i] <= 10^9
'''

# 思路: 題目有提到 piles.length <= H <= 10^9, H最小時候是當piles.length == H, 吃貨量為 max(piles), 超過它以上結果都一樣
# 當吃貨量為1, 會造成H所花時間最長 => lo, hi = 1, max(piles), 並利用 check來判斷此吃貨量是否可以 <= H, 來判斷與調整吃貨量
# 題目跟1283 是一樣的

# time complexity O(nlogm) (m=max(arr)), n = len(piles), space complexity O(1)
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        lo, hi = 1, max(piles)
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if self.check(piles, H, mid):
                hi = mid
            else:
                lo = mid
        if self.check(piles, H, lo):
            return lo
        else:
            return hi
            
        
    def check(self, piles, H, mid):
        res = 0
        for pile in piles:
            res += ceil(pile / mid)  #向上取整
        return res <= H


#重寫第二次, time complexity O(nlogm), m: max(piles), space complexity O(1)
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l, r = 1, max(piles)
        while l + 1 < r:
            mid = l + (r - l) // 2
            if self.helper(mid, piles) > H:
                l = mid
            else:
                r = mid
        if self.helper(l, piles) <= H:
            return l
        return r
    
    
    def helper(self, k, piles):
        hr = 0
        for pile in piles:
            if pile % k:
                hr += (pile // k + 1)
            else:
                hr += pile // k
        return hr







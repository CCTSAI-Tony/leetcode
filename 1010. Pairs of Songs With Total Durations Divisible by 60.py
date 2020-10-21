'''
In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  
Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 

Note:

1 <= time.length <= 60000
1 <= time[i] <= 500
'''

#看提示自己想的, time complexity O(n)
#思路: 我們只考慮每個數%60的值, 並把它加到dict, 並遍歷1-29, 看是否有對應的值加起來 == 60, 此時組合數就是mod[i]*mod[60-i] => 每個組合只有一種排序 => 一定可以 i < j
#針對30, 60 的組合數為 C(n取二) 若mod(30), mod(60) > 1 else 0
from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mod = defaultdict(int)
        for t in time:
            mod[t % 60] += 1
        count = 0
        for i in range(1, 30):
            if (60-i) in mod:
                count += mod[i]*mod[60-i] #可以pair 的組合
        if mod[0] > 1:
            count += (mod[0]*(mod[0]-1))//2
        if mod[30] > 1:
            count += (mod[30]*(mod[30]-1))//2
        return count










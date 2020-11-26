'''
In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring", 
and use the dial to spell a specific keyword in order to open the door.

Given a string ring, which represents the code engraved on the outer ring and another string key, which represents the keyword needs to be spelled. 
You need to find the minimum number of steps in order to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at 12:00 direction. 
You need to spell all the characters in the string key one by one 
by rotating the ring clockwise or anticlockwise to make each character of the string key aligned at 12:00 direction and then by pressing the center button.

At the stage of rotating the ring to spell the key character key[i]:

You can rotate the ring clockwise or anticlockwise one place, which counts as 1 step. 
The final purpose of the rotation is to align one of the string ring's characters at the 12:00 direction, where this character must equal to the character key[i].
If the character key[i] has been aligned at the 12:00 direction, you need to press the center button to spell, 
which also counts as 1 step. After the pressing, you could begin to spell the next character in the key (next stage), otherwise, you've finished all the spelling.
Example:


 
Input: ring = "godding", key = "gd"
Output: 4
Explanation:
For the first key character 'g', since it is already in place, we just need 1 step to spell this character. 
For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
Also, we need 1 more step for spelling.
So the final output is 4.
Note:

Length of both ring and key will be in range 1 to 100.
There are only lowercase letters in both strings and might be some duplcate characters in both strings.
It's guaranteed that string key could always be spelled by rotating the string ring.
'''

# Store every index of every character in ring in indexes hashtable
# Initialize steps for every index in ring in DP
# For first character of key, update every DP[i] as distance btw zero index plus 1 step for press
# For every next character in key, update every DP[i] as min distance btw pre indexes plus 1 step for press
# Return min DP for last character of key
# why are we doing the plus 1's everytime? Ans: we need 1 more step for spelling.

#time complexity O(rk)
#思路: dp[i] 代表從key[0] spell 到目前key letter's index[i] 所花的最小 spell steps, 這裡i 是 key letter 在ring 的 indexes
#dp[j] 代表前一個letter 在ring 個別index 最小的spell steps
#for key[0], dp[i] = min(i, n - i) + 1, 每個key[0]的letter index 轉到12點鐘的最小steps, 目前12點鐘的index = 0, => min(i, n - i) => 逆, 順 時鐘轉ring
#dp[i] = min(dp[j] + min(i - j, j + n - i) if i >= j else dp[j] + min(j - i, i + n - j) for j in indexes[pre]) + 1 => dp[i] 參照前一個letter dp[j] 選一個最小步數方案
#技巧: i >= j => min(i-j, n-i+j), i < j => min(j-i, n-j+i) => circle index, 順逆反向對應i,j 之間的距離
class Solution:
    def findRotateSteps(self, ring, key):
        indexes, n, dp, pre = collections.defaultdict(list), len(ring), [0] * len(ring), key[0]
        for i, c in enumerate(ring): #紀錄每個character 在 ring 的 初始indexes
            indexes[c].append(i)
        for i in indexes[key[0]]: #初始: 找出每個key[0] 在ring 的 index 最小的移動steps + 1(spell)
            dp[i] = min(i, n - i) + 1  #技巧: i 代表逆時鐘轉ring 至 12點鐘, n - i 代表順時鐘轉ring 至 12點鐘
        for c in key[1:]:
            for i in indexes[c]:
                dp[i] = min(dp[j] + min(i - j, j + n - i) if i >= j else dp[j] + min(j - i, i + n - j) for j in indexes[pre]) + 1
            pre = c #紀錄前一個letter
        return min(dp[i] for i in indexes[key[-1]]) #找出index[key[-1]] 的indexes中, 誰的步數最小


#自己重寫, time complexity O(r*k), 刷題用這個
from collections import defaultdict
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        indexes = defaultdict(list)
        for i, v in enumerate(ring):
            indexes[v].append(i)
        n = len(ring)
        dp = [0] * n
        pre = key[0]
        
        for i in indexes[key[0]]:
            dp[i] = min(i, n-i) + 1
        
        for c in key[1:]:
            for i in indexes[c]:
                dp[i] = min(dp[j] + min(i-j, n-i+j) if i >= j else dp[j] + min(j-i, n-j+i) for j in indexes[pre]) + 1
            pre = c
        
        return min(dp[i] for i in indexes[key[-1]])








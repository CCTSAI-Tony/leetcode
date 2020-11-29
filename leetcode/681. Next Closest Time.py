'''
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, 
because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. 
It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
'''



#刷題用這個, time complexity O(16), space complecity O(16)
#思路: 利用sort 來製造2 digits 組合
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        hour, minute = time.split(":")
        
        # Generate all possible 2 digit values
        # There are at most 16 sorted values here
        nums = sorted(set(hour + minute)) #關鍵
        two_digit_values = [a+b for a in nums for b in nums] #關鍵

        # Check if the next valid minute is within the hour
        i = two_digit_values.index(minute)
        if i + 1 < len(two_digit_values) and two_digit_values[i+1] < "60":
            return hour + ":" + two_digit_values[i+1]

        # Check if the next valid hour is within the day
        i = two_digit_values.index(hour)
        if i + 1 < len(two_digit_values) and two_digit_values[i+1] < "24":
            return two_digit_values[i+1] + ":" + two_digit_values[0]
        
        # Return the earliest time of the next day
        return two_digit_values[0] + ":" + two_digit_values[0]





#自己想的, time complexity O(4**4), space complexity O(4)
#思路: backtracking, 這題容易搞混的地方是output 一定要集滿四個digits
class Solution:
    def nextClosestTime(self, time: str) -> str:
        time = time.split(":")
        self.time = int(time[0]) * 60 + int(time[1])
        self.diff = float("inf")
        time = "".join(time)
        self.dfs(time, "")
        h = str(((self.time + self.diff) // 60) % 24)
        m = str((self.time + self.diff) % 60)
        if len(h) == 1:
            h = "0" + h
        if len(m) == 1:
            m = "0" + m   
        return h + ":" + m
    
    def dfs(self, time, path):
        if len(path) == 4:
            hh, mm = path[:2], path[2:]
            if int(hh) >= 24 or int(mm) >= 60:
                return
            temp = int(hh)*60 + int(mm)
            if temp <= self.time:
                temp += 60 * 24
            diff = temp - self.time
            if diff < self.diff:
                self.diff = diff
            return
        for n in time:
            self.dfs(time, path + n)



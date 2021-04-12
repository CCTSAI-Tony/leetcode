'''
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.
'''

# Intuition
# Is this a real interview problem?
# The formula for this problem is Zelle formula
# Another name: Zeller's congruence or Kim larsen calculation formula.

Complexity
Time O(1)
Space O(1)

Python:

class Solution:
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", ]
    def dayOfTheWeek(self, d, m, y):
        if m < 3:
            m += 12
            y -= 1
        c, y = y / 100, y % 100
        w = (c / 4 - 2 * c + y + y / 4 + 13 * (m + 1) / 5 + d - 1) % 7
        return self.days[w]

Python Cheat
As I mentioned the usage of datetime in 1154. Day of the Year
I google the doc of package and find a method called weekday

class Solution:
    def dayOfTheWeek(self, d, m, y):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        from datetime import datetime  # index 0 is Monday
        return days[datetime(y, m, d).weekday()]







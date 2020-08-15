'''
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  
The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
 

Constraints:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
'''

#刷題用這個
#time: O(nlogn)
#思路: sort 排序技巧! prioirity: without identifier => if ties => compare identifier
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key = lambda x: (x.split()[1:],x.split()[0]))
        return letters + digits






class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digits = []
        letters = []
        # divide logs into two parts, one is digit logs, the other is letter logs
        for log in logs:
            if log.split()[1].isdigit():  #split() 預設遇到任何空格split
                digits.append(log)
            else:
                letters.append(log)
                
        letters.sort(key = lambda x: x.split()[0])            #when suffix is tie, sort by identifier, 注意 先做這一步
        letters.sort(key = lambda x: x.split()[1:])           #sort by suffix
        result = letters + digits                                        #put digit logs after letter logs
        return result



# a = "dig1 8 1 5 1"
# a.split()
# ['dig1', '8', '1', '5', '1']

# my_nums = [1,2,3,4,5]
# list(map(lambda num: num ** 2, my_nums))
# [1, 4, 9, 16, 25]


# nums = [0,1,2,3,4,5,6,7,8,9,10]
# list(filter(lambda n: n % 2 == 0,nums))
# [0, 2, 4, 6, 8, 10]

# filtered = filter(fun, sequence) 

# map & filter 常與lambda連用



















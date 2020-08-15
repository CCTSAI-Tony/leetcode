'''
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. 
Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match 
your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number 
but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
'''

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        l1, l2 = [0]*10, [0]*10 #0-9 digit
        nums1, nums2 = list(map(int, secret)), list(map(int, guess)) #map returns a generator, nums1 [1,1,2,3] nums2 [0,1,1,1]
        length = len(secret)
        for i in range(length):
            if nums1[i] == nums2[i]:
                bulls += 1
            else:
                l1[nums1[i]] += 1
                l2[nums2[i]] += 1
        cows = sum(map(min, zip(l1,l2))) #這招去除重複digit 的cow, 請用這個例子自己想 secret = "1123", guess = "0111" Output: "1A1B"
        return '%dA%dB' % (bulls, cows)





# secret = "1807"
# g = map(int, secret)
# for i in g:
#     print(i)

# 1
# 8
# 0
# 7

# l1 = [9,8,3]
# l2 =[4,1,7]
# list(map(min, zip(l1,l2)))
# [4, 1, 3]

# sum(map(min, zip(l1,l2)))
# 8














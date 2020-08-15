'''
[1, 2, 3, 4] represents integer 1234, add one to 1234(the length of array not changed), 
you get 1235. but [9, 9, 9, 9] represents 9999, add one to 9999, you get 10000(the length of array changed)

'''
class Solution(object):
    def plusOne(self, digits):
        if digits == []:  #just for case: digits = [9] 進位增加位數
            return [1]
        if digits[-1] != 9:
            return digits[:-1]+[digits[-1]+1] #list處裡 [digits[-1]+1]
        else:
            return self.plusOne(digits[:-1])+[0] #就像骨牌效應





class Solution(object):
    def plusOne(self, digits):
        digits = digits or [0] #進位增加位數
        last = digits.pop()
        
        if last == 9:
            return self.plusOne(digits) + [0]
        else:
            return digits + [last + 1]






'''
a = [1,2,3,4,5]
a[:-1]

[1, 2, 3, 4]

'''
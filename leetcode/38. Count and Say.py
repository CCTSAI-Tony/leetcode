class Solution(object):
    def countAndSay(self, n):
        s = '1'
        for _ in range(n-1): # 已經有base 1
            let, temp, count = s[0], '', 0
            for l in s:
                if let == l:
                    count += 1
                else:
                    temp += str(count)+let
                    let = l  #不斷更換
                    count = 1
            temp += str(count)+let
            s = temp
        return s

        '''
        1.     1
        2.     11
        3.     21
        4.     1211
        5.     111221
        1 is read off as "one 1" or 11.
        11 is read off as "two 1s" or 21.
        21 is read off as "one 2, then one 1" or 1211.






        '''
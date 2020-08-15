'''
A string S of lowercase English letters is given. 
We want to partition this string into as many parts as possible so that each letter appears in at most one part, 
and return a list of integers representing the size of these parts.

 

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 

Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
'''

#自己想的, time complexity O(n), n = len(S), 76ms, 刷題也可用這個
#  思路: 利用dict儲存每個字母 leftmost,rightmost index, 再遍歷S, 若字母的leftmost index沒有超過前面part的rightmost index, 則屬於同一part, 並更新此part的rightmost index
#  若字母的leftmost index超過前面part的rightmost index, 則屬於新part, res.append 舊part, 更新 leftmost,rightmost index based on 新字母
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = dict() #紀錄每個字母 leftmost,rightmost index
        for i in range(len(S)):
            if S[i] not in d:
                d[S[i]] = [i,i] #記得這裡不能用tuple, 因為tuple裡面元素不能修改
            else:
                d[S[i]][1] = i
        res = []
        start,end = d[S[0]] #初始S[0]
        for s in S:
            if d[s][0] < end: #屬於同一part
                end = max(end, d[s][1])
            elif d[s][0] > end:  #進入新part, 越多part越好, greedy
                res.append(end-start+1)  #append前一part的值
                start, end = d[s]
        res.append(end-start+1)
        return res


#  別人的答案 time complexity O(n), 刷題用這個
#  思路: 一樣儲存每個字母的rightmost index, 再遍歷S, 指針每遍歷一個元素就更新right 指針, 
#  若指針走到right指針 , 代表這一part已結束, res append 此part, 此part之後的序列都不會出現此part的元素
#  left指針移動此part的下一個index
class Solution:
    def partition_labels(S):

        rightmost = {c:i for i, c in enumerate(S)} #dic comprehension
        left, right = 0, 0

        result = []
        for i, letter in enumerate(S):

            right = max(right,rightmost[letter])
        
            if i == right:
                result += [right-left + 1]
                left = i+1

        return result






 


 




















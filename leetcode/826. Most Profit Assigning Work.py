'''
We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i] is the profit of the ith job. 

Now we have some workers. worker[i] is the ability of the ith worker, which means that this worker can only complete a job with difficulty at most worker[i]. 

Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.  If a worker cannot complete any job, his profit is $0.

What is the most profit we can make?

Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100 
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.
Notes:

1 <= difficulty.length = profit.length <= 10000
1 <= worker.length <= 10000
difficulty[i], profit[i], worker[i]  are in range [1, 10^5]
'''


# 刷題用這個 396 ms
# Sort and Two pointer
# zip difficulty and profit as jobs.
# sort jobs and sort 'worker'.
# Use 2 pointers. For each worker, find his maximum profit best he can make under his ability.

# Because we have sorted jobs and worker,
# we will go through two lists only once.
# this will be only O(D + W).
# O(DlogD + WlogW), as we sort jobs.
#  思路: jobs = sorted(zip(difficulty, profit)), 這樣一來等等 依能力 sorted worker 來遍歷jobs就可以依難度遍歷one pass
#  使用2 pointer for each worker, i 來遍歷jobs, 另一指針來紀錄此工人能力可獲得最大的profit, 因為工人依能力排序, 前一工人能做到的, 後一工人延續
 
class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = sorted(zip(difficulty, profit))  #tuple, default, 依difficult sort
        res = i = best = 0
        for ability in sorted(worker):
            while i < len(jobs) and ability >= jobs[i][0]:  #看能勝任到多大難度
                best = max(jobs[i][1], best)  #取最大profit
                i += 1  #i指針持續往右, 因為worker已經sorted, 前一個能勝任的, 下一個也可以, best profit同理
            res += best
        return res








#  最難的工作並不是利潤最高的, 還有不同的難度的工作有同樣profit, 因此每個不同 profit要match 最低難度的工作, 才能金錢最大化
#  自己想的 time complexity O(nlogn), n: len(profit) 因為sort, 388ms
#  思路:  一開始建立dict 來紀錄 一個profit 對應到最少的難度是多少, 之後sorted profit and worker
#  倒序遍歷 profit, 若worker[-1] 有能力超過此profit的難度, 紀錄下來此profit的count, 並把此worker排除, 這樣的遍歷保證每個工人的profit最大化
#  這個算單指針解法
from collections import defaultdict
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        profitsHard = dict()
        for i in range(len(profit)):
            if profit[i] not in profitsHard:
                profitsHard[profit[i]] = difficulty[i]
            else:
                profitsHard[profit[i]] = min(profitsHard[profit[i]], difficulty[i])
        
        profit.sort()
        worker.sort()
        workCount = defaultdict(int)
        for i in range(len(profit)-1,-1,-1):
            while worker and worker[-1] >= profitsHard[profit[i]]:
                worker.pop()
                workCount[profit[i]] += 1
            if not worker:  #提早結束
                break
        
        return sum(i[0]*i[1] for i in workCount.items())




 



      
        












  



  


 





















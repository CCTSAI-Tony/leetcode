'''
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

 

Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]
 

Note:

cells.length == 8
cells[i] is in {0, 1}
1 <= N <= 10^9
'''

# Let us solve this problem by definition: we do iteration by iteration. However if N is very big, 
# then we spend O(N) time and it can take too much time. Note, that there can be only 2^8 possible options for cells 
# (in fact only 2^6 even, because after first step the first and the last symbols will always be zeros). It means, 
# that afrer some number of iterations, cells start to repeat, and we found a loop.

# How can we find a loop? We need to keep our positions in hash-table, so we can find loop_len. 
# We do iteration by iteration and if we found a loop, we need to do (N - i) % loop_len more steps.

# Complexity: time and memory is O(64), because the loop size will be not more than 2^6

# the repeatition or pattern or cyclicality may start at N = 0 or 1.
# Fact: the first and last element of the list will always be 0.
# If your input starts with 1 [1......] or ends with 1[......1], it couldn't be in the cyclicality.
# So We can't assume the input is inside the cyclicality.

#思路: 此題cell 是 0 or 1, cells 有八個, 但頭尾cell 經過第一天都會變成0, 因此cells的全部可能排列可能 = 2^6 
#破題: cells pattern 一定會有loop 且loop_len 只有一個, 
#why 一定有loop, 想一下若N > 64, 假設之前每一天cells都不一樣, 最久經過64天cells一定會遇到之前一樣的排列, 若沒有遇到一樣的代表有第65種新排列 => 矛盾!!
#cells pattern 會從N=0 or 1 開始loop, 若初始頭尾其一不是0的話 => N=0 不能算進loop pattern, 要從N=1 開始
#利用dict 來紀錄改天的cells排列, 若之後遇到一樣的就能計算loop_len, 把剩餘天數 % loop_len 就能大幅減少之後要迭代的天數, 若%完 == 0, 直接retrun 當下cells 排列
#trick: 此題若沒找loop直接一天一天迭代, time complexity => O(n), 因此先計算所有排列的可能性就能知道是否有優化的可能
#time complexity O(64), space complexity O(64 or 65), ex:N = 127, loop_len = 64 => 總共迭代127天 < 2 * 64
class Solution:
    def prisonAfterNDays(self, cells, N):
        found_dic = {}
        for i in range(N):
            cells_str = str(cells) #str化 才能當hash key
            if cells_str in found_dic:
                loop_len = i - found_dic[cells_str] #計算loop長度
                return self.prisonAfterNDays(cells, (N - i) % loop_len) #(N - i) => 剩餘天數, i => i天的cells
            else:
                found_dic[cells_str] = i 
                cells = self.next_step(cells) #進入下一天的cells
                
        return cells


    def next_step(self, cells):
        res = [0] * 8
        for i in range(1,7): #扣除首尾
            res[i] = int(cells[i-1] == cells[i+1]) 
        return res

#自己重寫 time complexity O(64) => O(1)
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        memo = {}
        for i in range(N):
            cells_str = str(cells)
            if cells_str in memo:
                loop_len = i - memo[cells_str]
                return self.prisonAfterNDays(cells, (N -i) % loop_len)
            else:
                memo[cells_str] = i
                cells = self.next_day(cells)
        return cells
                
                
    def next_day(self, cells):
        new_cells = [0] * 8
        for i in range(1,7):
            new_cells[i] = int(cells[i-1] == cells[i+1])
        return new_cells







#自己想的 naive loop TLE, time complexity O(8*N => O(n)
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        n = 0
        while n < N:
            new_cells = []
            for i in range(len(cells)):
                if i == 0 or i == len(cells) - 1:
                    new_cells.append(0)
                else:
                    if cells[i-1] == cells[i+1]:
                        new_cells.append(1)
                    else:
                        new_cells.append(0)
            n += 1
            cells = new_cells
            
        return cells
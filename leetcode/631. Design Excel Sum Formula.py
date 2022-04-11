'''
Design the basic function of Excel and implement the function of the sum formula.

Implement the Excel class:

Excel(int height, char width) Initializes the object with the height and the width of the sheet. 
The sheet is an integer matrix mat of size height x width with the row index in the range [1, height] 
and the column index in the range ['A', width]. All the values should be zero initially.
void set(int row, char column, int val) Changes the value at mat[row][column] to be val.
int get(int row, char column) Returns the value at mat[row][column].
int sum(int row, char column, List<String> numbers) Sets the value at mat[row][column] to be the sum of cells represented by numbers 
and returns the value at mat[row][column]. 
This sum formula should exist until this cell is overlapped by another value or another sum formula. numbers[i] could be on the format:
"ColRow" that represents a single cell.
For example, "F7" represents the cell mat[7]['F'].
"ColRow1:ColRow2" that represents a range of cells. 
The range will always be a rectangle where "ColRow1" represent the position of the top-left cell, 
and "ColRow2" represents the position of the bottom-right cell.
For example, "B3:F7" represents the cells mat[i][j] for 3 <= i <= 7 and 'B' <= j <= 'F'.
Note: You could assume that there will not be any circular sum reference.

For example, mat[1]['A'] == sum(1, "B") and mat[1]['B'] == sum(1, "A").
 

Example 1:

Input
["Excel", "set", "sum", "set", "get"]
[[3, "C"], [1, "A", 2], [3, "C", ["A1", "A1:B2"]], [2, "B", 2], [3, "C"]]
Output
[null, null, 4, null, 6]

Explanation
Excel excel = new Excel(3, "C");
 // construct a 3*3 2D array with all zero.
 //   A B C
 // 1 0 0 0
 // 2 0 0 0
 // 3 0 0 0
excel.set(1, "A", 2);
 // set mat[1]["A"] to be 2.
 //   A B C
 // 1 2 0 0
 // 2 0 0 0
 // 3 0 0 0
excel.sum(3, "C", ["A1", "A1:B2"]); // return 4
 // set mat[3]["C"] to be the sum of value at mat[1]["A"] and the values sum of the rectangle range whose top-left cell is mat[1]["A"] 
 and bottom-right cell is mat[2]["B"].
 //   A B C
 // 1 2 0 0
 // 2 0 0 0
 // 3 0 0 4
excel.set(2, "B", 2);
 // set mat[2]["B"] to be 2. Note mat[3]["C"] should also be changed.
 //   A B C
 // 1 2 0 0
 // 2 0 2 0
 // 3 0 0 6
excel.get(3, "C"); // return 6
 

Constraints:

1 <= height <= 26
'A' <= width <= 'Z'
1 <= row <= height
'A' <= column <= width
-100 <= val <= 100
1 <= numbers.length <= 5
numbers[i] has the format "ColRow" or "ColRow1:ColRow2".
At most 100 calls will be made to set, get, and sum.
'''

# Problem:

# This problem asks us to design a small excel spread sheet (less than 27 columns)
# that is capable of setting certain cells to either integer values or the dynamic
# sum of other cells.

# The Tricky Bits:

# The sum can include individual cells, a 2D range of cells, or both.
# Furthermore, if a sum contains cell "A1" and range "A1:B2" we should
# count the value in "A1" twice.

# The sum must be dynamic. If the sum contains "A1" and the value of
# "A1" changes from 2 to 3, then the sum should also increase by 1.

# The sum can include cells that also contain a dynamic sum.
# But there are no test cases that result in an infinite loop.

# Implementation:

# Create a 2D array form of dimensions H and W to store your values.

# When setting a value change form[r][c] to the integer value v.

# When setting a sum change form[r][c] to a multiset (counter)
# of the cells included in the sum. We can keep track of how many times
# each cell occurs in the sum using the multiset.

# The form now contains two data types, integers and multisets.

# When getting the value for a cell, check if the value is an integer.
# If so, simply return the integer.
# However, if the value is a multiset, then recursively call the get function on
# the cells included in the multiset. Remember to multiply the value of each
# cell by the number of times the cell occurs in the multiset.

# Things to Remember:

# Because the sum must be dynamic we cannot simply store the value
# of the current sum at (r, c). Instead we must record the summed cells
# at (r, c) and calculate the sum only when get is called.

# The given r is 1-based so we need to subtract 1 from r.

# The given c is a string so we make use of the unicode value ord(c)
# to convert c to an integer and subtract ord("A") = 65 from ord(c) so that
# the columns will range from 0 to the width of form. Note: extra steps will
# need to be taken if larger column inputs such as "AA", ..., "ZZZZ" are allowed.


# 刷題用這個
# 思路: 使用defaultdict(int) 來紀錄 sum 要加哪些cell
class Excel:

    def __init__(self, height: int, width: str):
        self.height, self.width = height, self._map(width) + 1
        self.form = [[0]*self.width for _ in range(self.height)]
        
    def _map(self, char):
        return ord(char) - 65
        

    def set(self, row: int, column: str, val: int) -> None:
        self.form[row-1][self._map(column)] = val

    def get(self, row: int, column: str) -> int:
        r, c = row-1, self._map(column)
        if type(self.form[r][c]) is int:
            return self.form[r][c]
        return sum(self.get(i+1, chr(j+65)) * self.form[r][c][(i, j)] for i, j in self.form[r][c])
    
    def _parse(self, string: str):
        i = int(''.join(char for char in string if char.isdigit())) - 1
        j = self._map([char for char in string if char.isalpha()][0])
        return i, j
        

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        cells = collections.defaultdict(int)
        for string in numbers:
            if ':' not in string:
                i, j = self._parse(string)
                cells[(i, j)] += 1
            else:
                start, end = string.split(':')
                i0, j0 = self._parse(start)
                i1, j1 = self._parse(end)
                for i in range(i0, i1+1):
                    for j in range(j0, j1+1):
                        cells[(i, j)] += 1
        self.form[row-1][self._map(column)] = cells
        return self.get(row, column)


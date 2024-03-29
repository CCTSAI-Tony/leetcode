/*
    N-Queens: place n queens such that no 2 queens atk each other, return all soln's

    Place queens per row, try all possibilities & validate for further rows, backtrack

    Time: O(n!)
    Space: O(n^2)
*/

class Solution {
private:
    unordered_set<int> cols;     //for Columns
    unordered_set<int> negDiag;  //for negative diagnals R-C
    unordered_set<int> posDiag;  //for positive diagnals R+C
    
    void backtrack(int n, int row, vector<vector<string>>& res, vector<string>& board){
        if(row==n){
            res.push_back(board);
            return ; 
        }
        
        for(int col = 0; col < n; col++){   //Shifting through each col
            if( cols.find(col) != cols.end() or //if queen alread placed in this col
                negDiag.find(row - col) != negDiag.end() or //if queen in negDiag
                posDiag.find(row + col) != posDiag.end()    //if queen in posDiag
              )
                continue;
            
            cols.insert(col);
            negDiag.insert(row - col);
            posDiag.insert(row + col);
            board[row][col] = 'Q';
            
            backtrack(n, row +1, res, board);
            
            cols.erase(col);
            negDiag.erase(row - col);
            posDiag.erase(row + col);
            board[row][col] = '.';
        }
    }
   
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> res;
        vector<string> board(n, string(n,'.'));
        backtrack(n, 0, res, board);
        return res;
    }
};


// 重寫第二次
class Solution {
public:
    unordered_set<int> cols;
    unordered_set<int> n_diag;
    unordered_set<int> p_diag;
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> res;
        vector<string> board(n, string(n,'.'));
        backtrack(n, 0, res, board);
        return res;
    }

    void backtrack(int n, int row, vector<vector<string>>& res, vector<string>& board) {
        if (row == n) {
            res.push_back(board);
            return ;
        }

        for (int col=0; col<n; col++) {
            if (cols.find(col) != cols.end() or n_diag.find(row-col) != n_diag.end() or p_diag.find(row+col) != p_diag.end()) continue;
            cols.insert(col);
            n_diag.insert(row-col);
            p_diag.insert(row+col);
            board[row][col] = 'Q';
            backtrack(n, row+1, res, board);
            cols.erase(col);
            n_diag.erase(row-col);
            p_diag.erase(row+col);
            board[row][col] = '.';
        }
    }
};

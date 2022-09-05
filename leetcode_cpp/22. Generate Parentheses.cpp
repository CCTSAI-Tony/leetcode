// The idea is intuitive. Use two integers to count the remaining left parenthesis (n) and the right parenthesis (m) to be added. 
// At each function call add a left parenthesis if n >0 and add a right parenthesis if m>0. 
// Append the result and terminate recursive calls when both m and n are zero.

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        addingpar(res, "", n, 0);
        return res;
    }
    void addingpar(vector<string> &v, string str, int n, int m){
        if(n==0 && m==0) {
            v.push_back(str);
            return;
        }
        if(m > 0){ addingpar(v, str+")", n, m-1); }
        if(n > 0){ addingpar(v, str+"(", n-1, m+1); }
    }
};

// 自己寫的, 刷題用這個, backtracking, time complexity O(2^n), space complexity O(n)
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        vector<char> path;
        dfs(res, path, 0, n);
        return res;
    }
    
    void dfs(vector<string>& res, vector<char>& path, int path_sum, int n) {
        if (path_sum < 0 || path_sum > n) return;
        if (path.size() == 2 * n) {
            if (path_sum == 0) {
                res.emplace_back(string(path.begin(), path.end()));
            }
            return;
        }
        char par[2] = {'(', ')'};
        for (auto c: par) {
            path.emplace_back(c);
            if (c == '(') dfs(res, path, path_sum + 1, n);
            else dfs(res, path, path_sum - 1, n);
            path.pop_back();
        }
    }
};

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        vector<char> path;
        dfs(res, path, 0, n);
        return res;
    }
    
    void dfs(vector<string>& res, vector<char>& path, int path_sum, int n) {
        if (path_sum < 0 || path_sum > n) return;
        if (path.size() == 2 * n) {
            if (path_sum == 0) {
                res.emplace_back(string(path.begin(), path.end()));
            }
            return;
        }
        for (auto c: string {"()"}) {  // string initialization
            path.emplace_back(c);
            if (c == '(') dfs(res, path, path_sum + 1, n);
            else dfs(res, path, path_sum - 1, n);
            path.pop_back();
        }
    }
};
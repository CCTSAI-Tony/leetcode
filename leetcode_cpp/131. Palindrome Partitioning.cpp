// 重寫第二次, 刷題用這個, time complexity O(N⋅2^N), where N is the length of string s, This is the worst-case time complexity when all the possible substrings are palindrome.
// For each substring, it takes O(N) time to generate the substring and determine if it is a palindrome or not
// space complexity O(N)
class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        vector<string> path;
        dfs(s, 0, res, path);
        return res;
    }

    void dfs(string& s, int index, vector<vector<string>>& res, vector<string>& path) {
        if (index == s.size()) {
            res.push_back(path);
            return;
        }
        for (int i=index; i<s.size(); i++) {
            if (isPalindrome(s, index, i)) {
                path.push_back(s.substr(index, i-index+1));
                dfs(s, i+1, res, path);
                path.pop_back();
            }
        }
    }

    bool isPalindrome(const string& s, int start, int end) {
        while (start <= end) {
            if (s[start++] != s[end--]) return false;
        }
        return true;
    }
};


class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string> > ret;
        if(s.empty()) return ret;
        
        vector<string> path;
        dfs(0, s, path, ret);
        
        return ret;
    }
    
    void dfs(int index, string& s, vector<string>& path, vector<vector<string> >& ret) {
        if(index == s.size()) {
            ret.push_back(path);
            return;
        }
        for(int i = index; i < s.size(); ++i) {
            if(isPalindrome(s, index, i)) {
                path.push_back(s.substr(index, i - index + 1));
                dfs(i+1, s, path, ret);
                path.pop_back();
            }
        }
    }
    
    bool isPalindrome(const string& s, int start, int end) {
        while(start <= end) {
            if(s[start++] != s[end--])
                return false;
        }
        return true;
    }
};
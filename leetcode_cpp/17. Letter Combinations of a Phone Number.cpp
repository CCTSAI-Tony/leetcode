// 刷題用這個, time complexity O(3(4)^n) space complexity O(n)
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        unordered_map<char, string> map;
        vector<string> ans;
        string temp;
        if (digits.empty()) return ans;
        map['2'] = "abc";
        map['3'] = "def";
        map['4'] = "ghi";
        map['5'] = "jkl";
        map['6'] = "mno";
        map['7'] = "pqrs";
        map['8'] = "tuv";
        map['9'] = "wxyz";
        dfs(0, digits, map, ans, temp);
        return ans;
    }

    void dfs(int index, string& digits, unordered_map<char, string>& map, vector<string>& ans, string& temp) {
        if (index == digits.size()) {
            ans.push_back(temp);
            return;
        }
        string str = map[digits[index]];
        for (auto c: str) {
            temp.push_back(c);
            dfs(index+1, digits, map, ans, temp);
            temp.pop_back();
        }
    }
};




class Solution {
public:
    
    void help(int i,vector<string>&ans,string digits,string&temp, unordered_map<char,string>mp){
        if(i==digits.size()){
            ans.push_back(temp);
            return;
        }
        
        string str=mp[digits[i]];
        for(int j=0;j<str.length();j++){
            temp.push_back(str[j]);
            help(i+1,ans,digits,temp,mp);
            
            //Bactracking
            temp.pop_back();
        }
    }
    vector<string> letterCombinations(string digits) {
        unordered_map<char,string>mp;
        vector<string>ans;
        string temp;
        if(digits==""){
            return ans;
        }
        mp['2']="abc";
        mp['3']="def";
        mp['4']="ghi";
        mp['5']="jkl";
        mp['6']="mno";
        mp['7']="pqrs";
        mp['8']="tuv";
        mp['9']="wxyz";
        
        help(0,ans,digits,temp,mp);
        return ans;
    }
};


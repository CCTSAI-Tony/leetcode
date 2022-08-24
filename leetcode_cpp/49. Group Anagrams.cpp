
// time complexity O(nklogk)
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // Base case
		if(strs.size() == 1)
            return {{strs[0]}};
        
        vector<vector<string>> ans;
        unordered_map<string, vector<string>> M;
        for(int  i = 0; i < strs.size(); i++)
        {
            string str = strs[i];
            sort(strs[i].begin(), strs[i].end()); // Sorting the string
            M[strs[i]].push_back(str);  // Sorted string is the key and the value is the initial string
        }
        for(auto i = M.begin(); i != M.end(); i++)
            ans.push_back(i -> second);  // Traversing the map and adding the vectors of string to ans
        return ans;
    }
};

//刷題用這個
//time complexity O(nk)
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        for (string s : strs) {
            mp[strSort(s)].push_back(s);
        }
        vector<vector<string>> anagrams;
        for (auto p : mp) { 
            anagrams.push_back(p.second);
        }
        return anagrams;
    }
private:
    string strSort(string& s) {
        int counter[26] = {0};
        for (char c : s) {
            counter[c - 'a']++;
        }
        string t;
        for (int c = 0; c < 26; c++) {
            t += string(counter[c], c + 'a'); // c + 'a' => ex: 1 + 'a' => 'b', counter[c] => 次數
        }
        return t;
    }
};

//重寫第二次
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        unordered_map<string, vector<string>> map;
        for (auto& str: strs){
            string strKey = strSort(str);
            map[strKey].push_back(str);
        }
        for (auto item: map){
            res.push_back(item.second);
        }
        return res;
    }
    
    string strSort(string& str){
        int counts[26] = {0};
        for (auto c: str){
            counts[c - 'a']++;
        }
        
        string temp;
        for (int i=0; i < 26; i++){
            temp += string(counts[i], i + 'a');
        }
        
        return temp;
    }
};

//重寫第三次
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        unordered_map<string, vector<string>> map;
        for (auto& str: strs){
            string strKey = strSort(str);
            map[strKey].push_back(str);
        }
        for (auto item: map){
            res.push_back(item.second);
        }
        return res;
    }
    
    string strSort(string& str){
        array<int, 26> counts {0};
        for (auto c: str){
            counts[c - 'a']++;
        }
        
        string temp;
        for (int i=0; i < 26; i++){
            temp += string(counts[i], i + 'a');
        }
        
        return temp;
    }
};


int main()
{
    string test {'a'};
    string test2;
    test += string(3, 2 + 'a');
    test2 = string(10, 10 + 'a');
    cout << test << endl;
    cout << test2 << endl;
    return 0;
}

accc
kkkkkkkkkk

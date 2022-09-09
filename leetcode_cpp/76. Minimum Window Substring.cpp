class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> letters;
        int start {0}, target_len = t.size();
        string min_window;
        for (auto c: t){
            letters[c]++;
        }
        for (int end = 0; end < s.size(); end++){
            if (letters[s[end]] > 0) target_len--;
            letters[s[end]]--;
            while (target_len == 0){
                int window_len = end - start + 1;
                if (!min_window.size() || window_len < (int) min_window.size()){
                    min_window = s.substr(start, end - start + 1);
                }
                letters[s[start]]++;
                if (letters[s[start]] > 0) target_len++;
                start++;
            }
        }
        return min_window;
    }
};

//  學到 s.substr(start, end - start + 1) 用法!
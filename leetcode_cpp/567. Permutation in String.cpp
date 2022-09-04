class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) return false;
        int letters[26] = {0};
        for (auto c: s1){
            letters[c - 'a']++;
        }
        int char_credit = s1.size();
        for (int i = 0; i < s2.size(); i++){
            if (letters[s2[i] - 'a'] > 0) char_credit--;
            letters[s2[i] - 'a']--;
            if (char_credit == 0) return true;
            if (((i - static_cast<int>(s1.size())) + 1) >= 0){ // why I need static_cast<int>(s1.size()) => prevent from addition of unsigned offset to 0x7fff12c01e20 overflowed error
                if (letters[s2[i - s1.size() + 1] - 'a'] >= 0) char_credit++;
                letters[s2[i - s1.size() + 1] - 'a']++;
            }
        }
        return false;
    }
};

// 重寫第二次
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) return false;
        int letters[26] = {0};
        for (auto c: s1){
            letters[c - 'a']++;
        }
        int char_credit = s1.size();
        for (int i = 0; i < s2.size(); i++){
            if (letters[s2[i] - 'a'] > 0) char_credit--;
            letters[s2[i] - 'a']--;
            if (char_credit == 0) return true;
            if ((i - (int) s1.size() + 1) >= 0){  // Converting by assignment: (int) s1.size(). This can be also considered as forceful casting.
                if (letters[s2[i - s1.size() + 1] - 'a'] >= 0) char_credit++;
                letters[s2[i - s1.size() + 1] - 'a']++;
            }
        }
        return false;
    }
};
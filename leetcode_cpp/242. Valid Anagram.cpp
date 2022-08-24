class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        int n = s.length();
        unordered_map<char, int> counts;
        for (int i = 0; i < n; i++) {
            counts[s[i]]++;
            counts[t[i]]--;
        }
        for (auto count : counts)
            if (count.second) return false;
        return true;
    }
};

// 重寫第二次, time complexity O(n), space complexity O(1)
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length())
            return false;
        int n = s.length();
        unordered_map<char, int> counts;
        for (int i = 0; i < n; i++){
            counts[s[i]] += 1;
            counts[t[i]] -= 1;
        }
        
        for (auto count: counts){
            if (count.second)
                return false;
        }
        
        return true;
    }
};

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        int n = s.length();
        int counts[26] = {0};
        for (int i = 0; i < n; i++) { 
            counts[s[i] - 'a']++;
            counts[t[i] - 'a']--;
        }
        for (int i = 0; i < 26; i++)
            if (counts[i]) return false;
        return true;
    }
};

// 重寫第二次, time complexity O(n), space complexity O(1)
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length())
            return false;
        int n = s.length();
        int counts[26] = {0};
        for (int i = 0; i < n; i++){
            counts[s[i] - 'a'] += 1;
            counts[t[i] - 'a'] -= 1;
        }
        
        for (int i = 0; i < 26; i++){
            if (counts[i])
                return false;
        }
        
        return true;
    }
};
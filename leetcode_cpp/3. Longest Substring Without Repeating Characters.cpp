class Solution {
public:
	int lengthOfLongestSubstring(string s) 
	{
		unordered_set<char> set;
    
		int i = 0, j = 0, n = s.size(), ans = 0;
    
		while( i<n && j<n)
		{
			if(set.find(s[j]) == set.end()) //If the character does not in the set
			{
				set.insert(s[j++]); //Insert the character in set and update the j counter
				ans = max(ans, j-i); //Check if the new distance is longer than the current answer
			}
			else
			{
				set.erase(s[i++]); 
				/*If character does exist in the set, ie. it is a repeated character, 
				we update the left side counter i, and continue with the checking for substring. */
			}
		}
    
		return ans;
	}
};

// 自己寫的, time complexity O(n)
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (!s.size()) return 0;
        int max_len {0};
        unordered_set<char> stored;
        int l {0};
        for (int r = 0; r < s.size(); r++){
            while (stored.find(s[r]) != stored.end()){
                stored.erase(s[l++]);
            }
            stored.insert(s[r]);
            max_len = max(max_len, r - l + 1);
        }
        return max_len;
    }
};
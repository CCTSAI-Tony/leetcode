// This might be an example of a pattern to keep in mind while solving sliding window problems with optimisation (min/max).

// One can see that we need to keep a count of the element which occurs the maximum times in a window, 
// and keep extending the window till the elements within the window except the one with maximum count are <= k. 
// The moment we exceed k, start should be incremented, and max count should be updated for the new window.

// This is intuitive and correctly solves the problem, however this will give TLE. 
// The insight/trick here is that max count within a window does not actually need to be updated every time start is updated, because:

// The largest window possible (after the present window) will always have greater than the present max count of elements in it, 
// so if we just update the total count of elements while incrementing start, and not the max count, we will still get the correct answer
// I do think this is difficult to come up with spontaneously in an interview, hence the idea can be memorized as a pattern in sliding window problems.

// time complexity O(n)
// even though we s[start]--, didn't resolve end - start + 1 - max_count_in_window > k, we don't care, cause it doesn't change the max_len answer
// We only need to update max_count_in_window for end, until we find end's character count bigger then preveios most frequent char,
// at that point, max_len may be increased
class Solution {
public:
    int characterReplacement(string s, int k) {
        int end = 0;
        int start = 0;
        
        int max_len = 0;
        int max_count_in_window = 0;
        
        unordered_map<char,int> count;
        
        for(end = 0; end < s.size(); end++)
        {
            count[s[end]]++;
            max_count_in_window = max(count[s[end]], max_count_in_window);
            if(end - start + 1 - max_count_in_window > k) 
            {
                count[s[start]]--;
                start++;
            }
            max_len = max(max_len, end - start + 1);
        }
        
        return max_len;
    }
};

// lamda expression
auto key_selector = [](auto pair){return pair.first;};
auto value_selector = [](auto pair){return pair.second;};
vector<Key> keys(map.size());
vector<Value> values(map.size());
transform(map.begin(), map.end(), keys.begin(), key_selector);
transform(map.begin(), map.end(), values.begin(), value_selector);

// for_each learning
// https://www.geeksforgeeks.org/for_each-loop-c/

// from python idea, is not good as above solution
class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> dic;
        int max_len {0}, l {0};
        for (int r = 0; r < s.size(); r++) {
            dic[s[r]]++;
            while (((r - l + 1) - max_map_value(dic)) > k){
                dic[s[l]]--;
                l++;
            }
            max_len = max(max_len, r-l+1);
        }
        return max_len;
    }
    
    int max_map_value(unordered_map<char, int>& map){
        auto pr = max_element(map.begin(), map.end(), [](const auto &x, const auto &y) {
                    return x.second < y.second; // depends on y
                });
        return pr->second;
    }
};
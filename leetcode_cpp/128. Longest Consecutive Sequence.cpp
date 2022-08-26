// time complexity O(n), 參照 pyrhon 解法
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> set;
        for (auto num: nums){
            set.insert(num);
        }
        int max_len {0};
        while (!set.empty()){
            int temp = *set.begin(); // 不能 temp = *--set.end() => 因為set.end() 是 forward iterators
            set.erase(temp);
            int l {0};
            int r {0};
            int i = temp + 1;
            while (set.find(i) != set.end()){
                set.erase(i);
                i += 1;
                r += 1;   
            }
            i = temp - 1;
            while (set.find(i) != set.end()){
                set.erase(i);
                i -= 1;
                l += 1;
            }
        max_len = max(max_len, l + 1 + r);
        }
        return max_len;
    }
};

// set.end() return type is a forward iterator, You cannot use decrement operator with forward iterators

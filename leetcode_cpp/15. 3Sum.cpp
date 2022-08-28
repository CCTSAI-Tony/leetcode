// time complexity O(n)
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 2; i++){
            if (i > 0 && nums[i] == nums[i-1]) continue;
            int l = i + 1, r = nums.size() -1;
            while (l < r){
                int s = nums[i] + nums[l] + nums[r];
                if (s < 0) l++;
                else if (s > 0) r--;
                else{
                    res.emplace_back(vector<int>{nums[i], nums[l], nums[r]});
                    while (l < r && nums[l] == nums[l + 1]) l++;
                    while (l < r && nums[r] == nums[r - 1]) r--;
                    l++, r--;
                }
            }
        }
        return res;
    }
};

// res.emplace_back(obj{}); => 這裡若要啟動move operator for &&obj, 要用到{} initilize list, 而不能obj()

// emplace_back calls whatever constructor matches the arguments you pass it. In this case you have chosen to pass Object{}, which matches the Object&& move constructor.

// When the description says, "no move or copy is performed", it means apart from the object construction that you specify. 
// If that construction happens to be a move or copy then of course it is performed.

// If you want emplace_back to use the no-args constructor then pass it no arguments: v.emplace_back().


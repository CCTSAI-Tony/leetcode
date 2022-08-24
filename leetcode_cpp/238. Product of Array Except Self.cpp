class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans(size(nums),1);
        for(int i = 1; i < size(nums); i++)                            // store prefix product
			ans[i] = ans[i-1] * nums[i-1];
        for(int i = size(nums)-1, suffixProd = 1; i >= 0; i--) {
            ans[i] *= suffixProd;                                      // multiply stored prefix product with suffix product
            suffixProd *= nums[i];                                     // update suffix product
        }
        return ans;
    }
};

// 重寫第二次, time complexity O(n)
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res(nums.size(), 1);
        for (int i = 1; i < nums.size(); i++){
            res[i] = res[i-1] * nums[i-1];
        }
        
        for (int i = nums.size() - 1, temp = 1; i >= 0; i--){ // i, temp type只能同一個 那就是int, 且只需要宣告一次
            res[i] *= temp;
            temp *= nums[i];
        }
        return res;
    }
};
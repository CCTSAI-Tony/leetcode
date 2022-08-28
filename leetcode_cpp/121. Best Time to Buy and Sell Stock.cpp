class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit {0}, min_value {INT_MAX};
        for (auto price: prices){
            min_value = min(min_value, price);
            profit = max(profit, price - min_value);
        }
        return profit;
    }
};
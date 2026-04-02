class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int lowest = INT_MAX;
        int profit = 0;
        for (auto const& price: prices) {
            lowest = std::min(lowest, price);
            profit = std::max(profit, price - lowest);
        }
        return profit;
    }
};

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;

        int l = 0;
        int r = 1;

        while (r < prices.size()) {
            profit = max(profit, prices[r] - prices[l]);
            if (prices[r] < prices[l]) {
                l = r;
            }
            r += 1;
        }
        return profit;
    }
};

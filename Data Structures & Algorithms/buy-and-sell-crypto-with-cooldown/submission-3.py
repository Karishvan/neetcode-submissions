class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * (len(prices)+1) for _ in range(len(prices) + 1)]

        for i in range(1, len(prices)+1):
            # if i == 2:
            #     print(dp)
            for j in range(1, len(prices)+1):
                # Buy on i, selling on j
                if j > i:
              

                    dp[i][j] = max(prices[j-1]-prices[i-1] + dp[i-1][i-2], dp[i-1][j])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # print(dp)
        return max(dp[len(prices)])
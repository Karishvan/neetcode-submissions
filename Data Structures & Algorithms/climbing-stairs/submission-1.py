class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i], many of possible ways to reach step i
        # dp [1] = 1
        # dp [2] = 2 (1 + 1, 2)
        # dp [3] = 3 (1 + 1 + 1, 1 + 2, 2 + 1), the number of ways u ccan climb 2 steps, + number of ways you can climb 1 step
        # dp [4] = 5 (1 + 1 + 1 + 1, 1 + 2 + 1, 2 + 1 + 1, 1 + 1 + 2, 2 + 2)
        dp = [1] * (n + 1)
        for i in range (2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
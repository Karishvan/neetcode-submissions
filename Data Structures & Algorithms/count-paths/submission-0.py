class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        print(dp)

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r + 1 < m and c + 1 < n:
                    dp[r][c] = dp[r + 1][c] + dp[r][c + 1]


        return dp[0][0]
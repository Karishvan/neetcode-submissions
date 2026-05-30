class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_idx = [0, 0]
        resLen = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(len(s)-1, -1, -1):
            for j in range (i, len(s)):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i + 1 > resLen:
                        resLen = j-i+1
                        res_idx = [i, j]
        
        return s[res_idx[0]: res_idx[1]+1]
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]

        for i in range (len(text1)):
            for j in range (len(text2)):
                dp_i = i+1
                dp_j = j+1
                if text1[i] == text2[j]:
                    dp[dp_i][dp_j] = 1 + dp[dp_i-1][dp_j-1]
                else:
                    dp[dp_i][dp_j] = max(dp[dp_i-1][dp_j], dp[dp_i][dp_j-1])
        
        return dp[len(text1)][len(text2)]
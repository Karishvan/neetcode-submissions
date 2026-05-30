class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range (len(s)):
            for word in wordDict:
                if dp[i]:
                    break
                if len(word) <= (i+1):
                    if i - len(word) < 0:
                        dp[i] = s[:i+1] == word
                    else:
                        dp[i] = dp[i-len(word)] and s[i+1-len(word):i+1] == word
        print(dp)
        return dp[len(s)-1]

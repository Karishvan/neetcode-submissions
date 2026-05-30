class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        num_of_each_char = {}
        l = 0
        maxf = 0
        for r in range (len(s)):
            num_of_each_char[s[r]] = 1 + num_of_each_char.get(s[r], 0)
            maxf = max(num_of_each_char[s[r]], maxf)
            
            

            while ((r-l + 1) - maxf > k):
                l += 1
                num_of_each_char[s[l-1]] -= 1
            max_len = max(r-l+1, max_len)
        
        return max_len

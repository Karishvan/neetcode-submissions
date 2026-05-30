class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        num_of_each_char = {}
        l = 0

        for r in range (len(s)):
            num_of_each_char[s[r]] = 1 + num_of_each_char.get(s[r], 0)
            num_of_diff_char = (r-l + 1) - max(num_of_each_char.values())
            
            

            while (num_of_diff_char > k):
                l += 1
                num_of_each_char[s[l-1]] -= 1
                num_of_diff_char = (r-l + 1) - max(num_of_each_char.values())
            max_len = max(r-l+1, max_len)
        
        return max_len

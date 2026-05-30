class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map_of_t = {}
        for c in t:
            num = map_of_t.get(c, 0)
            map_of_t[c] = num + 1

        map_of_s = {}
        l = 0
        have, need = 0, len(map_of_t)
        res = [-1, -1]
        min_len = float('inf')
        for r in range(len(s)):
            count_of_char = map_of_s.get(s[r], 0)
            map_of_s[s[r]] = count_of_char + 1
            if s[r] in map_of_t and map_of_s[s[r]] == map_of_t[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < min_len:
                    res = [l, r+1]
                    min_len = r-l + 1
                if s[l] in map_of_t and map_of_s[s[l]] == map_of_t[s[l]]:
                    have -= 1
                map_of_s[s[l]] -= 1
                l += 1
        return s[res[0] : res[1]]
                

        
        

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map_of_t = {}
        for c in t:
            num = map_of_t.get(c, 0)
            map_of_t[c] = num + 1
        
        def isSubMap(map_of_s, map_of_t):
            for k, v in map_of_t.items():
                num = map_of_s.get(k, 0)
                if num < v:
                    return False

            return True

        map_of_s = {}
        l = 0
        res = ""
        cur = ""
        min_len = float('inf')
        for r in range(len(s)):
            cur += s[r]
            count_of_char = map_of_s.get(s[r], 0)
            map_of_s[s[r]] = count_of_char + 1
            #print(cur)
            while l < len(s) and isSubMap(map_of_s, map_of_t):
                #print("IN WHILE LOOP")
                #print(map_of_s)
                if r - l + 1 < min_len:
                    res = cur[l:]
                    min_len = r-l + 1
                map_of_s[s[l]] -= 1
                l += 1
        return res
                

        
        

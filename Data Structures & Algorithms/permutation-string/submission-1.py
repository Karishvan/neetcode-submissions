class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False



        sub_size = len(s1)
        # substring is from l(inclusive) to r (non-inclusive)
        l = 0
        #fill up s1_hashmap
        s1_map = {}
        s2_map = {}
        for c in s1:
            s1_map[c] = s1_map.get(c, 0) + 1
        
        for r in range(0, sub_size):
            s2_map[s2[r]] = s2_map.get(s2[r], 0) + 1
        if s1_map == s2_map:
            return True
        for r in range (sub_size, len(s2)):
            prev_idx = r - sub_size
            s2_map[s2[prev_idx]] -= 1
            if s2_map[s2[prev_idx]] == 0:
                del s2_map[s2[prev_idx]]
            s2_map[s2[r]] = s2_map.get(s2[r], 0) + 1

            if s1_map == s2_map:
                return True
        
        return False



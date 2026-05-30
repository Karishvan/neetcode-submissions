class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        # sSet = set(s)
        # uniqueChars = len(sSet)
        length = 0
        seen = set()

        # if (len(s) == 0):
        #     return 0

        for r in range(0,len(s)):
            # sSet = set(s[l:r])
            # uniqueChars = len(sSet)
            #print(l,r)
            #print(s[l:r])
            #print("UNIQ", uniqueChars)
            #print(len(s[l:r]))

            while (l <= r and s[r] in seen):
                seen.remove(s[l])
                l+=1
                # sSet = set(s[l:r])
                # uniqueChars = len(sSet)
                print(l, "UPDATING L")
            length = max(length, (r-l)+1)
            seen.add(s[r])
            #print("F", length)
        
        return length
            


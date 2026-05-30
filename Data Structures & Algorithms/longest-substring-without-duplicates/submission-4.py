class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        # sSet = set(s)
        # uniqueChars = len(sSet)
        length = 1

        if (len(s) == 0):
            return 0

        for r in range(1,len(s)+1):
            sSet = set(s[l:r])
            uniqueChars = len(sSet)
            #print(l,r)
            #print(s[l:r])
            #print("UNIQ", uniqueChars)
            #print(len(s[l:r]))
            while (l <= r and uniqueChars != len(s[l:r])):
                l+=1
                sSet = set(s[l:r])
                uniqueChars = len(sSet)
                print(l, "UPDATING L")
            length = max(length, (r-l))
            #print("F", length)
        
        return length
            


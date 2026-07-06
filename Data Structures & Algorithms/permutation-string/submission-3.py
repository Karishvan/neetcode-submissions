class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False



        sub_size = len(s1)
        # substring is from l(inclusive) to r (non-inclusive)
        l = 0
        s1_count = [0] * 26
        s2_count = [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1 
            s2_count[ord(s2[i]) - ord('a')] += 1
        
             
        matches = 0
        for i in range (len(s1_count)):
            if s1_count[i] == s2_count[i]:
                matches += 1
        

        print("s2",s2_count)
        for r in range (sub_size, len(s2)):
            if matches == 26:
                return True
            prev_idx = r - sub_size
            prev_idx = ord(s2[prev_idx]) - ord('a')
            if s2_count[prev_idx] == s1_count[prev_idx]:
              
                matches -= 1
            s2_count[prev_idx] -= 1
            if s2_count[prev_idx] == s1_count[prev_idx]:
                matches += 1

            current_idx = ord(s2[r]) - ord('a')
            
            if s2_count[current_idx] == s1_count[current_idx]:
                matches -= 1
            s2_count[current_idx] += 1
            if s2_count[current_idx] == s1_count[current_idx]:
                
                matches += 1
            # print("s1",s1_count)
            # print("s2",s2_count)

            # print(matches)
        if matches == 26:
                return True
        return False



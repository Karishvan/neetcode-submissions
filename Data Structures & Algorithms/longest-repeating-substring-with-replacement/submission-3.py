class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        curr_len = 0
        num_of_diff_char = 0
        l = 0
        num_of_each_char = [0] * 26 #26 upper characters
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for r in range (len(s)):
            curr_len += 1
            num_of_each_char[alphabet.index(s[r])] += 1
            sorted_char = sorted(num_of_each_char, reverse = True)
            num_of_diff_char = sum(sorted_char[1:])
            #print(num_of_diff_char)
            
            

            while (num_of_diff_char > k):
                #print("L IS: ", l, "R IS: ", r)
                l += 1
                curr_len -= 1
                num_of_each_char[alphabet.index(s[l-1])] -= 1
                sorted_char = sorted(num_of_each_char, reverse = True)
                num_of_diff_char = sum(sorted_char[1:])
            max_len = max(curr_len, max_len)
        
        return max_len

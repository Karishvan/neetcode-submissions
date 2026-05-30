class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_seq = 0

        for num in nums:
            if num-1 not in num_set:
                #num is the beginning of sequence
                cur_seq = 1
                nxt = num+1
                while nxt in num_set:
                    nxt += 1
                    cur_seq += 1
                max_seq = max(cur_seq, max_seq)
        
        return max_seq

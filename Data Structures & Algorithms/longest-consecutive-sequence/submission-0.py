class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        sequences_starting = []

        for i in range(len(nums)):
            if (not nums[i]-1 in nums_set):
                sequences_starting.append(nums[i])

        #print(sequences_starting)
        
        longest = 0
        for j in range(len(sequences_starting)):
            counter = 1
            current_num = sequences_starting[j]
            while (current_num+1 in nums_set):
                counter +=1
                current_num +=1
            if (counter > longest):
                longest = counter
        

        return longest

        
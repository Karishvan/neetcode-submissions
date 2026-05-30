class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        #sequences_starting = []

        longest = 0
        for i in range(len(nums)):
            if (not nums[i]-1 in nums_set):
                #sequences_starting.append(nums[i])
                counter = 1
                current_num = nums[i]
                while (current_num+1 in nums_set):
                    counter +=1
                    current_num +=1
                if (counter > longest):
                    longest = counter

        #print(sequences_starting)
        
        
        #for j in range(len(sequences_starting)):
            
        

        return longest

        
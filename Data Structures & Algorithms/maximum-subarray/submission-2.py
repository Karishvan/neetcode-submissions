class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
       
        for r in range (len(nums)):
            current_sum += nums[r]
            max_sum = max(current_sum, max_sum)            
            if current_sum < 0:
                current_sum = 0
            
        return max_sum
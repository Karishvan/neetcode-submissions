class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        l = 0
        # if len(nums) == 1:
        #     return max_sum
        for r in range (len(nums)):
            current_sum += nums[r]
            max_sum = max(current_sum, max_sum)            
            if current_sum <= 0:
                l = r
                current_sum = 0
            
        return max_sum
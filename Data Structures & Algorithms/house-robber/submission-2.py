class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i] relies on the max value u get between robbing [i-2 or i-3]
        dp = [0] * len(nums)
        for i in range (min(2, len(nums))):
            dp[i] = nums[i]
        
        for i in range (2, len(nums)):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
            print(dp[i])
        return max(dp[len(nums)-1], dp[len(nums)-2])

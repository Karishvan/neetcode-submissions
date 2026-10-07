class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target_sum = sum(nums) // 2

        dp = [[False] * (target_sum+1) for _ in range(len(nums)+1)]
        for k in range(len(nums)+1):
            dp[k][0] = True

        for i in range(1, len(nums)+1):
            for j in range(0, target_sum+1):
                # Target sum is j
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(nums)][target_sum]
        
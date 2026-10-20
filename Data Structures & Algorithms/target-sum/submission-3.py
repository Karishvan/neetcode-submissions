class Solution:
    """
    different permutations
    -2, 2, 2 != 2, -2, 2

    can add or subtract

    want to return the number of permutations
    [4, 2, 3]
    sum 0
    choice, +4 or -4
    sum = 4 or -4
    choice, +2 or -2
    
    choice, +3 or -3

    [0, 0, 0, 0, 0, 0, 0, 0, 1]
    0, 0
    
    """
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        dp[0][0] = 1 # 1 way using the first 0 elements to sum up to 0

        for i in range(len(nums)):
            for cur_sum, count in dp[i].items():
                dp[i+1][cur_sum - nums[i]] += count
                dp[i+1][cur_sum + nums[i]] += count
        
        return dp[len(nums)][target]

        
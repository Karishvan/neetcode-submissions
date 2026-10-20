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
        cache = {}
        def dfs(i, cur_sum):
            if i == len(nums):
                return 1 if target == cur_sum else 0
            if (i, cur_sum) in cache:
                return cache[(i, cur_sum)]
            pos_choice = cur_sum + nums[i]
            neg_choice = cur_sum - nums[i]
            pos_total = dfs(i+1, pos_choice)
            neg_total = dfs(i+1, neg_choice)
            cache[(i, cur_sum)] = pos_total + neg_total
            return cache[(i, cur_sum)]

        return dfs(0, 0)
        
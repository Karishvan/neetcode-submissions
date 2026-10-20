class Solution:
     
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1] * (amount+1) for i in range(len(coins) + 1)]
        def recurse(i, target):
            if i == len(coins):
                dp[i][target] = 1 if target == 0 else 0
                return dp[i][target]
            take = 0
            if coins[i] <= target:
                if dp[i][target - coins[i]] != -1:
                    take = dp[i][target- coins[i]]
                else:
                    take = recurse(i, target-coins[i])
            skip = 0
            if dp[i+1][target] == -1:
                skip = recurse(i+1, target)
            else:
                skip = dp[i+1][target]
            dp[i][target] = take + skip
            return take + skip
        
        return recurse(0, amount)
            
        """
      0 1 2 3 4
   0 [0 0 0 0 0 ]
   1 [0 1 1 1 1 ]
   2 [0 1 2 2 3 ]
   3 [0 1 2 3 4 ]
   """
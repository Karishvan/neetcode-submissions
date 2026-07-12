class Solution {
    fun minCostClimbingStairs(cost: IntArray): Int {
        val dp = IntArray(cost.size+1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for (i in 2..cost.size) {
            if (i == cost.size) {
                dp[i] = min(dp[i-2], dp[i-1])
            } else {
                dp[i] = min(dp[i-2] + cost[i], dp[i-1] + cost[i])
            }
        }
        return dp[cost.size]
    }
}

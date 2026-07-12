class Solution {
    fun minCostClimbingStairs(cost: IntArray): Int {
        var first = cost[0]
        var second = cost[1]
        for (i in 2..cost.size) {
            var temp = -1
            if (i == cost.size) {
                temp = min(first, second)
            } else {
                temp = min(first + cost[i], second + cost[i])
            }
            first = second
            second = temp

        }
        return second
    }
}

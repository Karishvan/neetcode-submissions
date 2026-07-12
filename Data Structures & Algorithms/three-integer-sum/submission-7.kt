class Solution {
    fun threeSum(nums: IntArray): List<List<Int>> {
        nums.sort()
        val res = mutableListOf<List<Int>>()

        for (i in 0..nums.size-1) {
            if (i >= 1 && nums[i] == nums[i-1]) {
                continue
            }
            var l = i + 1
            var r = nums.size-1
            val target = 0 - nums[i]
            while (l < r) {
                
                if (nums[l] + nums[r] < target) {
                    l++
                } else if (nums[l] + nums[r] > target) {
                    r--
                } else {
                    
                    res.add(listOf(nums[i], nums[l], nums[r]))
                    
                    l++
                    while (l <= r && nums[l] == nums[l-1]) {
                        l++
                    }
                }
            }
        }
        return res
    }
}

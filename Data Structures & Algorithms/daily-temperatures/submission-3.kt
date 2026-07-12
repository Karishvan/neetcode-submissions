class Solution {
    fun dailyTemperatures(temperatures: IntArray): IntArray {
        val stack = ArrayDeque<Int>()
        val res = MutableList(temperatures.size) {0}

        for (i in 0..temperatures.size-1) {
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.last()]) {
                
                val prev_idx = stack.removeLast()
                res[prev_idx] = i - prev_idx
            }
            stack.addLast(i)
        }
        return res.toIntArray()
    }
}

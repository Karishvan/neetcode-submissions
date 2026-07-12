class Solution {
    fun checkInclusion(s1: String, s2: String): Boolean {
        if (s1.length > s2.length) {
            return false
        }
        
        val s1Count = MutableList(26) {0}
        val s2Count = MutableList(26) {0}
        var matches = 0
        
        for (i in 0..s1.length-1) {
            s1Count[s1[i] - 'a']++
            s2Count[s2[i] - 'a']++
        }
        for (i in 0..s1Count.size-1) {
            if (s1Count[i] == s2Count[i]) {
                matches++
            }
        }
    
        
        var l = 1
        for (r in s1.length..s2.length-1) {
            
            if (matches == 26) {
                return true
            }
            val prev_idx = s2[l-1] - 'a'
            s2Count[prev_idx]--
            if (s2Count[prev_idx] + 1 == s1Count[prev_idx]) {
                matches -= 1
            }
            if (s2Count[prev_idx] == s1Count[prev_idx]) {
                matches += 1
            }
            val next_idx = s2[r] - 'a'
            s2Count[next_idx]++
            if (s2Count[next_idx] == s1Count[next_idx]) {
                matches += 1
            }
            if (s2Count[next_idx]-1 == s1Count[next_idx]) {
                matches -= 1
            }
            l++
        }
        if (matches == 26) {
            return true
        }
        return false
        
    }
}

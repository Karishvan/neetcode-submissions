class Solution {
    fun checkInclusion(s1: String, s2: String): Boolean {
        if (s1.length > s2.length) {
            return false
        }
        
        val s1Count = IntArray(26)
        val s2Count = IntArray(26)
        var matches = 0
        
        for (i in s1.indices) {
            s1Count[s1[i] - 'a']++
            s2Count[s2[i] - 'a']++
        }
        for (i in s1Count.indices) {
            if (s1Count[i] == s2Count[i]) {
                matches++
            }
        }
    
        
        var l = 0
        for (r in s1.length until s2.length) {
            
            if (matches == 26) {
                return true
            }
            val prev_idx = s2[l] - 'a'
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
        return matches == 26
        
    }
}

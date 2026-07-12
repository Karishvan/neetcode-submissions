class Solution {
    fun groupAnagrams(strs: Array<String>): List<List<String>> {
        val res = mutableListOf<List<String>>()
        val words_to_groups = HashMap<HashMap<Char, Int>, List<String>>()

        for (item: String in strs) {
            val char_counter = HashMap<Char, Int>()
            for (c in item) {
                char_counter[c] = char_counter.getOrDefault(c, 0) + 1
            }
            words_to_groups[char_counter] = words_to_groups.getOrDefault(char_counter, emptyList()) + item
            
        }
        for ((key, value) in words_to_groups) {
            res.add(value)
        }
        return res
    }
}

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> wordsPerAnagram = new HashMap<>();

        for (String elem: strs){
            int [] count = new int[26];
            for (char c: elem.toCharArray()){
                count[c - 'a'] ++;
            }
            
            String key = Arrays.toString(count);
            if (!wordsPerAnagram.containsKey(key)){
                wordsPerAnagram.put(key, new ArrayList<>());
            } 
            wordsPerAnagram.get(key).add(elem);
        }

        //System.out.println((wordsPerAnagram.values()));
        return new ArrayList<>(wordsPerAnagram.values());
    }
}

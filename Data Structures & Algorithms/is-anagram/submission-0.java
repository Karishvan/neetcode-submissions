class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> numOfCharsS = new HashMap<>();
        Map<Character, Integer> numOfCharsT = new HashMap<>();
        if (s.length() != t.length()){
            return false;
        }
        for (int i = 0; i < s.length(); i++){
            if (!(numOfCharsS.containsKey(s.charAt(i)))){
                numOfCharsS.put(s.charAt(i), 1);
            } else {
                numOfCharsS.put(s.charAt(i), numOfCharsS.get(s.charAt(i)) + 1);
            }

            if (!(numOfCharsT.containsKey(t.charAt(i)))){
                numOfCharsT.put(t.charAt(i), 1);
            } else {
                numOfCharsT.put(t.charAt(i), numOfCharsT.get(t.charAt(i)) + 1);
            }
            
        }
        for(Character elem: numOfCharsS.keySet()){
            if (numOfCharsS.get(elem) != numOfCharsT.get(elem)){
                return false;
            }
        }
        return true;
    }
}

class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        return isPal(s);
       
    }
    public boolean isPal(String s){
        if (s.length() <= 1){
            return true;
        }
        int lastChar = s.length()-1;
        if (!((s.charAt(0) >= 'a' && s.charAt(0) <= 'z') || (s.charAt(0) >= '0' && s.charAt(0) <= '9'))){
            return isPal(s.substring(1));
        }
         if (!((s.charAt(lastChar) >= 'a' && s.charAt(lastChar) <= 'z') || (s.charAt(lastChar) >= '0' && s.charAt(lastChar) <= '9'))){
            return isPal(s.substring(0, lastChar));
        }
        if (s.charAt(0)!= s.charAt(lastChar)){
            return false;
        } else {
            return isPal(s.substring(1, lastChar));
        }
    }
}

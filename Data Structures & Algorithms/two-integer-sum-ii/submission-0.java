class Solution {
    public int[] twoSum(int[] numbers, int target) {
        for (int i = 0; i < numbers.length; i++){
            int bot = i;
            int top = numbers.length-1;
            int conjugate = target - numbers[i];
            while (bot <= top){
                int mid = (bot + top)/2;
                if (numbers[mid] == conjugate){
                    return new int[]{i+1, mid+1};
                } else if (numbers[mid] > conjugate){
                    top = mid-1;
                } else {
                    bot = mid+1;
                }
            }
            
        }
        return new int[]{-1,-1};
    }
}

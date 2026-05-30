class Solution {
    public int search(int[] nums, int target) {
        int bot = 0;
        int top = nums.length-1;
        
        while (bot <= top) {
            int mid = (top + bot) / 2;

            if (nums[mid] == target){
                return mid;
            } else if (nums[mid] > target){
                top = mid-1;
            } else {
                bot = mid+1;
            }
        }
        return -1;
    }
}

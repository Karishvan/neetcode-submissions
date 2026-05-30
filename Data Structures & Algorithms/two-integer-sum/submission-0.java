class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numToIndex = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            int conjugate = target - nums[i];
            if (numToIndex.containsKey(conjugate)){
                return new int[] {numToIndex.get(conjugate), i};
            } else {
                numToIndex.put(nums[i], i);
            }
        }
        return new int[]{-1,-1};

    }
}

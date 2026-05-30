class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> numsToFrequency = new HashMap<>();
        List<Integer>[] freq = new List[nums.length + 1];

        for (int i = 0; i < freq.length; i ++){
            freq[i] = new ArrayList<>();
        }
        for (int i = 0; i < nums.length; i++){
            if (numsToFrequency.containsKey(nums[i])){
                numsToFrequency.put(nums[i],numsToFrequency.get(nums[i])+1);
            } else {
                numsToFrequency.put(nums[i], 1);
            }
        }
        for (int key: numsToFrequency.keySet()){
            freq[numsToFrequency.get(key)].add(key);
        }
        int [] res = new int[k];
        int count = 0;
        for (int i = freq.length-1; i >= 0; i--){
            for (int n: freq[i]){
                res[count++] = n;
                if (count == k){
                    return res;
                }
            }
        }
        return res;

    }
}


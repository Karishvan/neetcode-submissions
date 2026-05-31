class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = res ^ num
        regular_xor = 0
        for i in range(len(nums)+1):
            regular_xor = regular_xor ^ i
    
        return regular_xor ^ res
            


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        min_val, max_val = 1, 1

        for num in nums:
            if num == 0:

                min_val, max_val = 1,1
            else:
                tmp = max_val * num
                max_val = max(tmp, num, min_val * num)
                min_val = min(tmp, num, min_val * num)
                res = max(max_val, res)
                    
        
        return res
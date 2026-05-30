class Solution:
    def rob(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return nums[0]
        return max(self.houseRobber1(1, len(nums), nums), self.houseRobber1(0, len(nums)-1, nums))

    def houseRobber1(self, start, end ,nums):
        rob0, rob1 = 0,0
        for i in range(start, end):
            tmp = max(rob0 + nums[i], rob1)
            rob0 = rob1
            rob1 = tmp
        return rob1
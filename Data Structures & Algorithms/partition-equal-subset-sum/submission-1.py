class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = {0}
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2

        for i in range(len(nums)):
            nextDP = set()
            for n in sums:
                nextDP.add(nums[i] + n)
                nextDP.add(n)
            sums = nextDP

        return True if target in sums else False


        
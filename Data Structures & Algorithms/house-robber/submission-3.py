class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i] relies on the max value u get between robbing [i-2 or i-3]
        rob0, rob1 = 0,0
        for n in nums:
            #either rob 0 + n, or rob1 (rob1 and n are adjacent cant pick both)
            tmp = max(rob0 + n, rob1)
            rob0 = rob1
            rob1 = tmp
        return rob1

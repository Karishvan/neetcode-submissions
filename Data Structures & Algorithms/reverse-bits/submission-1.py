class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(31, -1, -1):
            bit = n & 1
            n = n >> 1
            bit = bit << i
            res = res | bit
    
        return res

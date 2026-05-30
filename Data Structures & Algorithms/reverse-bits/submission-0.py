class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = n % 2
            n = n >> 1
            #print(n)
            res = res << 1
            res += bit
            print(res)
        return res

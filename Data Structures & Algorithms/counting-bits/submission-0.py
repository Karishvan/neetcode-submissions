class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOnes(num):
            res = 0
            while num:
                res += 1
                num = num & (num-1)
            return res
        output = [1] * (n+1)
        for i in range(n+1):
            output[i] = countOnes(i)
        
        return output
    
        
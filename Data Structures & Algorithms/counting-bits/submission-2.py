class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n+1)
        for i in range(n+1):
            if i % 2 == 0:
                output[i] = output[i >> 1]
            else:
                output[i] = 1 + output[i >> 1]
        
        return output
    
        
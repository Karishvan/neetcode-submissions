class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        position = 31
        while position >= 0:
            if n >= 2**position:
                print(position)
                n -= 2**position
                count +=1
            position -= 1
        
        return count
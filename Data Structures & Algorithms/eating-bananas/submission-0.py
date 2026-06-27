import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low , high = 1, max(piles)
        k = -1
        while (low <= high):
            iteration_k = (low + high) // 2

            iteration_h = 0
            for bananas in piles:
                iteration_h += math.ceil(bananas / iteration_k)
            
            if iteration_h <= h:
                k = iteration_k
                high = iteration_k - 1
            elif iteration_h > h:
                low = iteration_k + 1
        
        return k
            


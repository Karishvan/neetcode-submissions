class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            elem1 = heapq.heappop_max(stones)
            elem2 = heapq.heappop_max(stones)
            if elem1 > elem2:
                heapq.heappush_max(stones, elem1-elem2)
        
        return stones[0] if stones else 0

                
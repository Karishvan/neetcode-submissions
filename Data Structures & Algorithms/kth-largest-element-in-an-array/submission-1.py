class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for i in range (k):
            heapq.heappush(min_heap, nums[i])
            # print(nums[i])
        for j in range(i+1,len(nums)):
            # print("i")
            # print(i)
            heapq.heappushpop(min_heap, nums[j])
        # print(min_heap)
        return min_heap[0]
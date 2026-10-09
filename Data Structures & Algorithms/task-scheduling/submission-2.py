class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        cooldowns = deque()

        
        heap = [value for value in counts.values()]
        heapq.heapify_max(heap)
        time = 0
        # hasCooldowns = True
        
        while heap or cooldowns:
            time += 1
            if heap:
                occurence = heapq.heappop_max(heap) - 1
                if occurence:
                    cooldowns.append([occurence, time + n])
                
            if cooldowns and cooldowns[0][1] == time:
                heapq.heappush_max(heap, cooldowns.popleft()[0])

        return time
            

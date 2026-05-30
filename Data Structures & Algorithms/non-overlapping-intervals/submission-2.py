class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        res = 0
        prevEnd = intervals[0][1]
        print(intervals)
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] < prevEnd:
                res += 1
                prevEnd = min(prevEnd, curr[1])
                continue
            prevEnd = curr[1]
        
        return res
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Iterate through the intervals
        # if end interval > start interval of prev
        # merge these 2 interrvals, add merged interval to result, update our prev interval
        # else just add to result

        intervals.sort()
        print(intervals)
        res = []
        prev_interval = intervals[0]
        for (i, interval) in enumerate(intervals):
            start, end = interval
            if i > 0 and start <= prev_interval[1]:
                #merge the two intervals
                print("MERGING")
                interval = [prev_interval[0], max(prev_interval[1], end)]
                res.pop()
            res.append(interval)
            prev_interval = interval
        return res
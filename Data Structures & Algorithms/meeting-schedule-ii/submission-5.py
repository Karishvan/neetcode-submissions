"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts.sort()
        ends.sort()
        start_ptr = 0
        end_ptr = 0

        res = 0
        count = 0
        while start_ptr < len(intervals) and end_ptr < len(intervals):
            if ends[end_ptr] <= starts[start_ptr]:
                count -= 1
                end_ptr += 1
            else:
                count += 1
                start_ptr += 1
            
            res = max(count, res)
        
        return res

            
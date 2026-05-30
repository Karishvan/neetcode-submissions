"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 1
        intervals.sort(key=lambda x: x.start)
        for interval in intervals:
            print('(', interval.start, ',', interval.end, ')', end = " ")
        print()
        if not intervals:
            return 0
        # Each element in room is the last ending value of a room
        rooms = [intervals[0].end]
        found_spot = False
        for i in range (1, len(intervals)):
            print(rooms)
            for j in range(len(rooms)):
                lastEnd = rooms[j]
                if not intervals[i].start < lastEnd:
                    found_spot = True
                    rooms[j] = intervals[i].end
                    break
            if not found_spot:
                res += 1
                rooms.append(intervals[i].end)
            found_spot = False

        return res
            
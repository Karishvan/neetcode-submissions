class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        found_spot = False
        
        for cur_start, cur_end in intervals:
            new_start, new_end = newInterval
            if not (new_end < cur_start or new_start > cur_end):
                # overlapping
                print(new_start)
                newInterval_start = min(new_start, cur_start)
                newInterval_end = max(new_end, cur_end)
                newInterval = [newInterval_start, newInterval_end]
                print(newInterval)
            elif not found_spot and new_end < cur_end:
                found_spot = True
                res.append(newInterval)
                res.append([cur_start, cur_end])
            else:
                res.append([cur_start, cur_end])
        
        if not found_spot:
            res.append(newInterval)
            


        return res
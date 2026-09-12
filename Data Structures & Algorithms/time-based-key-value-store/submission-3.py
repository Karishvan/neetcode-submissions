class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.time_map[key]
        l, r = 0, len(vals)-1
        res = -1
        while (l <= r):
            mid = (l + r) // 2
            # print(vals)
            # print(l, r)
            if vals[mid][1] == timestamp:
                return vals[mid][0]
            if vals[mid][1] > timestamp:
                r = mid-1
            if vals[mid][1] < timestamp:
                res = mid
                l = mid+1
        if res >= 0:
            return vals[res][0]
        else:
            return ""
            
        
    #Because set is strictly increasing, we can store time_map as a hash map with key as key, and value as a list of tuples containing (value, timestamp). Then for get we can do a simple binary search starting at the middle of the list and taking the largest prev_timestamp > timestamp
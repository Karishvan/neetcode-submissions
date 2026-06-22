class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = []
        num_to_idx = {}
        for i, temp in enumerate(temperatures):
           
            if not s or temp <= s[-1][0]:
                s.append((temp, i))
            elif temp > s[-1][0]:
                while s and temp > s[-1][0]:
                    num, idx = s.pop()
                    res[idx] = i - idx
                   
                s.append((temp, i))
        
        return res
            


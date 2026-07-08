class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # index 0 is position, index 1 is speed
        pos_speed = list(zip(position, speed))
        pos_speed.sort(key=lambda x: x[0], reverse=True)
        
        res = len(position)
        time = [-1.0] * res
        for i in range(len(pos_speed)):
            pos, sp = pos_speed[i]
            time[i] = (target - pos) / sp

        stack = [time[-1]]
        for i in range(len(time)-2, -1, -1):
            while stack and time[i] >= stack[-1]:
                stack.pop()
                res -= 1
            stack.append(time[i])
        return res

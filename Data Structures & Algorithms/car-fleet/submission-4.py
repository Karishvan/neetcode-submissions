class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # index 0 is position, index 1 is speed
        pos_speed = list(zip(position, speed))
        pos_speed.sort(key=lambda x: x[0], reverse=True)
        
        stack = []
        
        for i in range(len(pos_speed)):
            pos, sp = pos_speed[i]
            time = (target - pos) / sp
            if stack and time <= stack[-1]:
                continue
            stack.append(time)

        return len(stack)

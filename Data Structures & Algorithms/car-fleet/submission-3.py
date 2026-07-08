class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # index 0 is position, index 1 is speed
        pos_speed = list(zip(position, speed))
        pos_speed.sort(key=lambda x: x[0], reverse=True)
        
        stack = []
        
        for i in range(len(pos_speed)):
            pos, sp = pos_speed[i]
            stack.append((target - pos) / sp) 
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

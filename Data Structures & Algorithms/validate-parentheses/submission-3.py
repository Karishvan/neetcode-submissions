class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        closed_to_open = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c not in closed_to_open:
                stack.append(c)
            else:
                if (len(stack) == 0 or stack.pop() != closed_to_open[c]):
                    return False
        
        return len(stack) == 0
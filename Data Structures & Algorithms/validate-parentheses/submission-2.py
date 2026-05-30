class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        open_brackets = ['(', '{', '[']
        closed_to_open = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in open_brackets:
                stack.append(c)
            else:
                if (len(stack) == 0 or stack.pop() != closed_to_open[c]):
                    return False
        
        return len(stack) == 0
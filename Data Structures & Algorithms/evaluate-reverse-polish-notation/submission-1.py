class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        s = []

        for token in tokens:
            if token not in operators:
                s.append(token)
            else:
                num2 = int(s.pop())
                num1 = int(s.pop())
                if token == '+':
                    s.append(num1 + num2)
                elif token == '-':
                    s.append(num1 - num2)
                elif token == '*':
                    s.append(num1 * num2)
                else:
                    s.append(num1 / num2)
        
        return int(s.pop())

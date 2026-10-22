class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(num_open, num_closed, path):
            if num_open == num_closed and num_closed == n:
                res.append(path[:])
                return
            
            if num_open < n:
                path.append('(')
                backtrack(num_open + 1, num_closed, path)
                path.pop()
            if num_closed < num_open:
                path.append(')')
                backtrack(num_open, num_closed + 1, path)
                path.pop()
        
        
        backtrack(0, 0, [])
        for i in range(len(res)):
            res[i] = "".join(res[i])
        return res
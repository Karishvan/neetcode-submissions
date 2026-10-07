class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(index, path, summation):
            # Base case
            
            if summation == target:
                res.append(path[:])
                return
            elif index >= len(candidates) or summation > target:
                return
            
            

            # Choice
            path.append(candidates[index])
            backtrack(index+1, path, summation + candidates[index])
            
            
            # Undo choice
            path.pop()
            index += 1
            while index < len(candidates) and candidates[index] == candidates[index-1]:
                index += 1
            backtrack(index, path, summation)
        backtrack(0, [], 0)
        return res
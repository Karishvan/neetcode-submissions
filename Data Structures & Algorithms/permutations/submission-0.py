class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path_set, path):
            #Base Case
            if len(path) == len(nums):
                res.append(path[:])
                return
            #Decisions
            for num in nums:
                if num not in path_set:
                    path_set.add(num)
                    path.append(num)
                    backtrack(path_set, path)
                    #Undo Decision
                    path_set.remove(num)
                    path.pop()
        backtrack(set(), [])
        return res


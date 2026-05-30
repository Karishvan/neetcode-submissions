# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        max_sum_at_each_root = {}
        
        
        def dfs(root):
            nonlocal max_sum
            if not root:
                return 0
            left_sum = dfs(root.left)
            right_sum = dfs(root.right)
            max_sum_at_each_root[root] = max(root.val, root.val + left_sum, root.val + right_sum)
            print(max_sum)
            max_sum = max(max_sum_at_each_root[root], max_sum, root.val + left_sum + right_sum)
            return max_sum_at_each_root[root]
            
        
        dfs(root)
        print(max_sum)
        return max_sum

        
        

            
            
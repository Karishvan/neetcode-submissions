# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
       

        def dfs(max_root, root):
            if not root:
                return 0
            if root.val >= max_root:
                res = 1
            else:
                res = 0
            max_root = max(root.val, max_root)
            res += dfs(max_root, root.left)
            res += dfs(max_root, root.right)
            return res
        return dfs(root.val, root)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        maxx = float('-inf')

        def dfs(max_root, root):
            nonlocal res
            if not root:
                return
            if root.val >= max_root:
                res += 1
                max_root = max(root.val, max_root)
            dfs(max_root, root.left)
            dfs(max_root, root.right)
        dfs(maxx, root)
        return res
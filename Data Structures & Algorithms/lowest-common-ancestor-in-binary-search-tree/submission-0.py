# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Run dfs for p and q, find its level
        #run dfs on min level, see if u can find other element
        # if not, go up one level, continue till result
        # use parent variable to find level above
        # def dfs(root, p, level):
        #     if (p.val < root):
        #         self.dfs(root.left, p, level+1)
        #     elif (p.val > root):
        #         self.dfs(root.right, p, level+1)
        #     else:
        #         return level
        if (p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
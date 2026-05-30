# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        cur = root
        res = []
        while stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                res.append(stack.pop())
                cur = res[-1].right
        return res[k-1].val
            
            
            
        
        



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
        n = 0
        while stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                process = stack.pop()
                n += 1
                cur = process.right
            if n == k:
                return process.val
        return -1
        
            
            
            
        
        



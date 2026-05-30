# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minRight = 1000
        maxLeft = -1000
        return self.isBST(root, minRight, maxLeft)
    
    def isBST(self, root, minRight, maxLeft):
        if (not root):
            return True
        # mR = -1
        # mL = -1
        # # print(root.val)
        # # print(root.left.val)
        # # print(root.right.val)
        # if (root.left):
        #     mR = min(minRight, root.val)
        #     if (not (maxLeft < root.left.val < mR)):
        #         return False
        # if (root.right):
        #     mL = max(maxLeft, root.val)
        #     if (not (mL < root.right.val < minRight)):
        #         return False
        if (not (maxLeft < root.val < minRight)):
            return False
        
        return self.isBST(root.left, root.val, maxLeft) and self.isBST(root.right, minRight, root.val)

        
        #return self.isBST(root.left, mR, maxLeft) and self.isBST(root.right, minRight, mL)

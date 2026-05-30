# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)
        
        while (q):
            layer = []
            qLen = len(q)
            for i in range(qLen):
                nxt_elem = q.popleft()
                if nxt_elem:
                    layer.append(nxt_elem.val)
                    q.append(nxt_elem.left)
                    q.append(nxt_elem.right)
            if (layer):
                res.append(layer)
        
        return res
                
                
                

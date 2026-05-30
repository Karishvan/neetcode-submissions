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
        layer = []
        hashmap = {root: 0}
        layer_idx = 0
        while (q):
            nxt_elem = q.popleft()
            if nxt_elem:
                if (hashmap[nxt_elem] > layer_idx):
                    layer_idx += 1
                    res.append(layer)
                    layer = []
                layer.append(nxt_elem.val)
                q.append(nxt_elem.left)
                q.append(nxt_elem.right)
                hashmap[nxt_elem.left] = layer_idx + 1
                hashmap[nxt_elem.right] = layer_idx + 1
        if (layer):
            res.append(layer)
        return res
                
                
                

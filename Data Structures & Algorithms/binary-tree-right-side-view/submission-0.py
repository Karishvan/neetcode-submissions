# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #Idea, bfs choosing right most element

        q = deque([root])
        res = []
        while q:
            qlen = len(q)
            for i in range(qlen):
                elem = q.popleft()
                if elem:
                    if elem.left:
                        q.append(elem.left)
                    if elem.right:
                        q.append(elem.right)
                if i == qlen - 1 and elem:
                    res.append(elem.val)
        return res

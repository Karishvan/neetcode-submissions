# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque()
        res = ""
        if root:
            q.append(root)
        
        while q:
            qlen = len(q)
            for i in range(qlen):
                elem = q.popleft()
                if elem:
                    q.append(elem.left)
                    q.append(elem.right)
                    res = res + str(elem.val) + ","
                else:
                    res = res + "_"+","
        print(res)
        return res[:len(res)-1]

            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data_list = data.split(",")
        print(data_list)
        q = deque()
        if not data_list:
            return None
        root = TreeNode(data_list[0], None, None)
        q.append(root)
        i = 0
        while i < len(data_list)-1:
            elem = q.popleft()
            #print("I: ", i)
            if elem:
                print("VALUE AT I: ",  i, elem.val)
            if elem:
                
                if data_list[i+1] == '_':
                    elem.left = None
                else:
                    elem.left = TreeNode(data_list[i+1], None, None)
                    
                if data_list[i+2] == '_':
                    elem.right = None
                else:
                    elem.right = TreeNode(data_list[i+2], None, None)
                
                
                
                q.append(elem.left)
                q.append(elem.right)
                i+=2
            

        
        return root
            
        



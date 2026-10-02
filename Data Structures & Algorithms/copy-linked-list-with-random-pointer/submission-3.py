"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        traversal = head
        prev_to_node = {None: None}
        while traversal:
            new_node = Node(traversal.val, None, None)
            prev_to_node[traversal] = new_node
            traversal = traversal.next
        
        traversal = head
        while traversal:
            new_node = prev_to_node[traversal]
            rand = traversal.random
            new_node.random = prev_to_node[rand]
            new_node.next = prev_to_node[traversal.next]
            traversal = traversal.next
        
        return prev_to_node[head]
            

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
        dummy = Node(-10)
        res = dummy
        prev_to_node = {}
        while traversal:
            new_node = Node(traversal.val, traversal.next, None)
            res.next = new_node
            
            if new_node:
                prev_to_node[traversal] = new_node
            traversal = traversal.next
            res = res.next
        
        traversal2 = head
        res = dummy.next
        while traversal2:
            rand = traversal2.random
            if rand:
                res.random = prev_to_node[rand]
            res = res.next
            traversal2 = traversal2.next
        
        return dummy.next
            

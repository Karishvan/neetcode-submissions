# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        temp = head
        if (not head):
            return False
        while (temp.next):
            if (temp in seen):
                return True
            else:
                seen.add(temp)
            temp = temp.next
        
        return False
        
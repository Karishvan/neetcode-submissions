# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # going to have 2 pointers, 1 is at the beginning, and the other is at beginning + n
        # each iteration we add 1, when end is at the end (None) then we remove the element at the first pointer
        dummy = ListNode(-1, head)
        first = dummy
        second = head
        while n > 0:
            second = second.next
            n-=1
    
        while (second):
            prev = first
            first = first.next
            second = second.next

        first.next = first.next.next
        return dummy.next
        # [1,2]
        #  ^ ^
        # prev = None, first = 1, second = None, i = 1
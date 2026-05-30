# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = head
        slow = head
        fast = head.next
        if not fast:
            return
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        #print(slow.val)
        #print(fast.val)

        def reverseList(head):
            prev = None
            curr = head
            
            while(curr):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            return prev

        def merge2Lists(l1, l2):
            l1Turn = True
            print("METO")
            res = ListNode()
            while (l1 and l2):
                if (l1Turn):
                    print("L1 TURN")
                    print(l1.val)
                    res.next = l1
                    l1 = l1.next
                else:
                    print("L2 TURN")
                    print(l2.val)
                    res.next = l2
                    l2 = l2.next
                res = res.next
                l1Turn = not l1Turn
                
            if (l1):
                res.next = l1
            if (l2):
                res.next = l2
        second_half = reverseList(slow.next)
        slow.next = None
        # d2 = second_half
        # while d2:
        #     print(d2.val)
        #     d2 = d2.next
        merge2Lists(dummy, second_half)
        
        # Slow here will be the half way point, we then merge the 2 linked lists
        




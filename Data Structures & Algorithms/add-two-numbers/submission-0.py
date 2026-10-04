# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            val1 = l1.val
            val2 = l2.val
            sum_vals = val1 + val2 + carry
            carry = sum_vals // 10
            res = sum_vals % 10
            cur.next = ListNode(res)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            sum_vals = l1.val + carry
            carry = sum_vals // 10
            res = sum_vals % 10
            cur.next = ListNode(res)
            cur = cur.next
            l1 = l1.next

        while l2:
            sum_vals = l2.val + carry
            carry = sum_vals // 10
            res = sum_vals % 10
            cur.next = ListNode(res)
            cur = cur.next
            l2 = l2.next
        if carry > 0:
            cur.next = ListNode(carry)
        return dummy.next


            
        
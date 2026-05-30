# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode
        temp = res
        atLeastOne = False

        while (list1 or list2):
            atLeastOne = True
            val = -1
            if (list1 is None):
                val = list2.val
                list2 = list2.next
            elif (list2 is None):
                val = list1.val
                list1 = list1.next
            else:
                if (list1.val < list2.val):
                    val = list1.val
                    list1 = list1.next
                else:
                    val = list2.val
                    list2 = list2.next
            
            temp.next = ListNode(val, None)
            temp = temp.next
        
        if (not atLeastOne):
            return None
        return res.next

            



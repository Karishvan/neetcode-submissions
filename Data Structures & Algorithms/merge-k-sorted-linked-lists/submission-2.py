# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # INFO
            # each linked list is sorted, ascending
            # result is merged linked list

        # Idea
            # Have a pointer at the beginning of each linked list, compare to determine which one is smallest
            # add that one to result, advance the pointer
            
            # each pointer is stored in an array, of size len(lists)

            # O(n*m) time
            # O(1) space, for pointers result and resultingPointer
        result = ListNode()
        resultingPointer = result
        def findMin(pointers):
            minVal = float('inf')
            minValIndex = -1
            for i in range(len(pointers)):
                if pointers[i] and pointers[i].val < minVal:
                    minVal = pointers[i].val
                    minValIndex = i
                #print(minValIndex)
            return minValIndex
        end = False
        
        pointers = [0] * len(lists)

        for i in range(len(lists)):
            pointers[i] = lists[i]

        while True:
            minIndex = findMin(pointers)
            if (minIndex == -1):
                break
            resultingPointer.next = pointers[minIndex]
            pointers[minIndex] = pointers[minIndex].next
            resultingPointer = resultingPointer.next


        return result.next
            

        
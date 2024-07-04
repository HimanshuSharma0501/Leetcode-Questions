# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        current=dummy
        head=head.next
        currentSum=0
        while head is not None:
            if head.val==0:
                if currentSum>0:
                    current.next=ListNode(currentSum)
                    current=current.next
                currentSum=0
            else:
                currentSum+=head.val
            head=head.next
        return dummy.next

        
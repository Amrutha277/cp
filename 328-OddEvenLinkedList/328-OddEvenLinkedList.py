# Last updated: 7/9/2025, 7:07:33 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd= head
        even= head.next
        even_og= even

        while even and even.next:
            odd.next= even.next
            odd= odd.next

            even.next= odd.next
            even= even.next

        
        odd.next= even_og
        

        return head

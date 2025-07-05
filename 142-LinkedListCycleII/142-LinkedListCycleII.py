# Last updated: 7/5/2025, 7:05:13 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
            slow, fast= head, head
            while fast and fast.next:
                slow= slow.next
                fast= fast.next.next
                if slow== fast:
                    ptr= head
                    while ptr != slow:
                        ptr= ptr.next
                        slow= slow.next
                    return ptr
            return None
# Last updated: 7/5/2025, 8:05:12 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # nodeslist= []
        # cur= head
        # while cur:
        #     nodeslist.append(cur.val)
        #     cur= cur.next
        
        # left, right= 0, len(nodeslist)-1
        # while left<right:
        #     if nodeslist[left] != nodeslist[right]:
        #         return False
        #     left+=1
        #     right-=1
        # return True

        slow, fast= head, head
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
        prev= None
        
        while slow:
            temp= slow.next
            slow.next= prev
            prev= slow
            slow= temp

        left, right= head, prev
        while right:
            if left.val != right.val:
                return False
            left= left.next
            right= right.next
        return True 




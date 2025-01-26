# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        temp = headA
        a_set= set()

        while temp is not None:
            a_set.add(temp)
            temp= temp.next
        
        temp1= headB
        while temp1 is not None:
            if temp1 in a_set:
                return temp1
            temp1= temp1.next
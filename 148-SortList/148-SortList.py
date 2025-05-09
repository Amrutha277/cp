class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head  
        
        left, right = self.split_list(head)  
        left = self.sortList(left)  
        right = self.sortList(right)  
        
        return self.merge_lists(left, right)  

    def split_list(self, head):
        if not head or not head.next:
            return head, None

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow.next
        slow.next = None  
        return head, middle

    def merge_lists(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next

        tail.next = l1 or l2  
        return dummy.next

# Last updated: 4/18/2025, 4:40:59 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result=[]
        s1=[]
        if not root:
            return []
        visited=None
        current=root
        while current or s1:
            if current:
                s1.append(current)
                current= current.left
            else:
                peek=s1[-1]
                if peek.right and visited!= peek.right:
                    current= peek.right
                else:
                    result.append(peek.val)
                    visited= s1.pop()
        return result

